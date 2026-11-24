# Evo.Darwin.IntegrationTests

The integration tests of the Darwin service, written with xUnit. Each test starts `Evo.Darwin.Api` in memory with `WebApplicationFactory` and calls it over HTTP.

## What belongs here

- Tests that call an endpoint of the API and check the response.

A test of a single class belongs in `Evo.Darwin.UnitTests`.

Today the project has one test, `HealthEndpointTests`. It calls `GET /health` and expects status 200.

## References

`Evo.Darwin.Api`.

## Run the tests

Run every command from the repository root.

```bash
dotnet test tests/Evo.Darwin.IntegrationTests
```

To run the tests of one class, filter by its name:

```bash
dotnet test tests/Evo.Darwin.IntegrationTests --filter "FullyQualifiedName~HealthEndpointTests"
```

The tests start the API themselves. Do not start the service first. They open no network port and need no database or other running dependency.

`dotnet test` without a path runs these tests and the unit tests.

## Environment variables

None is required.

| Name | Default in the tests | Effect |
| --- | --- | --- |
| `ASPNETCORE_ENVIRONMENT` | `Development` | Environment in which the tests start the API. A value set in the shell replaces the default. |

The API under test reads the same variables as in a normal run. They are listed in the [Api README](../../src/Evo.Darwin.Api/README.md#environment-variables).
