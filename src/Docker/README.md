# Docker

The complete Evo stack for local development, as a Docker Compose project. It starts the APIs, the Workers and the home site, and the services that they use: PostgreSQL, Redis and RabbitMQ.

Visual Studio shows this folder as the project `docker-compose` in `Evo.sln`. The project has one launch profile, `Docker Compose`.

Every variable and secret has a default value in `docker-compose.yml`, so the stack starts with no setup. The defaults are for a local machine only. The values of your own machine go into `docker-compose.override.yml`, which Git ignores: see [Your own values](#your-own-values).

The Migrations programs are not in the stack. They are run from the command line: see [Apply the migrations](#apply-the-migrations).

## Files

| File | Content |
| --- | --- |
| `docker-compose.yml` | The stack: the containers, their variables and secrets with the default values, and their ports. |
| `docker-compose.override.example.yml` | Examples of the values that a developer changes. Copy it to create `docker-compose.override.yml`. |
| `docker-compose.override.yml` | The values of one developer. Git ignores it, so a new checkout does not have it. |
| `docker-compose.dcproj` | The project that Visual Studio loads. |
| `launchSettings.json` | The launch profile `Docker Compose`. It says which containers Visual Studio starts with the debugger. |
| `postgres/init-databases.sql` | Creates the empty databases `darwin` and `galaxy` when PostgreSQL creates its data volume. |

The Dockerfile of an API or of a Worker is in the folder of its project, for example `src/Darwin/Evo.Darwin.Api/Dockerfile`. Visual Studio finds the project of a container through a Dockerfile in the project folder, and can then debug it.

## What starts

| Container | What it is | Address on the host |
| --- | --- | --- |
| `evo.darwin.api` | [`Evo.Darwin.Api`](../Darwin/Evo.Darwin.Api/README.md) | <http://localhost:5180> |
| `evo.darwin.worker` | [`Evo.Darwin.Worker`](../Darwin/Evo.Darwin.Worker/README.md) | None |
| `evo.galaxy.api` | [`Evo.Galaxy.Api`](../Galaxy/Evo.Galaxy.Api/README.md) | <http://localhost:5181> |
| `evo.galaxy.worker` | [`Evo.Galaxy.Worker`](../Galaxy/Evo.Galaxy.Worker/README.md) | None |
| `evo.home.site` | nginx. It serves the files of [`Evo.Home.Site`](../Home/Evo.Home.Site/README.md) from the folder of the site. | <http://localhost:8180> |
| `postgres` | PostgreSQL 18: one server with the databases `darwin` and `galaxy`. | `localhost:5532` |
| `redis` | Redis 8. | `localhost:6479` |
| `rabbitmq` | RabbitMQ 4 with the management UI. | `localhost:5772`. The management UI is at <http://localhost:15772>. |

A host port is the usual port of the service plus 100. The stack can then run next to a project that runs with `dotnet run`, and next to a local PostgreSQL.

PostgreSQL, Redis and RabbitMQ start first. An API starts when Redis and RabbitMQ are ready. A Worker starts when PostgreSQL and RabbitMQ are ready.

The APIs and the Workers do not connect to PostgreSQL, Redis or RabbitMQ yet, so `docker-compose.yml` gives them no address and no password of these services. The variables and the default values of the stack are listed in [docs/configuration.md](../../docs/configuration.md#local-stack).

The UIs are not in the stack. They are not built yet.

## Before the first start

- Docker must be running.
- The Krapka checkout must be in the folder next to this repository: see [Krapka](../../README.md#krapka) in the repository README. The images of the Workers are built from it.

The first start downloads the images and builds the Krapka libraries, so it takes some minutes.

## Start it from Visual Studio

1. Open `Evo.sln`.
2. In Solution Explorer, right-click the project `docker-compose` and select **Set as Startup Project**.
3. Select the launch profile `Docker Compose` and start it.

The launch profile starts the two APIs and the two Workers with the debugger. In the `Debug` configuration, Visual Studio builds these four projects on the host and runs their output in the containers. The other containers start without the debugger.

## Start it from the command line

Run every command from the repository root.

```bash
make up
```

`make up` runs `docker compose --project-directory src/Docker up --build --detach`: it builds the images and starts the stack in the background. Without Make, run that command yourself.

List the containers:

```bash
docker compose --project-directory src/Docker ps
```

The command lists eight containers with the status `Up`. Check an API:

```bash
curl http://localhost:5180/health
```

The response is `Healthy`.

Stop the stack:

```bash
make down
```

`make down` runs `docker compose --project-directory src/Docker down`. The data of PostgreSQL stays in a Docker volume. To delete it too, run the command with `--volumes`:

```bash
docker compose --project-directory src/Docker down --volumes
```

Do not replace `--project-directory src/Docker` with `-f src/Docker/docker-compose.yml`. With `-f`, Docker Compose does not read `docker-compose.override.yml`.

Visual Studio and the command line use the same project name, `evo`, and so the same containers and the same data volume. Start the stack from one of them at a time.

## Apply the migrations

The stack creates the databases `darwin` and `galaxy` empty. It does not apply the migrations. Apply them from the command line, when the stack runs. The PostgreSQL of the stack listens on port 5532 of the host.

For Darwin:

```bash
ConnectionStrings__Darwin="Host=localhost;Port=5532;Database=darwin;Username=postgres;Password=postgres" dotnet run --project src/Darwin/Evo.Darwin.Migrations
```

For Galaxy:

```bash
ConnectionStrings__Galaxy="Host=localhost;Port=5532;Database=galaxy;Username=postgres;Password=postgres" dotnet run --project src/Galaxy/Evo.Galaxy.Migrations
```

Each program exits with code 0. What it logs is in the README of [Evo.Darwin.Migrations](../Darwin/Evo.Darwin.Migrations/README.md#run-locally) and of [Evo.Galaxy.Migrations](../Galaxy/Evo.Galaxy.Migrations/README.md#run-locally).

Apply the migrations again after you add a migration, and after you delete the data volume.

## Your own values

A value that is right only for your machine does not belong in `docker-compose.yml`. Create the override file once:

```bash
cp src/Docker/docker-compose.override.example.yml src/Docker/docker-compose.override.yml
```

Then change `docker-compose.override.yml`. Docker Compose and Visual Studio read it after `docker-compose.yml`, and a value in it replaces the value of the same key. Name only the keys that you change. The file holds an example for a variable, a port and a password.

Git ignores the file, so your values are not committed. Check it:

```bash
git check-ignore src/Docker/docker-compose.override.yml
```

The command prints the path of the file.

To see the values that the stack uses after the two files are merged:

```bash
docker compose --project-directory src/Docker config
```

If you change the password of PostgreSQL or its host port, use the new value in the connection string of [Apply the migrations](#apply-the-migrations).

## When you change the stack

- A new variable or secret of a component: add it to `docker-compose.yml` with a default value that works on a local machine, and to [docs/configuration.md](../../docs/configuration.md#local-stack).
- A new container: add it to `docker-compose.yml`, to `serviceActions` in `launchSettings.json`, and to the table in [What starts](#what-starts).
