# Evo.Darwin.Entities

The classes that describe the tables of the Darwin database (PostgreSQL).

## What belongs here

- The classes that describe the database tables.

Nothing else belongs here: no database access, no logic. The context and the mapping to the tables belong in `Evo.Darwin.Data`. The migrations belong in `Evo.Darwin.Migrations`.

An entity derives from a base class of `KrapkaNet.Data.Abstractions`, for example `Entity`, which has an `Id` of the type `Guid`.

The project has no classes today.

## References

`KrapkaNet.Data.Abstractions` from [Krapka](../../../docs/architecture/overview.md#krapka). It references no other project of this repository.

`Evo.Darwin.Data` and `Evo.Darwin.Infrastructure` reference it. Infrastructure maps Entities to Models. Entities never reach `Evo.Darwin.Api`.

## Run locally

This is a class library. It cannot be run on its own. `Evo.Darwin.Migrations` and `Evo.Darwin.Worker` load it: see the [Migrations README](../Evo.Darwin.Migrations/README.md#run-locally) and the [Worker README](../Evo.Darwin.Worker/README.md#run-locally).

To build only this project, from the repository root:

```bash
dotnet build src/Darwin/Evo.Darwin.Entities
```

## Tests

The project has no tests: it holds no logic.

## Environment variables

None. The project reads no configuration.
