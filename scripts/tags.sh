#!/usr/bin/env bash
#
# Version tags of this repository. The rules are in docs/runbooks/deploy.md.
#
#   Master tag          0.0.1            every push to master gets the next one
#   Pull request tag    0.0.1-PR2-003    master version, pull request number,
#                                        sequence number within the pull request
#
# Commands that read the tags of the remote from standard input:
#
#   git ls-remote --tags origin | scripts/tags.sh next-master <commit>
#   git ls-remote --tags origin | scripts/tags.sh next-pr <pr-number> <commit>
#       Print the next tag for the commit. Print nothing if the commit
#       already has a tag of that kind.
#
#   git ls-remote --tags origin | scripts/tags.sh stale "<tags to keep>" [open-pr-number...]
#       Print the pull request tags whose pull request is not open,
#       except the tags to keep.
#
# Commands that take one tag:
#
#   scripts/tags.sh kind <tag>         Print "master" or "pr". Fail for any other tag.
#   scripts/tags.sh pr-number <tag>    Print the pull request number of a pull request tag.

set -euo pipefail

MASTER_TAG='^([0-9]+)\.([0-9]+)\.([0-9]+)$'
PR_TAG='^([0-9]+)\.([0-9]+)\.([0-9]+)-PR([0-9]+)-([0-9]+)$'

# Tag name -> commit.
declare -A commit_of=()

usage() {
    sed -n '3,23s/^# \{0,1\}//p' "$0" >&2
    exit 2
}

# Reads the output of "git ls-remote --tags". An annotated tag has two lines.
# The line that ends with ^{} names the commit, so it replaces the other line.
read_tags() {
    local sha ref name
    while read -r sha ref; do
        if [[ $ref != refs/tags/* ]]; then
            continue
        fi
        name=${ref#refs/tags/}
        if [[ $name == *'^{}' ]]; then
            commit_of[${name%'^{}'}]=$sha
        elif [[ -z ${commit_of[$name]:-} ]]; then
            commit_of[$name]=$sha
        fi
    done
}

# Prints the highest master tag, or nothing if there is none.
latest_master() {
    local name
    for name in "${!commit_of[@]}"; do
        if [[ $name =~ $MASTER_TAG ]]; then
            printf '%s\n' "$name"
        fi
    done | sort -t. -k1,1n -k2,2n -k3,3n | tail -n 1
}

next_master() {
    local commit=$1 name latest
    for name in "${!commit_of[@]}"; do
        if [[ $name =~ $MASTER_TAG && ${commit_of[$name]} == "$commit" ]]; then
            return 0
        fi
    done
    latest=$(latest_master)
    if [[ -z $latest ]]; then
        echo "0.0.1"
        return 0
    fi
    [[ $latest =~ $MASTER_TAG ]]
    echo "$((10#${BASH_REMATCH[1]})).$((10#${BASH_REMATCH[2]})).$((10#${BASH_REMATCH[3]} + 1))"
}

next_pr() {
    local pr=$1 commit=$2 name base sequence highest=0
    for name in "${!commit_of[@]}"; do
        if [[ $name =~ $PR_TAG && $((10#${BASH_REMATCH[4]})) -eq $((10#$pr)) ]]; then
            sequence=$((10#${BASH_REMATCH[5]}))
            if [[ ${commit_of[$name]} == "$commit" ]]; then
                return 0
            fi
            if ((sequence > highest)); then
                highest=$sequence
            fi
        fi
    done
    base=$(latest_master)
    printf '%s-PR%d-%03d\n' "${base:-0.0.0}" "$((10#$pr))" "$((highest + 1))"
}

stale() {
    local keep=" ${1//$'\n'/ } "
    shift
    local open=" $* " name pr
    for name in "${!commit_of[@]}"; do
        if [[ $name =~ $PR_TAG ]]; then
            pr=$((10#${BASH_REMATCH[4]}))
            if [[ $open != *" $pr "* && $keep != *" $name "* ]]; then
                printf '%s\n' "$name"
            fi
        fi
    done | sort
}

kind() {
    if [[ $1 =~ $MASTER_TAG ]]; then
        echo "master"
    elif [[ $1 =~ $PR_TAG ]]; then
        echo "pr"
    else
        echo "Not a version tag: '$1'. Expected a tag like 0.0.1 or 0.0.1-PR2-003." >&2
        return 1
    fi
}

pr_number() {
    if [[ $1 =~ $PR_TAG ]]; then
        echo "$((10#${BASH_REMATCH[4]}))"
    else
        echo "Not a pull request tag: '$1'. Expected a tag like 0.0.1-PR2-003." >&2
        return 1
    fi
}

command=${1:-}
case "$command" in
    next-master)
        [[ $# -eq 2 ]] || usage
        read_tags
        next_master "$2"
        ;;
    next-pr)
        [[ $# -eq 3 && $2 =~ ^[0-9]+$ ]] || usage
        read_tags
        next_pr "$2" "$3"
        ;;
    stale)
        [[ $# -ge 2 ]] || usage
        shift
        read_tags
        stale "$@"
        ;;
    kind)
        [[ $# -eq 2 ]] || usage
        kind "$2"
        ;;
    pr-number)
        [[ $# -eq 2 ]] || usage
        pr_number "$2"
        ;;
    *)
        usage
        ;;
esac
