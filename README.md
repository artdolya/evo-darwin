# Evo

The repository of the Evo project. It holds the services of Evo, built with .NET 10:

| Service | What it is | Components |
| --- | --- | --- |
| Darwin | TODO: describe in two or three sentences what Darwin does and who uses it. | UI, API, Worker, Migrations |
| Galaxy | The administration of Evo. | UI, API, Worker, Migrations |
| Home | The home site of Evo: a few static pages. | Site |

The repository is a skeleton today: each API has a health endpoint and no business features, each Worker starts and waits, and no migration exists. The UIs are not built yet. The home site has one static page. What each component does and what it may reach is in [docs/architecture/overview.md](docs/architecture/overview.md).

- **Project:** Evo
- **Services:** Darwin, Galaxy, Home
- **Owning team:** not recorded yet

TODO: name the owning team and how to reach it, and set the team in [.github/CODEOWNERS](.github/CODEOWNERS).

## Prerequisites

- [.NET SDK](https://dotnet.microsoft.com/download) 10.0.115 or a later 10.0 version. `global.json` selects it. Check with `dotnet --version`.
- A checkout of [Krapka](https://github.com/artdolya/krapka) in the folder next to this repository, named `krapka`. See [Krapka](#krapka).
- Docker, only if you run the [complete stack](#run-the-complete-stack), build or run the container image, or run the [local database](#local-database).
- Terraform 1.15 and Helm, only if you change files in `deploy/`.
- Make, only if you use the shortcut commands of the `Makefile`: `make up` and `make down` for the [complete stack](#run-the-complete-stack), and `make format`. `make format` formats the C# code and the Terraform code, so it needs Terraform too.

The APIs and the Workers need no database or other running dependency today. Only the Migrations programs need the [local database](#local-database).

### Krapka

The Krapka libraries are built from source. `src/Krapka` is a symbolic link to `../../krapka`, so the Krapka repository has to be cloned next to this one. From the repository root:

```bash
git clone https://github.com/artdolya/krapka.git ../krapka
```

Check that the link resolves. The command lists the folders of the Krapka libraries, such as `Data` and `EntityFramework`:

```bash
ls src/Krapka/src/Net
```

Without the checkout, `dotnet build` fails because it cannot find the Krapka project files. The reasons for this setup are in [ADR 0004](docs/adr/0004-krapka-as-source.md).

## Build

Run every command from the repository root.

```bash
dotnet build
```

The first build also builds the Krapka libraries for every target framework they declare, so it takes longer than the next ones.

## Run

Start the API of Darwin:

```bash
dotnet run --project src/Darwin/Evo.Darwin.Api
```

The API listens on <http://localhost:5080> and runs in the `Development` environment. Check that it is up:

```bash
curl http://localhost:5080/health
```

The response is `Healthy`. The OpenAPI document is at <http://localhost:5080/openapi/v1.json>.

Six projects run. Each has the command and the expected result in its README:

| Project | What it is | Local address |
| --- | --- | --- |
| [Evo.Darwin.Api](src/Darwin/Evo.Darwin.Api/README.md) | The HTTP API of Darwin. | <http://localhost:5080> |
| [Evo.Darwin.Worker](src/Darwin/Evo.Darwin.Worker/README.md) | The worker of Darwin. | None |
| [Evo.Darwin.Migrations](src/Darwin/Evo.Darwin.Migrations/README.md) | Applies the migrations of the Darwin database, then exits. | None |
| [Evo.Galaxy.Api](src/Galaxy/Evo.Galaxy.Api/README.md) | The HTTP API of Galaxy. | <http://localhost:5081> |
| [Evo.Galaxy.Worker](src/Galaxy/Evo.Galaxy.Worker/README.md) | The worker of Galaxy. | None |
| [Evo.Galaxy.Migrations](src/Galaxy/Evo.Galaxy.Migrations/README.md) | Applies the migrations of the Galaxy database, then exits. | None |

## Run the complete stack

One Docker Compose project starts the APIs, the Workers and the home site, and PostgreSQL, Redis and RabbitMQ with them. Every variable and secret has a default value, so it needs no setup:

```bash
make up
```

The command builds the images and starts the stack in the background. The first start takes some minutes. The API of Darwin then listens on <http://localhost:5180>, and the API of Galaxy on <http://localhost:5181>. Check one:

```bash
curl http://localhost:5180/health
```

The response is `Healthy`. Stop the stack:

```bash
make down
```

Without Make, run the commands of the two targets yourself: `docker compose --project-directory src/Docker up --build --detach` and `docker compose --project-directory src/Docker down`.

In Visual Studio, the same stack is the project `docker-compose` with the launch profile `Docker Compose`. It starts the APIs and the Workers with the debugger.

The stack does not run the Migrations programs. Run them from the command line against the PostgreSQL of the stack, which listens on port 5532: see [Apply the migrations](src/Docker/README.md#apply-the-migrations).

The other addresses, the start from Visual Studio, and the file for the values of your own machine are in [src/Docker/README.md](src/Docker/README.md).

## Local database

The complete stack has its own PostgreSQL, on port 5532. This section is for a run of a Migrations program without the stack.

The Migrations programs need a PostgreSQL server. Start one in Docker. It listens on port 5432, and its data is deleted when the container stops:

```bash
docker run --rm -d --name evo-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres:18
```

Create the database of Darwin and the database of Galaxy:

```bash
docker exec evo-postgres createdb -U postgres darwin
```

```bash
docker exec evo-postgres createdb -U postgres galaxy
```

The connection string of the Darwin database is then `Host=localhost;Database=darwin;Username=postgres;Password=postgres`. For Galaxy, replace `darwin` with `galaxy`. How to apply the migrations is in the README of [Evo.Darwin.Migrations](src/Darwin/Evo.Darwin.Migrations/README.md#run-locally) and of [Evo.Galaxy.Migrations](src/Galaxy/Evo.Galaxy.Migrations/README.md#run-locally).

Stop the server:

```bash
docker stop evo-postgres
```

## Test

```bash
dotnet test
```

This runs the unit tests and the integration tests of Darwin and of Galaxy. The integration tests start the API in memory, so nothing else has to be running.

## Run in a container

Only `Evo.Darwin.Api` has a container image that is deployed. The images of the other components are built only for the [complete stack](#run-the-complete-stack).

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
| `src/` | The services: one folder for each service (`Darwin`, `Galaxy`, `Home`), and in it one folder for each project, named `Evo.<Service>.<Component>`. Each project and what it may reference: [docs/architecture/overview.md](docs/architecture/overview.md). |
| `src/Krapka` | A symbolic link to the Krapka checkout next to this repository. See [Krapka](#krapka). |
| `src/Docker/` | The Docker Compose project of the [complete stack](#run-the-complete-stack) for local development. See [src/Docker/README.md](src/Docker/README.md). |
| `tests/` | The unit tests and the integration tests, in one folder for each service: `Darwin` and `Galaxy`. |
| `Evo.sln` | The solution. Its folders are the same as on disk: `src/Darwin`, `src/Galaxy`, `tests/Darwin`, `tests/Galaxy`, and `Krapka` for the Krapka projects. The project `docker-compose` of `src/Docker/` is in the folder `src`. |
| `deploy/docker/` | Dockerfile of the container image of `Evo.Darwin.Api` that is deployed. |
| `deploy/helm/evo-darwin/` | Helm chart of `Evo.Darwin.Api`. |
| `deploy/terraform/` | Terraform that installs the chart: one shared module and one folder per environment. |
| `docs/` | Documentation. |
| `scripts/` | Helper scripts. `tags.sh` computes the version tags for the workflows. |
| `.github/` | Workflows (CI, Terraform plan, tag, release, cleanup), code owners, pull request template. |
| `Makefile` | Shortcut commands. `make up` starts the [complete stack](#run-the-complete-stack) and `make down` stops it. `make format` formats the C# code and the Terraform code. |
| `dotnet-tools.json` | The .NET tools of the repository: `dotnet ef`, which creates migrations. `dotnet tool restore` installs them. |
| `.editorconfig` | Formatting and code style rules, read by editors and by `dotnet format`. |

Every project in `src/` and `tests/` has a `README.md` in its folder: what the project is for, how to run it or its tests, and which environment variables it needs. The projects that run are listed in [Run](#run).

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before you open a pull request. It describes the workflow, where code and tests belong, and which docs to update with a change.

## Documentation

Start at [docs/README.md](docs/README.md).
