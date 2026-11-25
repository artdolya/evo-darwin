# 0002. Versions and releases

## Status

Accepted, 2026-11-24.

## Context

[ADR 0001](0001-repository-structure.md) set up three environments (dev, staging and prod) and a CD workflow that deployed every push to `master` to all three in that order. An image was tagged with the commit SHA it was built from.

This ADR changes two things that ADR 0001 records: the list of environments in its decision 4, and the order in which the pipeline deploys to them. The rest of ADR 0001 stands.

The owner of the repository asked for a different flow, with these requirements:

- `master` has version tags in the format `0.0.1`.
- Every pull request produces tags in the format `0.0.1-PR2-003`: the master version, the number of the pull request, and a sequence number within the pull request.
- A release can be started from a pull request tag. It produces the artifacts and deploys them to a test environment.
- A release can be started from a master tag. It deploys to prod.
- When a pull request is merged, its tags and the packages produced from them are removed.
- In the pilot, test and prod are the same environment.

TODO: record why every merge is no longer deployed automatically, and which other flows were considered. The requirements were given without the reasons.

## Decision

### 1. Every push gets a version tag

We will give every push to `master` a master tag, and every push to a pull request a pull request tag. The Tag workflow creates them.

- A master tag is the highest master tag with its last number increased by 1. The first one is `0.0.1`. A new minor or major version is started by hand, with a tag such as `0.1.0` on a commit of `master`.
- A pull request tag is the highest master tag, the number of the pull request and a sequence number: `0.0.1-PR2-003`.

Reason for increasing the last number automatically: a merge then needs no decision about the version, and every commit of `master` that is released has a tag.

### 2. A release is started by hand, for one tag

We will deploy only when someone starts the Release workflow with a tag. A pull request tag is released to test, and a master tag to prod. The image, the Helm chart and the Terraform code all come from the tag, and the image tag is the version tag.

### 3. The tags of closed pull requests are deleted, except a deployed one

We will delete the tags of a pull request when it is closed, merged or not, and delete their images with them. We will keep a tag while its version is deployed, and delete it after another version is deployed.

Reason for the exception: an environment pulls the image again when a pod restarts. In the pilot a pull request build can be the version that runs in prod, and deleting its image at the merge would break the next restart.

### 4. The environments are test and prod, and in the pilot they are one

We will remove the dev and staging environments. `deploy/terraform/environments/` keeps one folder, `prod`, and both kinds of release deploy to it during the pilot.

Reason for one folder: each folder is a Terraform root with its own state. Two roots cannot manage the same namespace and the same Helm release.

### 5. The tag rules are in one script

We will keep the rules for the tags in `scripts/tags.sh`, and call it from the Tag, Release and Cleanup workflows.

Reason: the rules can be run and tested without GitHub, and the three workflows cannot drift apart.

## Consequences

- A merge deploys nothing. A version reaches prod only when someone releases its tag.
- Any master tag can be released, so a rollback is a release of an earlier tag. See [rollback.md](../runbooks/rollback.md).
- The image that reaches prod is built from the master tag. It is not the image that was tested from the pull request tag.
- In the pilot, a release of a pull request tag replaces the version that runs in prod.
- The Release workflow does not check that CI passed for the tag.
- Under the rules of Semantic Versioning, `0.0.1-PR2-003` is older than `0.0.1`, although it was built later. Nothing in this repository compares versions today. Revisit the format before a version is used where the order matters, for example as a NuGet package version.
- The Cleanup workflow needs read access to the Terraform state of every environment, because the state records the deployed version.
- Images are not deleted yet. The delete command depends on the container registry, which is not chosen. Until it is added, the Cleanup workflow deletes only the tags.
- A tag that a workflow creates does not start another workflow. A release cannot be started by the creation of a tag unless the Tag workflow gets a different token.
- When a separate test environment is created, it needs its own folder in `deploy/terraform/environments/`, and the Release workflow has to use it for pull request tags. See [deploy.md](../runbooks/deploy.md#environments).
