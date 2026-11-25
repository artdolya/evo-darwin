# Evo.Darwin.Infrastructure

The code of Darwin that talks to the database and to external systems. Only `Evo.Darwin.Worker` loads it.

## What belongs here

- Repositories: the classes that read and write the database through `DarwinDbContext`.
- Mapping between Entities types and Models types.
- Providers: the clients of blob storage, of an LLM and of other external systems.

Business rules belong in `Evo.Darwin.Domain`. The context belongs in `Evo.Darwin.Data`, the classes that describe the tables in `Evo.Darwin.Entities`, and the migrations in `Evo.Darwin.Migrations`. Contracts types never reach this project.

The project has no classes today.

TODO: name the blob storage and the LLM providers. They are not chosen yet.

## References

`Evo.Darwin.Domain`, `Evo.Darwin.Models`, `Evo.Darwin.Entities`, `Evo.Darwin.Data`.

Only `Evo.Darwin.Worker` references it. `Evo.Darwin.Api` does not: the Api has no access to the database or to a provider.

## Run locally

This is a class library. It cannot be run on its own. `Evo.Darwin.Worker` loads it: see [its README](../Evo.Darwin.Worker/README.md#run-locally).

To build only this project, from the repository root:

```bash
dotnet build src/Darwin/Evo.Darwin.Infrastructure
```

## Tests

No tests cover this project today: it has no code.

TODO: when the first repository or provider is added, describe here which tests cover it and what they need to run.

## Environment variables

None today.

TODO: when the database access and the first provider are added, list their settings here (for example the connection string) and in [docs/configuration.md](../../../docs/configuration.md).
