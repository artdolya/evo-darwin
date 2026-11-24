# Evo.Darwin.Domain

The business logic of the Darwin service.

## What belongs here

- The services that implement the business rules.

Domain works with Models only. It does not know the HTTP API (Contracts) or the database tables (Entities). HTTP endpoints belong in `Evo.Darwin.Api`, and database access and external clients belong in `Evo.Darwin.Infrastructure`.

The project has no classes today.

## References

`Evo.Darwin.Models`.

`Evo.Darwin.Api`, `Evo.Darwin.Infrastructure` and `Evo.Darwin.UnitTests` reference it.

## Run locally

This is a class library. It cannot be run on its own. `Evo.Darwin.Api` loads it: see [its README](../Evo.Darwin.Api/README.md#run-locally).

To build only this project, from the repository root:

```bash
dotnet build src/Evo.Darwin.Domain
```

## Tests

`Evo.Darwin.UnitTests` tests this project:

```bash
dotnet test tests/Evo.Darwin.UnitTests
```

## Environment variables

None. The project reads no configuration. Configuration belongs to the host, `Evo.Darwin.Api`.
