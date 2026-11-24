# Roll back

How to return an environment to the previous version of the service. Read [deploy.md](deploy.md) first: a rollback uses the same pipeline.

## Choose the procedure

| Situation | Procedure |
| --- | --- |
| The deploy job failed because the new pods did not become ready | [The rollout rolled back on its own](#the-rollout-rolled-back-on-its-own) |
| The deployment succeeded and the new version misbehaves | [Revert the commit](#revert-the-commit) |
| The same, and waiting for a revert pull request takes too long | [Re-run the last good deployment](#re-run-the-last-good-deployment), then revert the commit |

## The rollout rolled back on its own

Terraform waits up to 5 minutes for the new pods to pass the readiness probe. If they do not, Helm returns the release to the previous version, `terraform apply` fails, and the deploy job is red. The environments after it are not deployed.

1. Open the failed deploy job in the **CD** run and confirm that the **Terraform apply** step failed while it waited for the release.
2. [Verify](#verify) that the environment runs the previous image.
3. [Revert the commit](#revert-the-commit) or fix it in a new pull request. Until then `main` holds a version that cannot be deployed.

If the very first deployment to an environment fails, there is no previous version. Helm removes the release.

## Revert the commit

This is the standard rollback. It keeps `main` equal to what is deployed.

1. Find the commit that introduced the problem.
2. Create a branch and revert the commit:

   ```bash
   git revert <commit SHA>
   ```

3. Open a pull request, get it reviewed, and merge it into `main`.
4. The **CD** workflow builds a new image from the reverted code and deploys it to dev.
5. Approve **staging**, then **prod**, as in [deploy.md](deploy.md#deploy-a-change).
6. [Verify](#verify) each environment.

A rollback by revert takes as long as a normal deployment.

## Re-run the last good deployment

This is faster than a revert because it needs no pull request. It returns the image, the chart and the Terraform code to the last good commit.

1. In GitHub, open **Actions**, then **CD**.
2. Open the last run that deployed the good version. The run shows its commit SHA.
3. Select **Re-run all jobs**.
4. The run builds the image from that commit again, pushes it with the same tag, and deploys it to dev.
5. Approve **staging**, then **prod**.
6. [Verify](#verify) each environment.
7. [Revert the commit](#revert-the-commit) before anything else is merged. `main` still contains the bad commit, and the next merge would deploy it again.

Limits:

- GitHub re-runs a workflow run only within 30 days of its first run. For an older version, revert the commit.
- The build job pushes a tag that already exists in the registry. It fails if the registry does not allow a tag to be overwritten.

TODO: once the container registry is chosen, state here whether it allows a tag to be overwritten. If it does not, this procedure does not work as written.

## Do not roll back by hand

Do not use `helm rollback` or `kubectl rollout undo` as the normal procedure. They change the cluster without Terraform, so the Terraform state still records the version that was rolled away from, and `main` still contains it. If you had to use one of them because the pipeline was unavailable, [revert the commit](#revert-the-commit) as soon as the pipeline works again.

## Verify

With `kubectl` pointed at the cluster of the environment:

1. Check the image that is deployed. The tag is the commit SHA of the version you rolled back to:

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
