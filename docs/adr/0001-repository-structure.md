# 0001. Repository structure

## Status

Accepted, 2026-11-24.

Partly superseded by [0002](0002-versions-and-releases.md) on 2026-11-24: the list of environments in decision 4, and the order in which the pipeline deploys to them. The rest of this ADR stands.

Partly superseded by [0003](0003-services-and-components.md) on 2026-11-24: the repository holds several services and not Darwin alone, and in decision 2 the Api no longer references Infrastructure. The rest of this ADR stands.

## Context

This repository holds Darwin, a .NET 10 Web API service in the Evo project. It was created empty, and its structure had to be fixed before the first feature.

- A project usually grows into several components (an API, a worker and others) while the project name stays.
- The service handles data in three shapes: the requests and responses of its external API, the types on the message bus and in the business layer, and the rows of its database tables.
- The service is built and tested by GitHub Actions, packaged as a container image, and deployed to Kubernetes.
- There are three environments: dev, staging and prod.
- Documentation lives in the repository so that it is reviewed and versioned in the same pull requests as the code.

TODO: record the options that were considered and rejected for each decision below. They were not available when this ADR was written.

## Decision

### 1. Projects are named `<Project>.<Service>.<Component>`

Every .NET project is named `Evo.Darwin.<Component>`, for example `Evo.Darwin.Api`. The kebab-case form `evo-darwin` names the Helm chart, its folder, the Kubernetes namespace and the Kubernetes resources.

Reason: the components of a service change over time, and the project and service names do not. A shared prefix keeps all components of the service together under one name, and a new component such as `Evo.Darwin.Worker` is added without renaming anything.

### 2. Contracts, Models and Entities are three separate projects

- `Evo.Darwin.Contracts` holds the request and response types of the external API.
- `Evo.Darwin.Models` holds the types used on the message bus and in the business layer.
- `Evo.Darwin.Entities` holds the classes that describe the database tables.

None of the three references another project. `Evo.Darwin.Api` maps between Contracts and Models. `Evo.Darwin.Infrastructure` maps between Entities and Models. `Evo.Darwin.Domain` works with Models only. The Api never returns Entities, and Contracts types never reach Domain or Infrastructure.

### 3. Terraform deploys the Helm chart

The service has its own Helm chart in `deploy/helm/evo-darwin`. The Terraform module in `deploy/terraform/modules/service` creates the namespace and installs the chart through a `helm_release` resource. The pipeline runs `terraform apply` and never calls Helm directly.

### 4. Each environment has its own Terraform folder

`deploy/terraform/environments/` has one folder for each of dev, staging and prod. Each folder is a Terraform root with its own state, backend and provider configuration. It calls the shared `service` module with the values of its environment and takes the image tag as a variable.

## Consequences

### Naming

- Any assembly, namespace or Kubernetes resource shows which project and service it belongs to.
- Renaming the project or the service means renaming every .NET project, the namespaces, the chart and the Kubernetes resources.

### Contracts, Models and Entities

- The external API, the business types and the database tables can change separately. A change to a table does not change the API unless the mapping is changed too.
- Every feature needs mapping code in the Api and in Infrastructure, even when the three shapes are identical.
- The compiler stops Domain and Infrastructure from using Contracts, because they do not reference it.
- The compiler does not stop the Api from using Entities, because the Api reaches them through its reference to Infrastructure. Reviewers enforce this rule.

### Terraform deploys the Helm chart

- One `terraform apply` creates the namespace and deploys the release, and the Terraform plan in a pull request shows changes to both.
- The deployed image tag is recorded in the Terraform state.
- A change made with `helm` or `kubectl` by hand is not recorded in the Terraform state. See [rollback.md](../runbooks/rollback.md).
- The chart version must be bumped when the chart changes. See [deploy.md](../runbooks/deploy.md#change-the-chart-or-the-terraform-code).
- The pipeline needs a remote Terraform backend, cloud credentials and cluster access for each environment before it can deploy. These are not configured yet.

### One Terraform folder per environment

- An apply in one environment cannot change another environment, because the state is separate.
- A change reaches staging and prod only when it is applied there. The CD workflow applies the folders in the order dev, staging, prod.
- `versions.tf`, `providers.tf`, `variables.tf` and `outputs.tf` exist three times and have to be kept the same by hand. Everything that can be shared belongs in the `service` module.
