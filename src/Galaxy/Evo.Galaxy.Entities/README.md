# Evo.Galaxy.Entities

The classes that describe the tables of the Galaxy database (PostgreSQL).

## What belongs here

- The classes that describe the database tables.

Nothing else belongs here: no database access, no logic. The context and the mapping to the tables belong in `Evo.Galaxy.Data`. The migrations belong in `Evo.Galaxy.Migrations`.

An entity derives from a base class of `KrapkaNet.Data.Abstractions`, for example `Entity`, which has an `Id` of the type `Guid`.

The project has no classes today.

## References

`KrapkaNet.Data.Abstractions` from [Krapka](../../../docs/architecture/overview.md#krapka). It references no other project of this repository.

`Evo.Galaxy.Data` and `Evo.Galaxy.Infrastructure` reference it. Infrastructure maps Entities to Models. Entities never reach `Evo.Galaxy.Api`.

## Run locally

This is a class library. It cannot be run on its own. `Evo.Galaxy.Migrations` and `Evo.Galaxy.Worker` load it: see the [Migrations README](../Evo.Galaxy.Migrations/README.md#run-locally) and the [Worker README](../Evo.Galaxy.Worker/README.md#run-locally).

To build only this project, from the repository root:

```bash
dotnet build src/Galaxy/Evo.Galaxy.Entities
```

## Tests

The project has no tests: it holds no logic.

## Environment variables

None. The project reads no configuration.
