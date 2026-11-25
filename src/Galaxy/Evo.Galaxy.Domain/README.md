# Evo.Galaxy.Domain

The business logic of Galaxy, the administration of Evo.

## What belongs here

- The services that implement the business rules.

Domain works with Models only. It does not know the HTTP API (Contracts) or the database tables (Entities). Both hosts call its services: `Evo.Galaxy.Api` and `Evo.Galaxy.Worker`.

Domain references no client library. A service that needs the cache, the message bus, the database or a provider declares an interface for it. The implementation belongs in the host or in `Evo.Galaxy.Infrastructure`.

HTTP endpoints belong in `Evo.Galaxy.Api`, message consumers in `Evo.Galaxy.Worker`, and repositories and providers in `Evo.Galaxy.Infrastructure`.

The project has no classes today.

## References

`Evo.Galaxy.Models`.

`Evo.Galaxy.Api`, `Evo.Galaxy.Worker`, `Evo.Galaxy.Infrastructure` and `Evo.Galaxy.UnitTests` reference it.

## Run locally

This is a class library. It cannot be run on its own. `Evo.Galaxy.Api` and `Evo.Galaxy.Worker` load it: see the [Api README](../Evo.Galaxy.Api/README.md#run-locally) and the [Worker README](../Evo.Galaxy.Worker/README.md#run-locally).

To build only this project, from the repository root:

```bash
dotnet build src/Galaxy/Evo.Galaxy.Domain
```

## Tests

`Evo.Galaxy.UnitTests` tests this project:

```bash
dotnet test tests/Galaxy/Evo.Galaxy.UnitTests
```

## Environment variables

None. The project reads no configuration. Configuration belongs to the hosts, `Evo.Galaxy.Api` and `Evo.Galaxy.Worker`.
