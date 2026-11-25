# Evo.Darwin.Api

The HTTP API of Darwin: an ASP.NET Core web application. It is one of the three Darwin projects that run. The other two are [`Evo.Darwin.Worker`](../Evo.Darwin.Worker/README.md) and [`Evo.Darwin.Migrations`](../Evo.Darwin.Migrations/README.md).

## What belongs here

- HTTP endpoints.
- `Program.cs` and configuration (`appsettings.json`).
- Mapping between Contracts types and Models types.
- The clients of the cache (Redis) and of the message bus (RabbitMQ).

Business logic belongs in `Evo.Darwin.Domain`. The Api calls the services of Domain and works with Models.

The Api has no access to the database, to blob storage or to an LLM. It references neither `Evo.Darwin.Infrastructure` nor `Evo.Darwin.Data`, so the compiler stops it from using them. Work that needs one of them is sent over RabbitMQ to [`Evo.Darwin.Worker`](../Evo.Darwin.Worker/README.md).

Today the project has two endpoints and no business features. No Redis client and no RabbitMQ client is registered.

TODO: choose the client libraries for Redis and RabbitMQ, and register them in `Program.cs`.

| Endpoint | Purpose |
| --- | --- |
| `GET /health` | Returns `Healthy`. Used by the Kubernetes probes. |
| `GET /openapi/v1.json` | The OpenAPI document. Served only in the `Development` environment. See [docs/api/README.md](../../../docs/api/README.md). |

## References

`Evo.Darwin.Contracts`, `Evo.Darwin.Models`, `Evo.Darwin.Domain`.

## Run locally

Run every command from the repository root.

```bash
dotnet run --project src/Darwin/Evo.Darwin.Api
```

The service listens on <http://localhost:5080> and runs in the `Development` environment. Both values come from `Properties/launchSettings.json`. Check that it is up:

```bash
curl http://localhost:5080/health
```

The Api needs no Redis, RabbitMQ or other running dependency today.

To listen on another port, add `--urls`:

```bash
dotnet run --project src/Darwin/Evo.Darwin.Api --urls http://localhost:5090
```

To run it in a container, see the [repository README](../../../README.md#run-in-a-container). That image is the one that is deployed. It is built from `deploy/docker/Dockerfile`.

The [local stack](../../Docker/README.md) builds its own image of the Api from the `Dockerfile` in this folder, and runs it in a container. The Api then listens on <http://localhost:5180>.

## Tests

`Evo.Darwin.IntegrationTests` tests this project over HTTP:

```bash
dotnet test tests/Darwin/Evo.Darwin.IntegrationTests
```

## Environment variables

None is required. The project reads these optional variables:

| Name | Value in a local run | Effect |
| --- | --- | --- |
| `ASPNETCORE_ENVIRONMENT` | `Development`, from the launch profile | Name of the environment. `Development` serves the OpenAPI document and shows detailed error pages. Without a value the service runs as `Production`. |
| `ASPNETCORE_URLS` | `http://localhost:5080`, from the launch profile | Address the service listens on. |
| `ASPNETCORE_HTTP_PORTS` | Not set | Port the service listens on in the container. The .NET base image sets it to `8080`. |
| `Logging__LogLevel__Default` | `Information`, from `appsettings.json` | Lowest log level that is written. |
| `Logging__LogLevel__Microsoft.AspNetCore` | `Warning`, from `appsettings.json` | Lowest log level written for ASP.NET Core's own messages. |
| `AllowedHosts` | `*`, from `appsettings.json` | Host names the service accepts in the `Host` header. |

`dotnet run` applies the launch profile after the shell, so a value of `ASPNETCORE_ENVIRONMENT` set in the shell is ignored. To use the shell value, run without the profile:

```bash
ASPNETCORE_ENVIRONMENT=Production dotnet run --project src/Darwin/Evo.Darwin.Api --no-launch-profile
```

Without the profile the service listens on <http://localhost:5000>.

The values in each deployed environment, and where they come from, are in [docs/configuration.md](../../../docs/configuration.md). When you add a variable, add it to that file and to the table above in the same pull request.
