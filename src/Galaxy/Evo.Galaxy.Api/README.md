# Evo.Galaxy.Api

The HTTP API of Galaxy, the administration of Evo: an ASP.NET Core web application. It is one of the three Galaxy projects that run. The other two are [`Evo.Galaxy.Worker`](../Evo.Galaxy.Worker/README.md) and [`Evo.Galaxy.Migrations`](../Evo.Galaxy.Migrations/README.md).

## What belongs here

- HTTP endpoints.
- `Program.cs` and configuration (`appsettings.json`).
- Mapping between Contracts types and Models types.
- The clients of the cache (Redis) and of the message bus (RabbitMQ).

Business logic belongs in `Evo.Galaxy.Domain`. The Api calls the services of Domain and works with Models.

The Api has no access to the database or to a provider. It references neither `Evo.Galaxy.Infrastructure` nor `Evo.Galaxy.Data`, so the compiler stops it from using them. Work that needs one of them is sent over RabbitMQ to [`Evo.Galaxy.Worker`](../Evo.Galaxy.Worker/README.md).

Today the project has two endpoints and no business features. No Redis client and no RabbitMQ client is registered.

TODO: choose the client libraries for Redis and RabbitMQ, and register them in `Program.cs`.

| Endpoint | Purpose |
| --- | --- |
| `GET /health` | Returns `Healthy`. |
| `GET /openapi/v1.json` | The OpenAPI document. Served only in the `Development` environment. See [docs/api/README.md](../../../docs/api/README.md). |

## References

`Evo.Galaxy.Contracts`, `Evo.Galaxy.Models`, `Evo.Galaxy.Domain`.

## Run locally

Run every command from the repository root.

```bash
dotnet run --project src/Galaxy/Evo.Galaxy.Api
```

The service listens on <http://localhost:5081> and runs in the `Development` environment. Both values come from `Properties/launchSettings.json`. Check that it is up:

```bash
curl http://localhost:5081/health
```

The Api needs no Redis, RabbitMQ or other running dependency today.

To listen on another port, add `--urls`:

```bash
dotnet run --project src/Galaxy/Evo.Galaxy.Api --urls http://localhost:5091
```

`Evo.Galaxy.Api` is not built into a container image and is not deployed. See the [architecture overview](../../../docs/architecture/overview.md#deployment).

## Tests

`Evo.Galaxy.IntegrationTests` tests this project over HTTP:

```bash
dotnet test tests/Galaxy/Evo.Galaxy.IntegrationTests
```

## Environment variables

None is required. The project reads these optional variables:

| Name | Value in a local run | Effect |
| --- | --- | --- |
| `ASPNETCORE_ENVIRONMENT` | `Development`, from the launch profile | Name of the environment. `Development` serves the OpenAPI document and shows detailed error pages. Without a value the service runs as `Production`. |
| `ASPNETCORE_URLS` | `http://localhost:5081`, from the launch profile | Address the service listens on. |
| `Logging__LogLevel__Default` | `Information`, from `appsettings.json` | Lowest log level that is written. |
| `Logging__LogLevel__Microsoft.AspNetCore` | `Warning`, from `appsettings.json` | Lowest log level written for ASP.NET Core's own messages. |
| `AllowedHosts` | `*`, from `appsettings.json` | Host names the service accepts in the `Host` header. |

`dotnet run` applies the launch profile after the shell, so a value of `ASPNETCORE_ENVIRONMENT` set in the shell is ignored. To use the shell value, run without the profile:

```bash
ASPNETCORE_ENVIRONMENT=Production dotnet run --project src/Galaxy/Evo.Galaxy.Api --no-launch-profile
```

Without the profile the service listens on <http://localhost:5000>.

The variables are also listed in [docs/configuration.md](../../../docs/configuration.md#other-components). When you add a variable, add it to that file and to the table above in the same pull request.
