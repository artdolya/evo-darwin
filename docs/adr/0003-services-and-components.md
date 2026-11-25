# 0003. Services and components

## Status

Accepted, 2026-11-24.

## Context

[ADR 0001](0001-repository-structure.md) describes a repository that holds one service, Darwin, with one host, `Evo.Darwin.Api`. In that structure the Api references `Evo.Darwin.Infrastructure`, which holds the database context, the migrations and the clients of external services.

The owner of the repository asked for more components, with these requirements:

- Darwin has a UI, a JavaScript application. The framework is discussed separately.
- The Darwin API has access to the cache (Redis) and to the message bus (RabbitMQ). It has no direct access to PostgreSQL or to an LLM. It works with the business and bus models, through services.
- A Darwin Worker sits behind RabbitMQ and processes the requests of the API. It has access to PostgreSQL, and uses providers to reach blob storage, an LLM and other systems. The Workers are scaled with the load, starting with one.
- Darwin migrations run from their own project. The context and the entities are in separate projects.
- Galaxy is the administration of Evo. It has a UI, an API, a Worker and migrations, like Darwin.
- Evo may get a home site with a few static pages: basic information about Evo, and how to get the app from Google Play and from the App Store.

This ADR changes two things that ADR 0001 records: the repository holds several services and not Darwin alone, and in its decision 2 the Api no longer references Infrastructure. The rest of ADR 0001 stands.

For the layout of the Darwin libraries, three options were considered:

1. Add one project, `Evo.Darwin.Data`, for the context. Keep `Evo.Darwin.Infrastructure` for repositories and providers, and let only the Worker reference it.
2. The same split with the names of an earlier Evo repository: `Evo.Darwin.Data.EntityFramework` for the context, and `Evo.Darwin.Entities` renamed to `Evo.Darwin.Data.Entities`.
3. Replace Infrastructure with two projects: `Evo.Darwin.Providers`, and a shared `Evo.Darwin.Messaging` with the clients of RabbitMQ and Redis.

## Decision

### 1. The repository holds every service of Evo

We will keep Darwin, Galaxy and the home site in this repository and in one solution. A project is named `Evo.<Service>.<Component>`, as ADR 0001 decided: `Evo.Darwin.Api`, `Evo.Galaxy.Worker`, `Evo.Home.Site`.

The projects of a service are in a folder named after the service: `src/Darwin/`, `src/Galaxy/` and `src/Home/`, and `tests/Darwin/` and `tests/Galaxy/` for the test projects. The solution has the same folders. Reason: `src/` and the solution show the services first, and the projects of one service together.

No project of one service references a project of another service. Code that both services need belongs in Krapka: see [ADR 0004](0004-krapka-as-source.md).

TODO: record the reason for one repository over one repository for each service. The choice was made without a recorded reason.

### 2. Darwin and Galaxy each have four components

| Component | Project | Kind |
| --- | --- | --- |
| UI | `Evo.<Service>.Ui` | JavaScript application |
| API | `Evo.<Service>.Api` | ASP.NET Core web application |
| Worker | `Evo.<Service>.Worker` | .NET console application on the generic host |
| Migrations | `Evo.<Service>.Migrations` | .NET console application |

The UI calls the API. The API sends work to the Worker over RabbitMQ. The Worker reads and writes the database and calls the providers. Migrations changes the schema of the database.

Reason for a Worker behind the message bus: the number of Workers can follow the load without a change to the API.

### 3. The API cannot reach the database or a provider

We will keep the API away from PostgreSQL, blob storage and an LLM through the project references, so that the compiler enforces it:

- `Evo.<Service>.Api` references Contracts, Models and Domain. It does not reference Infrastructure or Data.
- `Evo.<Service>.Worker` references Models, Domain and Infrastructure.
- `Evo.<Service>.Infrastructure` holds the repositories and the providers. Only the Worker references it.

The clients of Redis and RabbitMQ are registered in the hosts, the Api and the Worker. They get no project of their own until there is code to share.

### 4. The context, the entities and the migrations are three projects

We will use option 1:

- `Evo.<Service>.Entities` holds the classes that describe the tables.
- `Evo.<Service>.Data` holds the EF Core context and the mapping of the entities to the tables. It references Entities.
- `Evo.<Service>.Migrations` holds the migration classes and the program that applies them. It references Data.

Reason for option 1 over option 2: it renames no existing project, and it keeps the one-word component names that ADR 0001 uses. Reason for option 1 over option 3: it adds one project and not two, and no code exists yet that the two extra projects would hold.

The separate Migrations project is a requirement of the owner.

TODO: record the reason for it.

### 5. The home site and the UIs are folders until they are built

We will keep a folder with a README for `Evo.Darwin.Ui`, `Evo.Galaxy.Ui` and `Evo.Home.Site`. Each README says what the component is and what is not decided.

## Consequences

### One repository

- One pull request can change Darwin, Galaxy and Krapka references together, and one CI run builds and tests all of them.
- The solution is renamed from `Evo.Darwin.sln` to `Evo.sln`. The repository and the Helm chart are still named after Darwin: `evo-darwin`. Those names no longer say what the repository holds.
- The version tags of [ADR 0002](0002-versions-and-releases.md) are tags of the repository. Darwin and Galaxy get the same version, and cannot be released one without the other being tagged.

### Components

- A feature that needs the database is written in two hosts: an endpoint in the Api, and a consumer in the Worker, with a message type in Models between them.
- A request that goes through the Worker is asynchronous. How its result returns to the API is not decided.
- Darwin and Galaxy have the same twelve projects each. A change to the structure of one has to be repeated in the other by hand.
- Only `Evo.Darwin.Api` has a container image and is deployed. The Workers, the Migrations programs, the Galaxy components, the UIs and the home site are not built by the pipeline and not deployed.

### Project references

- The compiler stops the Api from using the context, a repository, a provider or an entity. ADR 0001 left the rule about entities to reviewers. It is now enforced.
- Both hosts load Domain. A Domain service that needs a repository can be called from Api code. It fails at run time, because the Api registers no repository.
- The Worker can reach the context through Infrastructure, so the compiler does not stop it from applying migrations. Reviewers enforce that only Migrations changes the schema.
- The Migrations program can run with a database user that may change tables, and the Worker with a user that may not.
- RabbitMQ and Redis client code is written in each host. When the same code appears in two hosts, it has to move to a shared project or to Krapka.

### Open choices

- The framework of the UIs, and whether the home site is built.
- The client libraries of Redis and RabbitMQ, the blob storage and the LLM providers.
- Whether Darwin and Galaxy use one PostgreSQL server or two, and how Galaxy reads the data of Darwin.
