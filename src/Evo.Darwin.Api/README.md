# Evo.Darwin.Api

The host of the Darwin service: an ASP.NET Core web application. It is the only project in `src/` that runs. The other projects are libraries that it loads.

## What belongs here

- HTTP endpoints.
- `Program.cs` and configuration (`appsettings.json`).
- Mapping between Contracts types and Models types.

Business logic belongs in `Evo.Darwin.Domain`, and database access in `Evo.Darwin.Infrastructure`. The Api never returns Entities.

Today the project has two endpoints and no business features:

| Endpoint | Purpose |
| --- | --- |
| `GET /health` | Returns `Healthy`. Used by the Kubernetes probes. |
| `GET /openapi/v1.json` | The OpenAPI document. Served only in the `Development` environment. See [docs/api/README.md](../../docs/api/README.md). |

## References

`Evo.Darwin.Contracts`, `Evo.Darwin.Models`, `Evo.Darwin.Domain`, `Evo.Darwin.Infrastructure`.

## Run locally

Run every command from the repository root.

```bash
dotnet run --project src/Evo.Darwin.Api
```

The service listens on <http://localhost:5080> and runs in the `Development` environment. Both values come from `Properties/launchSettings.json`. Check that it is up:

```bash
curl http://localhost:5080/health
```

The service needs no database or other running dependency.

To listen on another port, add `--urls`:

```bash
dotnet run --project src/Evo.Darwin.Api --urls http://localhost:5090
```

To run it in a container, see the [repository README](../../README.md#run-in-a-container).

## Tests

`Evo.Darwin.IntegrationTests` tests this project over HTTP:

```bash
dotnet test tests/Evo.Darwin.IntegrationTests
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
ASPNETCORE_ENVIRONMENT=Production dotnet run --project src/Evo.Darwin.Api --no-launch-profile
```

Without the profile the service listens on <http://localhost:5000>.

The values in each deployed environment, and where they come from, are in [docs/configuration.md](../../docs/configuration.md). When you add a variable, add it to that file and to the table above in the same pull request.
