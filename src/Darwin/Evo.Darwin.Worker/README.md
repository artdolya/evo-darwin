# Evo.Darwin.Worker

The worker of Darwin: a .NET console application built on the generic host. It sits behind the message bus (RabbitMQ) and processes the requests that [`Evo.Darwin.Api`](../Evo.Darwin.Api/README.md) sends. It has no HTTP endpoint.

## What belongs here

- The consumers that receive messages from RabbitMQ and call the services of `Evo.Darwin.Domain`.
- `Program.cs` and configuration (`appsettings.json`).
- The client of the message bus (RabbitMQ).

The Worker is the only Darwin project with access to the database (PostgreSQL), to blob storage and to an LLM. It reaches them through `Evo.Darwin.Infrastructure`. Business logic belongs in `Evo.Darwin.Domain`. Repositories and providers belong in `Evo.Darwin.Infrastructure`.

Several Workers can run at the same time. The number of Workers follows the load.

Today the project registers no consumer. It starts and waits until it is stopped.

TODO: choose the RabbitMQ client library, and register the first consumer in `Program.cs`.

## References

`Evo.Darwin.Models`, `Evo.Darwin.Domain`, `Evo.Darwin.Infrastructure`.

## Run locally

Run every command from the repository root.

```bash
dotnet run --project src/Darwin/Evo.Darwin.Worker
```

The Worker runs in the `Development` environment. The value comes from `Properties/launchSettings.json`. The log shows that it is up:

```text
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
```

Stop it with Ctrl+C. The Worker needs no RabbitMQ, database or other running dependency today.

The Worker is not deployed. See the [architecture overview](../../../docs/architecture/overview.md#deployment).

The [local stack](../../Docker/README.md) builds an image of the Worker from the `Dockerfile` in this folder, and runs it in a container with PostgreSQL, Redis and RabbitMQ.

## Tests

No tests cover this project today: it has no code apart from the start-up.

TODO: when the first consumer is added, describe here which tests cover it and what they need to run.

## Environment variables

None is required. The project reads these optional variables:

| Name | Value in a local run | Effect |
| --- | --- | --- |
| `DOTNET_ENVIRONMENT` | `Development`, from the launch profile | Name of the environment. Without a value the Worker runs as `Production`. |
| `Logging__LogLevel__Default` | `Information`, from `appsettings.json` | Lowest log level that is written. |
| `Logging__LogLevel__Microsoft.Hosting.Lifetime` | `Information`, from `appsettings.json` | Lowest log level written for the start and stop messages of the host. |

When you add a variable, add it to [docs/configuration.md](../../../docs/configuration.md) and to the table above in the same pull request.

TODO: when the RabbitMQ client, the database access and the first provider are added, list their settings here (for example the connection strings).
