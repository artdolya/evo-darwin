# Configuration

Every environment variable and secret of the service and of its pipeline. Add a row in the same pull request that adds or changes a variable, and update the "Environment variables" section in the README of the project that reads it.

## How the service reads configuration

The service uses the ASP.NET Core defaults. It reads `src/Evo.Darwin.Api/appsettings.json` first, then environment variables. An environment variable overrides the file. For a nested key, join the levels with two underscores: the key `Logging:LogLevel:Default` is the variable `Logging__LogLevel__Default`.

## Service

| Name | Meaning | Required | Default | Where the value comes from |
| --- | --- | --- | --- | --- |
| `ASPNETCORE_ENVIRONMENT` | Name of the environment the service runs in. `Development` serves the OpenAPI document and shows detailed error pages. | No | `Production` | Local run: `Properties/launchSettings.json` sets `Development`. Kubernetes: the chart value `env.ASPNETCORE_ENVIRONMENT`, which Terraform sets for each environment (see [Terraform](#terraform)). |
| `ASPNETCORE_HTTP_PORTS` | Port the service listens on in the container. | No | `8080` | Set by the .NET base image. The chart value `containerPort` must match it. A local run uses port 5080 from `Properties/launchSettings.json` instead. |
| `ASPNETCORE_URLS` | Address the service listens on. Used in a local run only. | No | None | `dotnet run` sets it to `http://localhost:5080` from `Properties/launchSettings.json`. Not set in the container. |
| `Logging__LogLevel__Default` | Lowest log level that is written. | No | `Information` | `appsettings.json` |
| `Logging__LogLevel__Microsoft.AspNetCore` | Lowest log level written for ASP.NET Core's own messages. | No | `Warning` | `appsettings.json` |
| `AllowedHosts` | Host names the service accepts in the `Host` header. `*` accepts all. | No | `*` | `appsettings.json` |

## Secrets

The service uses no secrets today.

TODO: decide how secrets reach the pods, and document the mechanism here before the first secret is added. Then list every secret in a table with the same columns as above.

## Pipeline

Used by `.github/workflows/cd.yml` and `.github/workflows/terraform-plan.yml`.

| Name | Meaning | Required | Default | Where the value comes from |
| --- | --- | --- | --- | --- |
| `IMAGE_REPOSITORY` | Container image repository without a tag: `<registry>/<path>/evo-darwin`. | Yes | None | GitHub repository variable `IMAGE_REPOSITORY` (Settings, Secrets and variables, Actions, Variables). |
| `IMAGE_TAG` | Tag of the image that is built and deployed. | Yes | The commit SHA | Set in `cd.yml` from `github.sha`. |
| `TERRAFORM_VERSION` | Terraform version installed in the pipeline. | Yes | `1.15.6` | Set in both workflow files. |
| `TF_IN_AUTOMATION` | Tells Terraform that it runs in a pipeline, so it leaves out hints meant for interactive use. | No | `true` | Set in both workflow files. |

TODO: create the repository variable `IMAGE_REPOSITORY` once the container registry is chosen.

TODO: add the secrets or settings used to log in to the container registry. The registry is not known yet.

TODO: add the cloud credentials of each environment (dev, staging, prod). The cloud provider is not known yet.

TODO: add the settings that give Terraform access to each cluster. With no provider arguments, the Kubernetes and Helm providers read the `KUBE_*` environment variables, for example `KUBE_CONFIG_PATH`.

TODO: add the settings of the Terraform backend of each environment. The backend is not known yet.

## Terraform

Input variables of each environment folder in `deploy/terraform/environments/`. The pipeline passes them with `-var`.

| Name | Meaning | Required | Default | Where the value comes from |
| --- | --- | --- | --- | --- |
| `image_repository` | Container image repository without a tag. | Yes | None | `IMAGE_REPOSITORY` |
| `image_tag` | Tag of the image to deploy. | Yes | None | `IMAGE_TAG` in `cd.yml`. `terraform-plan.yml` uses the tag that is deployed now. |

Values that differ by environment are set in `main.tf` of each environment folder:

| Setting | dev | staging | prod |
| --- | --- | --- | --- |
| `namespace` | `evo-darwin` | `evo-darwin` | `evo-darwin` |
| `aspnetcore_environment` | `Development` | `Staging` | `Production` |
| `replica_count` | 1 | 1 | 2 |

TODO: set the prod replica count from the expected load. Two is a placeholder.

## Helm chart

The chart values and their defaults are in [deploy/helm/evo-darwin/values.yaml](../deploy/helm/evo-darwin/values.yaml). Terraform overrides `replicaCount`, `image.repository`, `image.tag` and `env.ASPNETCORE_ENVIRONMENT`.

To pass a new environment variable to the container, add it under `env` and add a row to the [Service](#service) table. If the value is the same in every environment, add it in `values.yaml`. If it differs, add it to the values that `deploy/terraform/modules/service/main.tf` passes to the chart.
