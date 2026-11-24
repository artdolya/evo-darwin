# Documentation

Documentation of the Evo.Darwin service. It lives in the repository so that it is reviewed and versioned in the same pull requests as the code.

## Index

| Document | What it answers |
| --- | --- |
| [../README.md](../README.md) | How do I build, run and test the service locally? |
| [architecture/overview.md](architecture/overview.md) | What does the service talk to, how are projects named, and which project may reference which? |
| [api/README.md](api/README.md) | How is the OpenAPI document generated and where do I get it? |
| [configuration.md](configuration.md) | Which environment variables and secrets exist, and where does each value come from? |
| [runbooks/deploy.md](runbooks/deploy.md) | How does a change reach dev, staging and prod? |
| [runbooks/rollback.md](runbooks/rollback.md) | How do I return an environment to the previous version? |
| [runbooks/template.md](runbooks/template.md) | Template for an alert runbook. |
| [adr/0001-repository-structure.md](adr/0001-repository-structure.md) | Why is the repository structured this way? |
| [adr/template.md](adr/template.md) | Template for an architecture decision record. |

Every .NET project has its own README. It says what the project is for, how to run it or its tests, and which environment variables it needs.

| Project README | Project |
| --- | --- |
| [Evo.Darwin.Api](../src/Evo.Darwin.Api/README.md) | The host: HTTP endpoints and configuration. The only project that runs. |
| [Evo.Darwin.Contracts](../src/Evo.Darwin.Contracts/README.md) | Request and response types of the external API. |
| [Evo.Darwin.Models](../src/Evo.Darwin.Models/README.md) | Types used on the message bus and in the business layer. |
| [Evo.Darwin.Entities](../src/Evo.Darwin.Entities/README.md) | Classes that describe the database tables. |
| [Evo.Darwin.Domain](../src/Evo.Darwin.Domain/README.md) | Business logic. |
| [Evo.Darwin.Infrastructure](../src/Evo.Darwin.Infrastructure/README.md) | Database access and external clients. |
| [Evo.Darwin.UnitTests](../tests/Evo.Darwin.UnitTests/README.md) | Unit tests. |
| [Evo.Darwin.IntegrationTests](../tests/Evo.Darwin.IntegrationTests/README.md) | Tests that call the API over HTTP. |

## Rules for writing docs

### Format and file names

- Write in Markdown as GitHub renders it.
- Name files in kebab-case with the `.md` extension, for example `message-retries.md`.
- `README.md` is the only upper-case name. It is the entry page of its folder.
- Name an ADR `NNNN-short-title.md`. `NNNN` is the next free four-digit number. Numbers are never reused.

### Where each type of doc goes

| Type | Location |
| --- | --- |
| How to build, run and test the whole service locally | `README.md` in the repository root |
| What one .NET project is for, how to run it or its tests, and the environment variables it needs | `README.md` in the folder of the project |
| Structure of the service and its surroundings | `docs/architecture/` |
| A decision and its reasons | `docs/adr/`, one file per decision, copied from `adr/template.md` |
| How to use the HTTP API | `docs/api/` |
| Steps to operate the service or to react to an alert | `docs/runbooks/`, one file per procedure or alert; alert runbooks are copied from `runbooks/template.md` |
| Environment variables and secrets | `docs/configuration.md` |

Add a new document only if someone will keep it current. A document that nobody maintains misleads people. Add every new document to the index above.

### Project READMEs

Every .NET project in `src/` and `tests/` has a `README.md` in its folder. A new project gets its README in the pull request that adds it. The README has these headings:

1. **What belongs here**: what the project is for, and what must go into another project instead.
2. **References**: the projects it references.
3. **Run locally**: the command that runs it. For a class library, say that it cannot be run on its own and name the project that loads it. A test project has **Run the tests** instead.
4. **Tests**: the test project that covers it and the command that runs those tests. A test project leaves this heading out.
5. **Environment variables**: the variables the project reads, or "None". The complete table for every environment stays in `docs/configuration.md`.

### Diagrams

Write diagrams as [Mermaid](https://mermaid.js.org/) text in a fenced `mermaid` code block. GitHub renders it, and a change to a diagram shows up in the diff. Do not commit diagrams as image files.

### Docs change with the code

Update a doc in the same pull request as the code it describes. The pull request template has a checkbox for it. A pull request that changes behaviour, configuration, the pipeline or the structure without the matching doc change is not complete.

### Review

Doc changes are reviewed in the pull request like code, by the same reviewers. The reviewer checks that the doc matches what the pull request does. GitHub requests reviews from the owners listed in [../.github/CODEOWNERS](../.github/CODEOWNERS).

TODO: name the team that reviews doc changes. `CODEOWNERS` has no owner yet because the owning team is not recorded.

### Audience and tone

- Write for an engineer who knows .NET and Kubernetes and is new to this service.
- Write runbooks for someone under time pressure: numbered steps, one action per step, the exact command, and the result to expect.
- Use short sentences and plain words. State facts. Leave out history and opinion, except in ADRs, which record why.
- Write commands, file paths, names and values in code formatting, exactly as they are typed.

### Unknown information

Do not guess. If you do not have the information, write a line that starts with `TODO:` and says what is needed. List the open ones with:

```bash
grep -rn "TODO:" --include="*.md" .
```

### Company style guide

TODO: add the link to the company-wide documentation style guide. Where it differs from the rules above, say which one applies.
