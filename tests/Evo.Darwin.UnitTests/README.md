# Evo.Darwin.UnitTests

The unit tests of the Darwin service, written with xUnit.

## What belongs here

- Tests of one class or a few classes at a time, mainly the business logic in `Evo.Darwin.Domain`.

A unit test does not start the API and needs no database, network or other running dependency. A test that calls the API over HTTP belongs in `Evo.Darwin.IntegrationTests`.

Today the project has one test, `SampleTests`. It proves that the project builds and runs. Replace it with the first real test.

## References

`Evo.Darwin.Domain`. To test another project, add a reference to it.

## Run the tests

Run every command from the repository root.

```bash
dotnet test tests/Evo.Darwin.UnitTests
```

To run the tests of one class, filter by its name:

```bash
dotnet test tests/Evo.Darwin.UnitTests --filter "FullyQualifiedName~SampleTests"
```

`dotnet test` without a path runs these tests and the integration tests.

## Environment variables

None. The tests read no configuration.
