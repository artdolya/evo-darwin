# Documentation

Documentation of the Evo services in this repository: Darwin, Galaxy and the home site. It lives in the repository so that it is reviewed and versioned in the same pull requests as the code.

## Index

| Document | What it answers |
| --- | --- |
| [../README.md](../README.md) | How do I set up the repository, and build, run and test the services locally? |
| [../CONTRIBUTING.md](../CONTRIBUTING.md) | How do I contribute, and when and how do I update the docs? |
| [architecture/overview.md](architecture/overview.md) | Which services and components exist, what may each component reach, how are projects named, and which project may reference which? |
| [SDLC.md](SDLC.md) | Which phases take a Dreamer's idea to running software, what does each phase produce, which roles work in each phase, and how does a demo work? |
| [dream-context.md](dream-context.md) | What is DreamContext, which parts and scores does it have, when is a point confirmed, and how does a confirmed point become a test? |
| [roles/README.md](roles/README.md) | Which roles exist, when is each one engaged, which architect role decides what, and what is a specialization of a role? |
| [api/README.md](api/README.md) | How is the OpenAPI document generated and where do I get it? |
| [../src/Docker/README.md](../src/Docker/README.md) | How do I run the complete stack in Docker, from Visual Studio or from the command line, and where do the values of my own machine go? |
| [configuration.md](configuration.md) | Which environment variables and secrets exist, and where does each value come from? |
| [runbooks/deploy.md](runbooks/deploy.md) | How is a version tagged, released and deployed? |
| [runbooks/rollback.md](runbooks/rollback.md) | How do I return an environment to the previous version? |
| [runbooks/template.md](runbooks/template.md) | Template for an alert runbook. |
| [adr/0001-repository-structure.md](adr/0001-repository-structure.md) | Why is the repository structured this way? |
| [adr/0002-versions-and-releases.md](adr/0002-versions-and-releases.md) | Why does every build have a version tag, and why is a release started by hand? |
| [adr/0003-services-and-components.md](adr/0003-services-and-components.md) | Why do Darwin and Galaxy each have a UI, an API, a Worker and Migrations, and why can the API not reach the database? |
| [adr/0004-krapka-as-source.md](adr/0004-krapka-as-source.md) | Why are the Krapka libraries built from a linked checkout and not taken from NuGet? |
| [adr/template.md](adr/template.md) | Template for an architecture decision record. |

Every role of the SDLC has its own document. It says what the role does and decides, how deep it works at each tier, and what it does in each phase.

| Group | Role documents |
| --- | --- |
| Decision | [Dreamer](roles/dreamer.md) |
| Contact | [Darwin](roles/darwin.md) |
| Product | [Product manager](roles/product-manager.md), [Business analyst](roles/business-analyst.md), [UX designer](roles/ux-designer.md) |
| Delivery | [Project manager](roles/project-manager.md) |
| Architecture | [Solution architect](roles/solution-architect.md), [Software architect](roles/software-architect.md), [Data architect](roles/data-architect.md), [Infrastructure architect](roles/infrastructure-architect.md), [Security architect](roles/security-architect.md), [AI architect](roles/ai-architect.md) |
| Engineering | [Tech lead](roles/tech-lead.md), [Developer](roles/developer.md) |
| Quality | [QA engineer](roles/qa-engineer.md) |
| Operations | [DevOps engineer](roles/devops-engineer.md), [Site reliability engineer](roles/site-reliability-engineer.md) |
| Documentation | [Technical writer](roles/technical-writer.md) |

Every project has its own README. It says what the project is for, how to run it or its tests, and which environment variables it needs. Darwin and Galaxy have the same projects.

| Project | Darwin | Galaxy |
| --- | --- | --- |
| The browser UI. Not built yet. | [Evo.Darwin.Ui](../src/Darwin/Evo.Darwin.Ui/README.md) | [Evo.Galaxy.Ui](../src/Galaxy/Evo.Galaxy.Ui/README.md) |
| The HTTP API. It runs. | [Evo.Darwin.Api](../src/Darwin/Evo.Darwin.Api/README.md) | [Evo.Galaxy.Api](../src/Galaxy/Evo.Galaxy.Api/README.md) |
| The worker behind the message bus. It runs. | [Evo.Darwin.Worker](../src/Darwin/Evo.Darwin.Worker/README.md) | [Evo.Galaxy.Worker](../src/Galaxy/Evo.Galaxy.Worker/README.md) |
| The migrations of the database. It runs, then exits. | [Evo.Darwin.Migrations](../src/Darwin/Evo.Darwin.Migrations/README.md) | [Evo.Galaxy.Migrations](../src/Galaxy/Evo.Galaxy.Migrations/README.md) |
| Request and response types of the external API. | [Evo.Darwin.Contracts](../src/Darwin/Evo.Darwin.Contracts/README.md) | [Evo.Galaxy.Contracts](../src/Galaxy/Evo.Galaxy.Contracts/README.md) |
| Types used on the message bus and in the business layer. | [Evo.Darwin.Models](../src/Darwin/Evo.Darwin.Models/README.md) | [Evo.Galaxy.Models](../src/Galaxy/Evo.Galaxy.Models/README.md) |
| Classes that describe the database tables. | [Evo.Darwin.Entities](../src/Darwin/Evo.Darwin.Entities/README.md) | [Evo.Galaxy.Entities](../src/Galaxy/Evo.Galaxy.Entities/README.md) |
| Business logic. | [Evo.Darwin.Domain](../src/Darwin/Evo.Darwin.Domain/README.md) | [Evo.Galaxy.Domain](../src/Galaxy/Evo.Galaxy.Domain/README.md) |
| The EF Core context. | [Evo.Darwin.Data](../src/Darwin/Evo.Darwin.Data/README.md) | [Evo.Galaxy.Data](../src/Galaxy/Evo.Galaxy.Data/README.md) |
| Repositories and providers. | [Evo.Darwin.Infrastructure](../src/Darwin/Evo.Darwin.Infrastructure/README.md) | [Evo.Galaxy.Infrastructure](../src/Galaxy/Evo.Galaxy.Infrastructure/README.md) |
| Unit tests. | [Evo.Darwin.UnitTests](../tests/Darwin/Evo.Darwin.UnitTests/README.md) | [Evo.Galaxy.UnitTests](../tests/Galaxy/Evo.Galaxy.UnitTests/README.md) |
| Tests that call the API over HTTP. | [Evo.Darwin.IntegrationTests](../tests/Darwin/Evo.Darwin.IntegrationTests/README.md) | [Evo.Galaxy.IntegrationTests](../tests/Galaxy/Evo.Galaxy.IntegrationTests/README.md) |

The home site has one folder: [Evo.Home.Site](../src/Home/Evo.Home.Site/README.md). It holds one static page.

## Writing and updating docs

The rules for docs are in the [Documentation section of CONTRIBUTING.md](../CONTRIBUTING.md#documentation), and only there: which doc to update for which change, where each type of doc lives, the format, the writing style, the ADR lifecycle and the review.

When you add, rename or remove a document, update the index above in the same pull request.
