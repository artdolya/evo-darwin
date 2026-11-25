# Evo.Galaxy.Models

The types used on the message bus (RabbitMQ) and in the business layer of Galaxy. They are the shape in which Galaxy handles its data internally.

## What belongs here

- The types that `Evo.Galaxy.Domain` works with.
- The types of the messages that `Evo.Galaxy.Api` and `Evo.Galaxy.Worker` exchange on the message bus.

Request and response types of the HTTP API belong in `Evo.Galaxy.Contracts`. Classes that describe database tables belong in `Evo.Galaxy.Entities`.

The project has no types today.

## References

None. This project references no other project.

`Evo.Galaxy.Api`, `Evo.Galaxy.Worker`, `Evo.Galaxy.Domain` and `Evo.Galaxy.Infrastructure` reference it.

## Run locally

This is a class library. It cannot be run on its own. `Evo.Galaxy.Api` and `Evo.Galaxy.Worker` load it: see the [Api README](../Evo.Galaxy.Api/README.md#run-locally) and the [Worker README](../Evo.Galaxy.Worker/README.md#run-locally).

To build only this project, from the repository root:

```bash
dotnet build src/Galaxy/Evo.Galaxy.Models
```

## Tests

The project has no tests of its own. Its types are tested together with the business logic that uses them, in `Evo.Galaxy.UnitTests`:

```bash
dotnet test tests/Galaxy/Evo.Galaxy.UnitTests
```

## Environment variables

None. The project reads no configuration.
