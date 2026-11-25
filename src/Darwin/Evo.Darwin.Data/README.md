# Evo.Darwin.Data

The EF Core context of the Darwin database (PostgreSQL).

## What belongs here

- `DarwinDbContext`.
- The mapping of each entity to its table: one `IEntityTypeConfiguration<T>` class for each entity. The context picks up every such class in this project.

Nothing else belongs here. The classes that describe the tables belong in `Evo.Darwin.Entities`. The migration classes belong in `Evo.Darwin.Migrations`. Repositories, and the mapping between Entities and Models, belong in `Evo.Darwin.Infrastructure`.

`DarwinDbContext` derives from `ApplicationDbContext` of `KrapkaNet.EntityFramework.Abstractions`.

Today the context has no tables.

## References

`Evo.Darwin.Entities`, and `KrapkaNet.EntityFramework.Abstractions` from [Krapka](../../../docs/architecture/overview.md#krapka).

`Evo.Darwin.Infrastructure` and `Evo.Darwin.Migrations` reference it. `Evo.Darwin.Api` does not: the Api has no access to the database.

## Run locally

This is a class library. It cannot be run on its own. `Evo.Darwin.Migrations` and `Evo.Darwin.Worker` load it: see the [Migrations README](../Evo.Darwin.Migrations/README.md#run-locally) and the [Worker README](../Evo.Darwin.Worker/README.md#run-locally).

To build only this project, from the repository root:

```bash
dotnet build src/Darwin/Evo.Darwin.Data
```

## Tests

No tests cover this project today.

TODO: when the first table is added, describe here which tests cover the context and what they need to run.

## Environment variables

None. The project reads no configuration. The host that creates the context supplies the connection string.
