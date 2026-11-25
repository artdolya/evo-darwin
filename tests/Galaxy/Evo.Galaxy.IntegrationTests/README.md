# Evo.Galaxy.IntegrationTests

The integration tests of Galaxy, written with xUnit. Each test starts `Evo.Galaxy.Api` in memory with `WebApplicationFactory` and calls it over HTTP.

## What belongs here

- Tests that call an endpoint of the API and check the response.

A test of a single class belongs in `Evo.Galaxy.UnitTests`.

Today the project has one test, `HealthEndpointTests`. It calls `GET /health` and expects status 200.

## References

`Evo.Galaxy.Api`.

## Run the tests

Run every command from the repository root.

```bash
dotnet test tests/Galaxy/Evo.Galaxy.IntegrationTests
```

To run the tests of one class, filter by its name:

```bash
dotnet test tests/Galaxy/Evo.Galaxy.IntegrationTests --filter "FullyQualifiedName~HealthEndpointTests"
```

The tests start the API themselves. Do not start the service first. They open no network port and need no database or other running dependency.

`dotnet test` without a path runs these tests and the unit tests.

## Environment variables

None is required.

| Name | Default in the tests | Effect |
| --- | --- | --- |
| `ASPNETCORE_ENVIRONMENT` | `Development` | Environment in which the tests start the API. A value set in the shell replaces the default. |

The API under test reads the same variables as in a normal run. They are listed in the [Api README](../../../src/Galaxy/Evo.Galaxy.Api/README.md#environment-variables).
