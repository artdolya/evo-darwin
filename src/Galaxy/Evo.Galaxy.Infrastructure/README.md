# Evo.Galaxy.Infrastructure

The code of Galaxy that talks to the database and to external systems. Only `Evo.Galaxy.Worker` loads it.

## What belongs here

- Repositories: the classes that read and write the database through `GalaxyDbContext`.
- Mapping between Entities types and Models types.
- Providers: the clients of external systems.

Business rules belong in `Evo.Galaxy.Domain`. The context belongs in `Evo.Galaxy.Data`, the classes that describe the tables in `Evo.Galaxy.Entities`, and the migrations in `Evo.Galaxy.Migrations`. Contracts types never reach this project.

The project has no classes today.

TODO: name the external systems that Galaxy uses. None is chosen yet.

## References

`Evo.Galaxy.Domain`, `Evo.Galaxy.Models`, `Evo.Galaxy.Entities`, `Evo.Galaxy.Data`.

Only `Evo.Galaxy.Worker` references it. `Evo.Galaxy.Api` does not: the Api has no access to the database or to a provider.

## Run locally

This is a class library. It cannot be run on its own. `Evo.Galaxy.Worker` loads it: see [its README](../Evo.Galaxy.Worker/README.md#run-locally).

To build only this project, from the repository root:

```bash
dotnet build src/Galaxy/Evo.Galaxy.Infrastructure
```

## Tests

No tests cover this project today: it has no code.

TODO: when the first repository or provider is added, describe here which tests cover it and what they need to run.

## Environment variables

None today.

TODO: when the database access and the first provider are added, list their settings here (for example the connection string) and in [docs/configuration.md](../../../docs/configuration.md).
