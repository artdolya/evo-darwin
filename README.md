# Evo.Darwin

Darwin is a .NET 10 Web API service in the Evo project.

TODO: describe in two or three sentences what the service does and who uses it. The repository is a skeleton today: the API has a health endpoint and no business features.

- **Project:** Evo
- **Service:** Darwin
- **Owning team:** not recorded yet

TODO: name the owning team and how to reach it, and set the team in [.github/CODEOWNERS](.github/CODEOWNERS).

## Prerequisites

- [.NET SDK](https://dotnet.microsoft.com/download) 10.0.115 or a later 10.0 version. `global.json` selects it. Check with `dotnet --version`.
- Docker, only if you build or run the container image.
- Terraform 1.15 and Helm, only if you change files in `deploy/`.

The service needs no database or other running dependency.

## Build

Run every command from the repository root.

```bash
dotnet build
```

## Run

```bash
dotnet run --project src/Evo.Darwin.Api
```

The service listens on <http://localhost:5080> and runs in the `Development` environment. Check that it is up:

```bash
curl http://localhost:5080/health
```

The response is `Healthy`. The OpenAPI document is at <http://localhost:5080/openapi/v1.json>.

## Test

```bash
dotnet test
```

This runs the unit tests and the integration tests. The integration tests start the API in memory, so nothing else has to be running.

## Run in a container

```bash
docker build -f deploy/docker/Dockerfile -t evo-darwin:local .
```

```bash
docker run --rm -p 8080:8080 evo-darwin:local
```

The container listens on port 8080: `curl http://localhost:8080/health`. It runs in the `Production` environment, which does not serve the OpenAPI document. Add `-e ASPNETCORE_ENVIRONMENT=Development` to `docker run` to serve it.

## Repository layout

| Path | Content |
| --- | --- |
| `src/` | The service. Each project and what it may reference: [docs/architecture/overview.md](docs/architecture/overview.md). |
| `tests/` | [Unit tests](tests/Evo.Darwin.UnitTests/README.md) and [integration tests](tests/Evo.Darwin.IntegrationTests/README.md). |
| `deploy/docker/` | Dockerfile of the container image. |
| `deploy/helm/evo-darwin/` | Helm chart of the service. |
| `deploy/terraform/` | Terraform that installs the chart: one shared module and one folder per environment. |
| `docs/` | Documentation. |
| `scripts/` | Helper scripts. Empty today. |
| `.github/` | CI and CD workflows, code owners, pull request template. |

Every project in `src/` and `tests/` has a `README.md` in its folder: what the project is for, how to run it or its tests, and which environment variables it needs. The project that runs is [Evo.Darwin.Api](src/Evo.Darwin.Api/README.md).

## Documentation

Start at [docs/README.md](docs/README.md).
