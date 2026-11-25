# Evo.Darwin.Domain

The business logic of Darwin.

## What belongs here

- The services that implement the business rules.

Domain works with Models only. It does not know the HTTP API (Contracts) or the database tables (Entities). Both hosts call its services: `Evo.Darwin.Api` and `Evo.Darwin.Worker`.

Domain references no client library. A service that needs the cache, the message bus, the database or a provider declares an interface for it. The implementation belongs in the host or in `Evo.Darwin.Infrastructure`.

HTTP endpoints belong in `Evo.Darwin.Api`, message consumers in `Evo.Darwin.Worker`, and repositories and providers in `Evo.Darwin.Infrastructure`.

The project has no classes today.

## References

`Evo.Darwin.Models`.

`Evo.Darwin.Api`, `Evo.Darwin.Worker`, `Evo.Darwin.Infrastructure` and `Evo.Darwin.UnitTests` reference it.

## Run locally

This is a class library. It cannot be run on its own. `Evo.Darwin.Api` and `Evo.Darwin.Worker` load it: see the [Api README](../Evo.Darwin.Api/README.md#run-locally) and the [Worker README](../Evo.Darwin.Worker/README.md#run-locally).

To build only this project, from the repository root:

```bash
dotnet build src/Darwin/Evo.Darwin.Domain
```

## Tests

`Evo.Darwin.UnitTests` tests this project:

```bash
dotnet test tests/Darwin/Evo.Darwin.UnitTests
```

## Environment variables

None. The project reads no configuration. Configuration belongs to the hosts, `Evo.Darwin.Api` and `Evo.Darwin.Worker`.
