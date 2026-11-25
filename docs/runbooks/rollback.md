# Roll back

How to return an environment to an earlier version of the service. Read [deploy.md](deploy.md) first: a rollback is a release of an earlier tag.

## Choose the procedure

| Situation | Procedure |
| --- | --- |
| The deploy job failed because the new pods did not become ready | [The rollout rolled back on its own](#the-rollout-rolled-back-on-its-own) |
| The deployment succeeded and the new version misbehaves | [Release the last good version](#release-the-last-good-version), then [fix master](#fix-master-after-a-rollback) |

## The rollout rolled back on its own

Terraform waits up to 5 minutes for the new pods to pass the readiness probe. If they do not, Helm returns the release to the previous version, `terraform apply` fails, and the deploy job is red.

1. Open the failed deploy job in the **Release** run and confirm that the **Terraform apply** step failed while it waited for the release.
2. [Verify](#verify) that the environment runs the previous image.
3. Fix the cause in a pull request, and release the new tag.

If the very first deployment to an environment fails, there is no previous version. Helm removes the release.

## Release the last good version

1. Find the last good tag. The runs of the **Release** workflow are named after their tag, for example "Release 0.0.2". In GitHub, open **Actions**, then **Release**, and find the last green run before the bad release.
2. Start the **Release** workflow with that tag, as described in [deploy.md](deploy.md#release-a-master-version-to-prod).
3. The run builds the image from that tag again, pushes it with the same image tag, and deploys it. The chart and the Terraform code of that tag are applied too.
4. [Verify](#verify) the environment.
5. [Fix master](#fix-master-after-a-rollback).

Limits:

- The build job pushes an image tag that already exists in the registry. It fails if the registry does not allow a tag to be overwritten.
- The tag of a closed pull request is deleted after another version is deployed, so it cannot be released again. Release a master tag instead.

TODO: once the container registry is chosen, state here whether it allows a tag to be overwritten. If it does not, this procedure does not work as written.

## Fix master after a rollback

A rollback changes what is deployed. It does not change `master`. Until the bad change is reverted or corrected, every new master tag contains it.

1. Find the commit that introduced the problem.
2. Create a branch and revert the commit:

   ```bash
   git revert <commit SHA>
   ```

3. Open a pull request, get it reviewed, and merge it into `master`.
4. The merge creates a new master tag. Release it as described in [deploy.md](deploy.md#release-a-master-version-to-prod).

## Do not roll back by hand

Do not use `helm rollback` or `kubectl rollout undo` as the normal procedure. They change the cluster without Terraform, so the Terraform state still records the version that was rolled away from. The Cleanup workflow reads the deployed version from the Terraform state, so it can delete the tag of the version that really runs.

If you had to use one of them because the pipeline was unavailable, release the version that is running as soon as the pipeline works again. The Terraform state then matches the cluster.

## Verify

With `kubectl` pointed at the cluster of the environment:

1. Check the image that is deployed. Its tag is the version tag that you rolled back to:

   ```bash
   kubectl -n evo-darwin get deployment evo-darwin -o jsonpath='{.spec.template.spec.containers[0].image}'
   ```

2. Check that all pods are ready:

   ```bash
   kubectl -n evo-darwin rollout status deployment/evo-darwin
   ```

3. Call `/health` as described in [deploy.md](deploy.md#verify-a-deployment).

## Database changes

The service has no database yet, so a rollback changes only the running code.

TODO: when database migrations are added, describe here how a rollback handles a schema that the previous version does not expect.
