# API

Each HTTP API is described by an OpenAPI document. The document is generated from the code. It is not stored in the repository.

This page describes the API of Darwin, `Evo.Darwin.Api`. The API of Galaxy, `Evo.Galaxy.Api`, works the same way: see [Galaxy](#galaxy).

## How the document is generated

The `Microsoft.AspNetCore.OpenApi` package builds the document at run time, when it is requested. Two lines in [Program.cs](../../src/Darwin/Evo.Darwin.Api/Program.cs) turn it on:

- `builder.Services.AddOpenApi()` registers the generator.
- `app.MapOpenApi()` serves the document at `/openapi/v1.json`.

The generator reads the endpoints mapped in `Evo.Darwin.Api`: the route, the HTTP method, and the request and response types. To add an endpoint to the document, map it in the Api project and use types from `Evo.Darwin.Contracts` for the request and the response.

The document uses OpenAPI 3.1. Its title is `Evo.Darwin.Api | v1`.

The document has no paths today. `/health` is mapped as a health check, not as an API endpoint, so it is not listed.

`Program.cs` maps the document only when the environment is `Development`. In any other environment `/openapi/v1.json` returns 404.

## Where to get the document

| Where | Served | How |
| --- | --- | --- |
| Local run | Yes | `dotnet run --project src/Darwin/Evo.Darwin.Api`, then open <http://localhost:5080/openapi/v1.json> |
| prod | No | It runs with `ASPNETCORE_ENVIRONMENT=Production`. In the pilot it is also the test environment, so no deployed environment serves the document. |

TODO: decide where consumers who cannot run the service get the document, for example a file published with every release, and describe it here.

TODO: add the base URL of each environment once the service is reachable from outside the cluster.

## Galaxy

`Evo.Galaxy.Api` generates its document with the same two lines in its [Program.cs](../../src/Galaxy/Evo.Galaxy.Api/Program.cs), from the endpoints mapped in `Evo.Galaxy.Api` and the types of `Evo.Galaxy.Contracts`. Its title is `Evo.Galaxy.Api | v1`. It has no paths today.

In a local run the document is at <http://localhost:5081/openapi/v1.json>:

```bash
dotnet run --project src/Galaxy/Evo.Galaxy.Api
```

`Evo.Galaxy.Api` is not deployed, so no environment serves its document.
