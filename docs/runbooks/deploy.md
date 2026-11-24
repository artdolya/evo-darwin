# Deploy

How a change reaches dev, staging and prod. The pipeline is [.github/workflows/cd.yml](../../.github/workflows/cd.yml).

## How deployment works

1. A pull request is merged into `main`. The **CD** workflow starts.
2. The **Build and push image** job builds the image from `deploy/docker/Dockerfile` and pushes it as `<IMAGE_REPOSITORY>:<commit SHA>`.
3. The **Deploy to dev** job runs `terraform apply` in `deploy/terraform/environments/dev` with that image tag. It starts without approval.
4. The **Deploy to staging** job waits for approval, then runs `terraform apply` in `environments/staging`.
5. The **Deploy to prod** job waits for approval, then runs `terraform apply` in `environments/prod`.

Each job starts only if the job before it succeeded.

Each `terraform apply` creates the `evo-darwin` namespace if it does not exist, and installs or upgrades the Helm release `evo-darwin` from the chart in `deploy/helm/evo-darwin`. Terraform waits up to 5 minutes for the new pods to pass the readiness probe on `/health`. If they do not, Helm returns the release to the previous version and the job fails.

Only one deployment to an environment runs at a time. A later run waits for the running one.

The CD workflow does not wait for the **CI** workflow. Both start on the same push to `main`.

## Before the first deployment

The pipeline cannot deploy until every item below is done. Each one is marked `TODO` in the file named.

TODO: choose the container registry, create the GitHub repository variable `IMAGE_REPOSITORY`, and add the registry login step to the build job in `cd.yml`. Until the variable exists, the build job fails with a message that names it and nothing is deployed.

TODO: add the cloud provider login to each deploy job in `cd.yml` and to the plan job in `terraform-plan.yml`.

TODO: configure access to each cluster in `providers.tf` of each folder in `deploy/terraform/environments/`.

TODO: configure the Terraform backend in `versions.tf` of each environment folder. Without it the state is lost after every run and the second deployment fails.

TODO: create the GitHub environments `dev`, `staging` and `prod` in the repository settings, and add required reviewers to `staging` and `prod`. Until the reviewers are set, the staging and prod jobs run without waiting for approval.

TODO: require the **CI** check on pull requests in the branch protection of `main`, so that only tested commits are deployed.

## Deploy a change

1. Merge the pull request into `main`.
2. In GitHub, open **Actions**, then **CD**, then the run of your commit.
3. Wait until **Deploy to dev** is green. [Verify](#verify-a-deployment) dev.
4. On the run page select **Review deployments**, tick **staging**, and select **Approve and deploy**. Only a required reviewer of the environment can approve.
5. Wait until **Deploy to staging** is green. Verify staging.
6. Approve **prod** in the same way. Wait until **Deploy to prod** is green. Verify prod.

To stop a change before staging or prod, select **Reject** instead of approving.

## Verify a deployment

A green deploy job means that Terraform saw the new pods become ready. To check by hand, with `kubectl` pointed at the cluster of the environment:

1. Check that the rollout is complete:

   ```bash
   kubectl -n evo-darwin rollout status deployment/evo-darwin
   ```

2. Check the image that is deployed. The tag is the commit SHA:

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

- **Chart.** Bump `version` in `deploy/helm/evo-darwin/Chart.yaml` in every pull request that changes the chart. Terraform upgrades the release when the chart version or the values passed to the chart change. A CD run always passes a new image tag, so it also applies the current chart. Without a new image tag, a chart change with an unchanged version is not applied.
- **Terraform.** A pull request that changes `deploy/terraform` runs the **Terraform plan** workflow. It checks the formatting and shows the plan for dev, staging and prod. Read the three plans before you approve the pull request. The change is applied by the CD workflow after the merge, in the same order as a code change.

## If a deployment fails

1. Open the failed job and read the output of the **Terraform apply** step.
2. If the pods did not become ready, Helm has already returned the environment to the previous version. The environments after it were not changed.
3. Fix the cause in a new pull request, or revert the commit. See [rollback.md](rollback.md).
