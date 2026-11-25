# Deploy

How a version of the service is tagged, released and deployed. A deployment is started by hand. Nothing is deployed when a pull request is merged.

A release builds and deploys `Evo.Darwin.Api` only. The other components of the repository have no container image and are not deployed: see the [architecture overview](../architecture/overview.md#deployment).

| Workflow | File | What it does |
| --- | --- | --- |
| **Tag** | [tag.yml](../../.github/workflows/tag.yml) | Gives every push a version tag. |
| **Release** | [release.yml](../../.github/workflows/release.yml) | Builds the image of one tag and deploys it. You start it by hand. |
| **Cleanup** | [cleanup.yml](../../.github/workflows/cleanup.yml) | Deletes the tags of closed pull requests. |

The reasons for this flow are recorded in [ADR 0002](../adr/0002-versions-and-releases.md).

## Versions and tags

Every build has a version, and the version is a Git tag. The **Tag** workflow creates the tags.

| Tag | Example | Created by | Released to |
| --- | --- | --- | --- |
| Master tag | `0.0.2` | A push to `master`, which is normally the merge of a pull request | prod |
| Pull request tag | `0.0.1-PR2-003` | A push to a pull request | test |

- **Master tag.** The workflow takes the highest master tag and adds 1 to its last number: after `0.0.1` comes `0.0.2`. The first tag is `0.0.1`.
- **Pull request tag.** It has three parts: the highest master tag at the time of the push, the number of the pull request, and a sequence number. The sequence number starts at `001` and grows with every push to the pull request. `0.0.1-PR2-003` is the third push to pull request 2, made when `master` was at `0.0.1`. Before the first master tag exists, the first part is `0.0.0`.
- The tag of a pull request points at the last commit of its branch.
- A commit gets one tag of each kind. If the workflow runs again for the same commit, it creates nothing.
- The workflow writes the tag it created to the summary of its run.
- When pushes follow each other faster than the workflow runs, a commit in the middle can stay without a tag. The newest commit always gets one.
- A pull request from a fork gets no tag.

The rules are implemented in [scripts/tags.sh](../../scripts/tags.sh).

To start a new minor or major version, create the tag by hand on a commit of `master`:

```bash
git tag 0.1.0 <commit SHA>
```

```bash
git push origin 0.1.0
```

The next push to `master` then gets `0.1.1`.

## Environments

A release has one of two targets: **test** for a pull request tag, and **prod** for a master tag.

In the pilot, test and prod are the same environment. It is defined in `deploy/terraform/environments/prod`, and both kinds of release deploy to it. A release of a pull request tag therefore replaces the version that runs in prod.

TODO: create a separate test environment after the pilot. Add the folder `deploy/terraform/environments/test`, use it for pull request tags in the **Choose the environment** step of `release.yml`, and add it to the matrix in `terraform-plan.yml`.

## How a release works

The **Release** workflow takes one input, the tag, and runs four jobs:

1. **Check the tag.** The tag must exist and must be a master tag or a pull request tag. A master tag must point at a commit of `master`. The kind of tag selects the target: test or prod.
2. **Build and push image.** Builds the image from `deploy/docker/Dockerfile` at the tag and pushes it as `<IMAGE_REPOSITORY>:<tag>`.
3. **Deploy to test** or **Deploy to prod.** Runs `terraform apply` in the Terraform folder of the environment with that image tag. The chart and the Terraform code are taken from the tag too.
4. **Cleanup.** Runs the **Cleanup** workflow. See [Cleanup](#cleanup).

Each job starts only if the job before it succeeded.

`terraform apply` creates the `evo-darwin` namespace if it does not exist, and installs or upgrades the Helm release `evo-darwin` from the chart in `deploy/helm/evo-darwin`. Terraform waits up to 5 minutes for the new pods to pass the readiness probe on `/health`. If they do not, Helm returns the release to the previous version and the job fails.

Only one deployment to an environment runs at a time. A later run waits for the running one.

The Release workflow does not check that the **CI** workflow passed for the commit of the tag. Check that yourself before you release.

## Before the first deployment

The pipeline cannot deploy until every item below is done. Each one is marked `TODO` in the file named.

TODO: choose the container registry, create the GitHub repository variable `IMAGE_REPOSITORY`, and add the registry login step to the build job in `release.yml`. Until the variable exists, the build job fails with a message that names it and nothing is deployed.

TODO: add the cloud provider login to the deploy job in `release.yml`, to the plan job in `terraform-plan.yml` and to the job in `cleanup.yml`. The Cleanup workflow only reads the Terraform state.

TODO: configure access to each cluster in `providers.tf` of each folder in `deploy/terraform/environments/`.

TODO: configure the Terraform backend in `versions.tf` of each environment folder. Without it the state is lost after every run: the second deployment fails, and the Cleanup workflow treats no version as deployed.

TODO: create the GitHub environments `test` and `prod` in the repository settings. Add required reviewers to `prod` if a release to prod needs an approval. Without reviewers the deploy job starts as soon as the image is built.

TODO: require the **CI** check on pull requests in the branch protection of `master`, so that only tested commits reach `master`.

TODO: decide who may create or delete version tags by hand, and protect the master tags with a tag ruleset if needed. The Tag and Cleanup workflows must keep the right to create and delete tags.

## Release a pull request build to test

1. Push to the pull request and wait for the **Tag** workflow. Open its run and read the tag in the summary, for example `0.0.1-PR2-003`.
2. In GitHub, open **Actions**, then **Release**, then **Run workflow**. Leave the branch on `master`, enter the tag, and select **Run workflow**. Or start it from a terminal:

   ```bash
   gh workflow run release.yml -f tag=0.0.1-PR2-003
   ```

3. Wait until **Deploy to test** is green. [Verify](#verify-a-deployment) the environment.

## Release a master version to prod

1. Merge the pull request into `master` and wait for the **Tag** workflow. Its summary shows the new tag, for example `0.0.2`.
2. Check that the **CI** run of that commit is green.
3. Start the **Release** workflow with the tag, in the same way as for a pull request tag:

   ```bash
   gh workflow run release.yml -f tag=0.0.2
   ```

4. If the GitHub environment `prod` has required reviewers, the **Deploy to prod** job waits. A reviewer opens the run, selects **Review deployments**, ticks **prod**, and selects **Approve and deploy**.
5. Wait until **Deploy to prod** is green. [Verify](#verify-a-deployment) the environment.

Any master tag can be released, not only the newest one. A [rollback](rollback.md) is a release of an earlier tag.

## Cleanup

The **Cleanup** workflow runs when a pull request is closed, merged or not, and after every release. It deletes the tags of every pull request that is not open.

It keeps a tag that is deployed, because the environment still pulls the image of that version. The Terraform state of each environment records the deployed tag, and the workflow reads it from there. The kept tag is deleted by the run that follows the next release.

Master tags are never deleted.

TODO: delete the container images too. The delete command depends on the registry, which is not chosen yet. Today the workflow deletes only the tags and prints a warning that names them. The place for the command is marked in `cleanup.yml`.

Your local clone keeps tags that were deleted on GitHub. To remove them:

```bash
git fetch --prune --prune-tags origin
```

## Verify a deployment

A green deploy job means that Terraform saw the new pods become ready. To check by hand, with `kubectl` pointed at the cluster of the environment:

1. Check that the rollout is complete:

   ```bash
   kubectl -n evo-darwin rollout status deployment/evo-darwin
   ```

2. Check the image that is deployed. Its tag is the version tag that you released:

   ```bash
   kubectl -n evo-darwin get deployment evo-darwin -o jsonpath='{.spec.template.spec.containers[0].image}'
   ```

3. Call the health endpoint. Forward a local port to the Service:

   ```bash
   kubectl -n evo-darwin port-forward service/evo-darwin 8080:80
   ```

   Then, in a second terminal:

   ```bash
   curl http://localhost:8080/health
   ```

   The response is `Healthy`.

TODO: describe how an engineer gets `kubectl` access to the cluster of each environment.

## Change the chart or the Terraform code

A release takes the chart and the Terraform code from the tag that is released. A change to them is applied by the first release of a tag that contains it. A release of an earlier tag applies the earlier chart and Terraform code.

- **Chart.** Bump `version` in `deploy/helm/evo-darwin/Chart.yaml` in every pull request that changes the chart. Terraform upgrades the Helm release when the chart version or the values passed to the chart change. A release of another tag passes a new image tag, so it also applies the chart. Without a new image tag, a chart change with an unchanged version is not applied.
- **Terraform.** A pull request that changes `deploy/terraform` runs the **Terraform plan** workflow. It checks the formatting and shows the plan for prod. Read the plan before you approve the pull request.

## If a deployment fails

1. Open the failed job and read the output of the **Terraform apply** step.
2. If the pods did not become ready, Helm has already returned the environment to the previous version.
3. Fix the cause in a pull request and release the new tag, or release the last good tag. See [rollback.md](rollback.md).
