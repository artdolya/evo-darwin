# API

The HTTP API of Evo.Darwin is described by an OpenAPI document. The document is generated from the code. It is not stored in the repository.

## How the document is generated

The `Microsoft.AspNetCore.OpenApi` package builds the document at run time, when it is requested. Two lines in [Program.cs](../../src/Evo.Darwin.Api/Program.cs) turn it on:

- `builder.Services.AddOpenApi()` registers the generator.
- `app.MapOpenApi()` serves the document at `/openapi/v1.json`.

The generator reads the endpoints mapped in `Evo.Darwin.Api`: the route, the HTTP method, and the request and response types. To add an endpoint to the document, map it in the Api project and use types from `Evo.Darwin.Contracts` for the request and the response.

The document uses OpenAPI 3.1. Its title is `Evo.Darwin.Api | v1`.

The document has no paths today. `/health` is mapped as a health check, not as an API endpoint, so it is not listed.

`Program.cs` maps the document only when the environment is `Development`. In any other environment `/openapi/v1.json` returns 404.

## Where to get the document

| Where | Served | How |
| --- | --- | --- |
| Local run | Yes | `dotnet run --project src/Evo.Darwin.Api`, then open <http://localhost:5080/openapi/v1.json> |
| dev | Yes, dev runs with `ASPNETCORE_ENVIRONMENT=Development` | Inside the cluster: `http://evo-darwin.evo-darwin/openapi/v1.json`. From a workstation: see below. |
| staging, prod | No | They run as `Staging` and `Production`. |

To read the document from dev on a workstation with access to the cluster, forward a local port to the Service:

```bash
kubectl -n evo-darwin port-forward service/evo-darwin 8080:80
```

```bash
curl http://localhost:8080/openapi/v1.json
```

TODO: decide where consumers who cannot run the service or reach the dev cluster get the document, for example a file published with every release, and describe it here.

TODO: add the base URL of each environment once the service is reachable from outside the cluster.
