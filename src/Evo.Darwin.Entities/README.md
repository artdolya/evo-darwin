# Evo.Darwin.Entities

The classes that describe the database tables of the Darwin service.

## What belongs here

- The classes that describe the database tables.

Nothing else belongs here: no database access, no logic. The `DbContext` and the migrations belong in `Evo.Darwin.Infrastructure`.

The project has no classes today.

TODO: name the database engine. It is not chosen yet.

## References

None. This project references no other project.

Only `Evo.Darwin.Infrastructure` references it, and maps Entities to Models. The Api never returns Entities.

## Run locally

This is a class library. It cannot be run on its own. `Evo.Darwin.Api` loads it through `Evo.Darwin.Infrastructure`: see [the Api README](../Evo.Darwin.Api/README.md#run-locally).

To build only this project, from the repository root:

```bash
dotnet build src/Evo.Darwin.Entities
```

## Tests

The project has no tests: it holds no logic.

## Environment variables

None. The project reads no configuration.
