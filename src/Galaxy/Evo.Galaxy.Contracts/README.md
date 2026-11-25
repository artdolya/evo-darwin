# Evo.Galaxy.Contracts

The request and response types of the external HTTP API of Galaxy. They are what a caller of the API sees, and they appear in the OpenAPI document.

## What belongs here

- The type of every request body and response body of an API endpoint.

Nothing else belongs here: no logic, no message bus types, no database classes. A change to a type in this project changes the external API.

The project has no types today.

## References

None. This project references no other project.

Only `Evo.Galaxy.Api` references it. Contracts types never reach `Evo.Galaxy.Domain`, `Evo.Galaxy.Worker` or `Evo.Galaxy.Infrastructure`: the Api maps them to Models first.

## Run locally

This is a class library. It cannot be run on its own. `Evo.Galaxy.Api` loads it: see [its README](../Evo.Galaxy.Api/README.md#run-locally).

To build only this project, from the repository root:

```bash
dotnet build src/Galaxy/Evo.Galaxy.Contracts
```

## Tests

The project has no tests of its own. Its types are tested through the endpoints that use them, in `Evo.Galaxy.IntegrationTests`:

```bash
dotnet test tests/Galaxy/Evo.Galaxy.IntegrationTests
```

## Environment variables

None. The project reads no configuration.
