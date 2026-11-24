# Evo.Darwin.Models

The types used on the message bus and in the business layer of the Darwin service. They are the shape in which the service handles its data internally.

## What belongs here

- The types that `Evo.Darwin.Domain` works with.
- The types of the messages sent and received on the message bus.

Request and response types of the HTTP API belong in `Evo.Darwin.Contracts`. Classes that describe database tables belong in `Evo.Darwin.Entities`.

The project has no types today.

TODO: name the message bus. It is not chosen yet.

## References

None. This project references no other project.

`Evo.Darwin.Api`, `Evo.Darwin.Domain` and `Evo.Darwin.Infrastructure` reference it.

## Run locally

This is a class library. It cannot be run on its own. `Evo.Darwin.Api` loads it: see [its README](../Evo.Darwin.Api/README.md#run-locally).

To build only this project, from the repository root:

```bash
dotnet build src/Evo.Darwin.Models
```

## Tests

The project has no tests of its own. Its types are tested together with the business logic that uses them, in `Evo.Darwin.UnitTests`:

```bash
dotnet test tests/Evo.Darwin.UnitTests
```

## Environment variables

None. The project reads no configuration.
