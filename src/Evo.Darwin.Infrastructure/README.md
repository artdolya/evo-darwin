# Evo.Darwin.Infrastructure

The code of the Darwin service that talks to the outside: the database and external services.

## What belongs here

- Database access: the `DbContext` and the migrations.
- Clients of external services.
- Mapping between Entities types and Models types.

Business rules belong in `Evo.Darwin.Domain`. Classes that describe database tables belong in `Evo.Darwin.Entities`. Contracts types never reach this project.

The project has no classes today.

## References

`Evo.Darwin.Domain`, `Evo.Darwin.Models`, `Evo.Darwin.Entities`.

Only `Evo.Darwin.Api` references it.

## Run locally

This is a class library. It cannot be run on its own. `Evo.Darwin.Api` loads it: see [its README](../Evo.Darwin.Api/README.md#run-locally).

To build only this project, from the repository root:

```bash
dotnet build src/Evo.Darwin.Infrastructure
```

TODO: when the database is chosen, describe here how to start a local database and how to create and apply migrations.

## Tests

No tests cover this project today: it has no code.

TODO: when database access is added, describe here which tests cover it and what they need to run.

## Environment variables

None today.

TODO: when the database and the first external client are added, list their settings here (for example the connection string) and in [docs/configuration.md](../../docs/configuration.md).
