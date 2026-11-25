# Contributing to Evo

This file is the one place that says how to contribute to this repository: the workflow, where code and tests belong, and when and how to update the documentation.

The documentation is kept next to the code. It stays true only if every contributor updates it together with the code. That is why [Documentation](#documentation) is the longest section of this file.

## Getting started

Set up, build, run and test the services as described in [README.md](README.md). The setup includes a checkout of Krapka next to this repository. The `README.md` in each project folder has the commands for that project.

## Workflow

### Branches

`master` is the branch that releases to prod are made from. Every push to `master` gets a version tag, for example `0.0.2`. Nothing is deployed until someone starts a release of a tag. The tags and the releases are described in [docs/runbooks/deploy.md](docs/runbooks/deploy.md).

Make every change on a branch created from `master`, and bring it to `master` with a pull request.

TODO: state the naming convention for branches.

TODO: state the format of commit messages.

TODO: state how pull requests are merged (merge commit, squash or rebase). The revert command in [docs/runbooks/rollback.md](docs/runbooks/rollback.md) depends on it.

TODO: state whether direct pushes to `master` are blocked, and which checks are required before a merge. Branch protection is a GitHub setting and is not recorded in the repository.

### Pull requests

1. Create a branch from `master`.
2. Make the change. Put its tests and its doc updates in the same branch. See [Tests](#tests) and [Documentation](#documentation).
3. Format, build and test locally:

   ```bash
   make format
   ```

   ```bash
   dotnet build
   ```

   ```bash
   dotnet test
   ```

4. Open a pull request into `master`. GitHub fills the description from [.github/pull_request_template.md](.github/pull_request_template.md). Say what the change does and why, say how it was tested, and go through the checklist.
5. Wait for the [checks](#checks) to pass and for the [review](#code-review).
6. Merge the pull request.

Every push to the pull request gets a version tag, for example `0.0.1-PR2-003`. To try the change in the test environment before the merge, release that tag: [docs/runbooks/deploy.md](docs/runbooks/deploy.md#release-a-pull-request-build-to-test).

A merge does not deploy. It gives `master` the next version tag. The tags of the pull request are deleted, except one that is still deployed. To deploy the new version to prod, release its tag: [docs/runbooks/deploy.md](docs/runbooks/deploy.md#release-a-master-version-to-prod). The same runbook lists the setup the pipeline needs before its first deployment.

### Checks

GitHub Actions runs these workflows on a pull request:

| Workflow | Runs when | What it does |
| --- | --- | --- |
| **CI** ([ci.yml](.github/workflows/ci.yml)) | Every pull request, and every push to `master` | Clones Krapka next to the repository. Then `dotnet restore`, then `dotnet format --verify-no-changes --no-restore --exclude src/Krapka`, then `dotnet build --no-restore --configuration Release`, then `dotnet test --no-build --configuration Release`. The format step fails when `dotnet format` would change a file. The test step runs the unit tests and the integration tests of Darwin and of Galaxy. |
| **Terraform plan** ([terraform-plan.yml](.github/workflows/terraform-plan.yml)) | A pull request that changes a file in `deploy/terraform/` | `terraform fmt -check -recursive deploy/terraform`. Then, for the prod environment: `terraform init`, `terraform validate` and `terraform plan`. |
| **Tag** ([tag.yml](.github/workflows/tag.yml)) | Every push to a pull request, and every push to `master` | Creates the next version tag for the commit. It checks nothing, and it fails only if the tag cannot be created. |
| **Cleanup** ([cleanup.yml](.github/workflows/cleanup.yml)) | A pull request is closed, merged or not | Deletes the version tags of closed pull requests. It keeps a tag that is deployed. |

The **Release** workflow ([release.yml](.github/workflows/release.yml)) does not run on a pull request. Someone starts it by hand to deploy one version tag.

- The build treats compiler warnings as errors. A warning fails CI.
- CI builds the Krapka libraries from the newest commit of the Krapka repository. See [Krapka](#krapka).
- The plan jobs need access to the cloud provider, the clusters and the Terraform state. That setup is listed in [docs/runbooks/deploy.md](docs/runbooks/deploy.md#before-the-first-deployment).
- When you change the Terraform code, read the plan in the pull request.
- No workflow checks the Helm chart or the documentation. Reviewers check them.

When you change the Helm chart, bump `version` in `deploy/helm/evo-darwin/Chart.yaml`. The reason is in [docs/runbooks/deploy.md](docs/runbooks/deploy.md#change-the-chart-or-the-terraform-code). Lint the chart locally:

```bash
helm lint deploy/helm/evo-darwin
```

A pull request fails its checks when the C# code or the Terraform code is not formatted. Format both before you push:

```bash
make format
```

`make format` runs `dotnet format --exclude src/Krapka` and then `terraform fmt -recursive deploy/terraform`. It needs Make, the .NET SDK and Terraform. If Terraform is not installed and your change does not touch `deploy/terraform/`, run `dotnet format --exclude src/Krapka` alone.

Do not run `dotnet format` without `--exclude src/Krapka`. It changes the files of the Krapka checkout, which belong to another repository.

The `Makefile` has two more targets, `make up` and `make down`. They start and stop the complete stack in Docker, and they check nothing. See [README.md](README.md#run-the-complete-stack).

The formatting rules for C# are in `.editorconfig`. The CI check covers the C# files of the solution, except the Krapka files: indentation and other whitespace, line endings, and the order of `using` directives. It does not cover:

- A rule with the severity `suggestion` or `silent`, such as file-scoped namespaces. Editors show these rules. Reviewers check them.
- Files that are not C#, such as JSON, YAML and Markdown. Editors apply `.editorconfig` to them.

To run the CI check locally, without changing a file:

```bash
dotnet format --verify-no-changes --exclude src/Krapka
```

### Code review

GitHub requests a review from the code owners in [.github/CODEOWNERS](.github/CODEOWNERS) on every pull request. The file has no owner yet: its only rule is commented out, so GitHub requests no review by itself. Until the owner is set, request a reviewer yourself.

TODO: name the owning team and set it in `.github/CODEOWNERS`.

TODO: state how many approvals a pull request needs before it is merged.

The reviewer checks the code, the tests and the docs. What to check in the docs is listed in [Reviewing docs](#reviewing-docs).

Releasing a version is a separate step. It is described in [docs/runbooks/deploy.md](docs/runbooks/deploy.md).

## Code

This section is a summary. The full description is in [docs/architecture/overview.md](docs/architecture/overview.md).

### Naming

Every project is named `<Project>.<Service>.<Component>`. In this repository that is `Evo.<Service>.<Component>`, for example `Evo.Darwin.Api` or `Evo.Galaxy.Worker`. The services are Darwin, Galaxy and Home. The folder and the project file have the same name as the project. The folder of a project is in the folder of its service, for example `src/Darwin/Evo.Darwin.Api` or `tests/Galaxy/Evo.Galaxy.UnitTests`.

`evo-darwin` is the kebab-case form of the project and service name. It names the Helm chart, the chart folder, the Kubernetes namespace and the Kubernetes resources of Darwin.

### Where new code belongs

The table names the projects of Darwin. Galaxy has the same projects with the prefix `Evo.Galaxy.`, and the same rules.

| New code | Project |
| --- | --- |
| An HTTP endpoint, start-up code and configuration of the API | `Evo.Darwin.Api` |
| Mapping between Contracts types and Models types | `Evo.Darwin.Api` |
| A client of the cache (Redis) | `Evo.Darwin.Api` |
| A client of the message bus (RabbitMQ) | The host that uses it: `Evo.Darwin.Api` or `Evo.Darwin.Worker` |
| A consumer of messages, start-up code and configuration of the Worker | `Evo.Darwin.Worker` |
| A request or response type of the external API | `Evo.Darwin.Contracts` |
| A type used in the business logic or on the message bus | `Evo.Darwin.Models` |
| A business rule or a service | `Evo.Darwin.Domain` |
| A class that describes a database table | `Evo.Darwin.Entities` |
| The context, the mapping of an entity to its table | `Evo.Darwin.Data` |
| A migration | `Evo.Darwin.Migrations`. `dotnet ef` generates it: see [its README](src/Darwin/Evo.Darwin.Migrations/README.md#add-a-migration). |
| A repository, a provider (a client of blob storage, of an LLM or of another external system) | `Evo.Darwin.Infrastructure` |
| Mapping between Entities types and Models types | `Evo.Darwin.Infrastructure` |
| Code of the browser UI | `Evo.Darwin.Ui` |
| Code that Darwin and Galaxy both need | Krapka. See [Krapka](#krapka). |

The `README.md` of each project says what belongs in it and what does not.

### Allowed project references

The table names the projects of Darwin. The same table applies to Galaxy with the prefix `Evo.Galaxy.`.

| Project | May reference |
| --- | --- |
| `Evo.Darwin.Api` | Contracts, Models, Domain |
| `Evo.Darwin.Worker` | Models, Domain, Infrastructure |
| `Evo.Darwin.Migrations` | Data |
| `Evo.Darwin.Contracts` | No other project |
| `Evo.Darwin.Models` | No other project |
| `Evo.Darwin.Entities` | `KrapkaNet.Data.Abstractions` |
| `Evo.Darwin.Domain` | Models |
| `Evo.Darwin.Data` | Entities, `KrapkaNet.EntityFramework.Abstractions` |
| `Evo.Darwin.Infrastructure` | Domain, Models, Entities, Data |

Do not add a project reference that is not in this table. A project of one service never references a project of another service. These rules follow:

- The Api has no access to the database, to blob storage, to an LLM or to another provider. The compiler enforces this: the Api references neither Infrastructure nor Data. Send the work to the Worker over the message bus.
- The Api never returns Entities. The compiler enforces this too: the Api cannot see Entities.
- Contracts types never reach Domain, the Worker or Infrastructure. The compiler enforces this: none of them references Contracts.
- Only Migrations changes the schema of the database. The compiler does not enforce this, because the Worker reaches the context through Infrastructure. Reviewers check it.

These rules are recorded decisions: [ADR 0001](docs/adr/0001-repository-structure.md) and [ADR 0003](docs/adr/0003-services-and-components.md). To change them, write a new ADR. See [ADR lifecycle](#adr-lifecycle).

### Krapka

Krapka is a set of shared libraries in another repository. This repository builds them from source through the link `src/Krapka`. The setup is in [README.md](README.md#krapka), and the full description in [docs/architecture/overview.md](docs/architecture/overview.md#krapka).

- A file under `src/Krapka` belongs to the Krapka repository. Commit and push a change to it there, not here.
- Push the Krapka commit before you open the pull request here. CI clones Krapka, and fails if the code it needs is not pushed.
- Do not copy Krapka code into this repository.
- To use one more Krapka project, add a `ProjectReference` whose path starts with `$(KrapkaNetRoot)`, as in `src/Darwin/Evo.Darwin.Entities/Evo.Darwin.Entities.csproj`. Then add the Krapka project to the solution folder `Krapka`:

  ```bash
  dotnet sln add --solution-folder Krapka src/Krapka/src/Net/<Area>/<Project>/<Project>.csproj
  ```

- Keep an Evo project as the first project in `Evo.sln`. When a Krapka project is first, `dotnet format` reads the `global.json` of Krapka, which asks for .NET SDK 9, and fails with `A compatible .NET SDK was not found`. `dotnet sln add` puts a project at the end of the file, so the order stays right unless the solution is rebuilt or edited by hand.

This setup is a recorded decision: [ADR 0004](docs/adr/0004-krapka-as-source.md).

### Shared settings

- `Directory.Build.props` sets the target framework, nullable reference types, implicit usings and warnings as errors for every project. Do not repeat these settings in a project file. It also sets `KrapkaNetRoot`, the folder of the Krapka projects.
- `Directory.Packages.props` holds the version of every NuGet package. To add a package, add a `PackageVersion` line there, and a `PackageReference` without a version in the project file.
- `global.json` selects the .NET SDK.
- `dotnet-tools.json` lists the .NET tools of the repository. `dotnet tool restore` installs them.
- `.editorconfig` holds the formatting and code style rules. Editors, `dotnet format` and the CI formatting check read it.

### Adding a project

1. Create the project in `src/<Service>/`, or in `tests/<Service>/` for a test project. Name it `Evo.<Service>.<Component>`.
2. Add it to `Evo.sln`, in the solution folder that has the same path as the folder on disk: `dotnet sln add --solution-folder src/<Service> <path of the project file>`.
3. Reference only projects that the table above allows.
4. Add a `README.md` to the project folder. Its headings are listed in [Project READMEs](#project-readmes).
5. Add the project to the tables in [docs/architecture/overview.md](docs/architecture/overview.md) and in [docs/README.md](docs/README.md).

## Tests

| What you change | Test it needs | Where the test goes |
| --- | --- | --- |
| Business logic in `Evo.Darwin.Domain` or `Evo.Galaxy.Domain` | A unit test | `tests/Darwin/Evo.Darwin.UnitTests` or `tests/Galaxy/Evo.Galaxy.UnitTests` |
| An endpoint: a new one, or a change in what it accepts or returns | An integration test that calls the endpoint over HTTP | `tests/Darwin/Evo.Darwin.IntegrationTests` or `tests/Galaxy/Evo.Galaxy.IntegrationTests` |
| A type in Contracts, Models or Entities | No test of its own. These projects hold no logic. The tests of the code that uses the type cover it. | |

TODO: state how the consumers in the Worker, the repositories and providers in Infrastructure, the context in Data and the migrations are tested. No test project references these projects.

- A unit test tests one class or a few classes. It does not start the API and needs no database, network or other running dependency.
- An integration test starts the API of its service in memory with `WebApplicationFactory` and calls it over HTTP. It opens no network port. Do not start the API first.
- A unit test project references only the Domain project of its service. To unit-test code in another project, add a reference to that project.
- `SampleTests` in each unit test project is a placeholder. Replace it with the first real test.
- CI runs the four test projects on every pull request. It does not measure test coverage.

Run all tests from the repository root:

```bash
dotnet test
```

Run one test project, for example the unit tests of Darwin:

```bash
dotnet test tests/Darwin/Evo.Darwin.UnitTests
```

The four test projects are `Evo.Darwin.UnitTests`, `Evo.Darwin.IntegrationTests`, `Evo.Galaxy.UnitTests` and `Evo.Galaxy.IntegrationTests`, in `tests/Darwin/` and `tests/Galaxy/`. More options are in the README of each one.

## Documentation

### Principle

Docs change in the same pull request as the code they describe. A pull request that makes a doc wrong is not ready to merge.

This applies to every doc in the repository: the files in `docs/`, the `README.md` in the root and in each project folder, and this file.

Before you open a pull request, find the docs your change affects in the table below and update them in the same branch. If the change affects no doc, confirm that in the pull request checklist.

### If you change this, update that

| If you change | Update |
| --- | --- |
| An endpoint, or a request or response type in a Contracts project | [docs/api/](docs/api/README.md), and the endpoint table in the README of the Api project |
| An environment variable or a secret: you add, remove or rename it, or change its default | [docs/configuration.md](docs/configuration.md), and the "Environment variables" section in the README of the project that reads it. Also `src/Docker/docker-compose.yml`, if a component needs the variable to run in the local stack. |
| The local stack in `src/Docker/`: a container, a port, a variable or its default value, or a Dockerfile that the stack builds | [src/Docker/README.md](src/Docker/README.md), and "Local stack" in [docs/configuration.md](docs/configuration.md) |
| A workflow in `.github/workflows/`, a script in `scripts/`, the Dockerfile, the Helm chart or the Terraform code | [docs/runbooks/deploy.md](docs/runbooks/deploy.md) and [docs/runbooks/rollback.md](docs/runbooks/rollback.md). Also [docs/configuration.md](docs/configuration.md) if a pipeline variable, a Terraform variable or a value of an environment changes, and [Checks](#checks) in this file if a workflow runs something else. |
| An alert: you add one | A new runbook, copied from [docs/runbooks/template.md](docs/runbooks/template.md) |
| A dependency (an external service, the message bus), a data store, or the project layout (a new project, a changed project reference) | [docs/architecture/overview.md](docs/architecture/overview.md). For a new project also its `README.md`. |
| What a project is for, or what it references | The `README.md` of the project, and [docs/architecture/overview.md](docs/architecture/overview.md) |
| A decision that is not obvious or is hard to reverse: you make one, or change one | A new ADR, copied from [docs/adr/template.md](docs/adr/template.md). See [ADR lifecycle](#adr-lifecycle). |
| The steps to set up, build, run or test | [README.md](README.md), and "Run locally" or "Run the tests" in the README of the project |
| A target in the `Makefile`: you add, rename or remove one | [Checks](#checks) in this file, and [README.md](README.md) |
| How to contribute: the workflow, the checks, or a rule in this file | This file |
| The phase diagram in [docs/SDLC.md](docs/SDLC.md#phases): a phase, an arrow or a label | `docs/assets/sdlc-phases.py`, and render `docs/assets/sdlc-phases.gif` again. See [Animations](#animations). |
| Any document: you add, rename or remove one | The index in [docs/README.md](docs/README.md) |

The table cannot list every case. Search the docs for each name you change or remove. For example, after a change to `ASPNETCORE_ENVIRONMENT`:

```bash
grep -rn "ASPNETCORE_ENVIRONMENT" --include="*.md" .
```

### Where each doc lives

| Location | What it is for |
| --- | --- |
| `README.md` in the repository root | Setting up, building, running and testing the services locally. |
| `CONTRIBUTING.md` | How to contribute, and the rules for docs. |
| `README.md` in each project folder | What the project is for, how to run it or its tests, and the environment variables it needs. |
| `docs/README.md` | The index of all documents. |
| `docs/SDLC.md` | The process that takes a Dreamer's idea to running software: the phases, their outputs, and the roles in each phase. It describes the projects that Evo builds, not the workflow of this repository. |
| `docs/dream-context.md` | DreamContext, the internal document that holds what Evo knows about one Dream: its parts, the status of each point, its scores and its life. |
| `docs/roles/` | The roles of that process, one file per role. `docs/roles/README.md` lists the headings of a role document. |
| `docs/assets/` | Animations that accompany a diagram, each with the script that renders it. See [Animations](#animations). |
| `docs/architecture/` | The structure of the services and their surroundings: components, dependencies, data stores, projects and their allowed references. |
| `docs/adr/` | Decisions and their reasons, one file per decision. |
| `docs/api/` | How to use the HTTP API, and where to get the OpenAPI document. |
| `docs/runbooks/` | Steps to operate the service, one file per procedure, and one file per alert. |
| `docs/configuration.md` | Every environment variable and secret: meaning, default, and where the value comes from. |

Add a new document only if someone will keep it current. A document that nobody maintains misleads people. Add every new document to the index in [docs/README.md](docs/README.md).

### Format

- Write in Markdown as GitHub renders it.
- Name files in kebab-case with the `.md` extension, for example `message-retries.md`.
- `README.md`, `CONTRIBUTING.md` and `SDLC.md` are the only upper-case names. A `README.md` is the entry page of its folder.
- Name an ADR `NNNN-short-title.md`. `NNNN` is the next free four-digit number. Numbers are never reused.
- Write diagrams as [Mermaid](https://mermaid.js.org/) text in a fenced `mermaid` code block. GitHub renders it, and a change to a diagram can be reviewed in the diff. Do not commit an image file in place of a Mermaid diagram.
- An animation may accompany a Mermaid diagram. The diagram stays in the document and is the source. The conditions are in [Animations](#animations).
- Link to other files of the repository with relative links.

### Animations

An animation is an image file that shows a Mermaid diagram in motion. It is allowed under these conditions:

- The Mermaid diagram stays in the document, next to the animation. The diagram is the source. When the two differ, the diagram is right.
- The animation is in `docs/assets/`, together with the script that renders it. Nobody edits the image by hand.
- The image has alternative text that says what the animation shows.
- A change to the diagram changes the script and the animation in the same pull request.

The repository has one animation: `docs/assets/sdlc-phases.gif`, the phase diagram of [docs/SDLC.md](docs/SDLC.md#phases). `docs/assets/sdlc-phases.py` renders it. The script does not read the Mermaid text. It holds its own copy of the phases, the arrows and the labels.

The script needs Python 3 with the Pillow package. Create a Python environment outside the repository and install Pillow in it:

```bash
python3 -m venv /tmp/evo-docs
```

```bash
/tmp/evo-docs/bin/pip install pillow
```

Render the animation:

```bash
/tmp/evo-docs/bin/python docs/assets/sdlc-phases.py docs/assets/sdlc-phases.gif
```

The command takes about ten seconds. It prints the number of frames and the length of the loop. To look at one frame before you render all of them, for example the frame at 2.5 seconds:

```bash
/tmp/evo-docs/bin/python docs/assets/sdlc-phases.py /tmp/frame.png --still 2.5
```

The image in the repository is rendered with the Ubuntu font. The script uses DejaVu Sans when the Ubuntu font is not installed, and the image then looks different. The font paths in the script are those of Ubuntu Linux. On another system, add a font to `FONTS` in the script.

### Project READMEs

Every .NET project in `src/` and `tests/` has a `README.md` in its folder. A new project gets its README in the pull request that adds it. A component that is not built yet (`Evo.Darwin.Ui`, `Evo.Galaxy.Ui`) has a short README that says what the component is and what is not decided. The README of `Evo.Home.Site`, which is not a .NET project, lists its files and says how to view the site. The README of `src/Docker`, the Docker Compose project, lists its files and says how to start the local stack. The README of a .NET project has these headings:

1. **What belongs here**: what the project is for, and what must go into another project instead.
2. **References**: the projects it references.
3. **Run locally**: the command that runs it. For a class library, say that it cannot be run on its own and name the project that loads it. A test project has **Run the tests** instead.
4. **Tests**: the test project that covers it and the command that runs those tests. A test project leaves this heading out.
5. **Environment variables**: the variables the project reads, or "None". The complete table for every environment stays in `docs/configuration.md`.

### Writing style

- Write for a developer who is new to the service. Assume that the reader knows .NET, and Kubernetes for the deployment docs. Assume that the reader knows nothing about this service.
- Use the present tense. Describe what the repository does now. Leave out history, plans and opinion. ADRs are the exception: they record why.
- Use short sentences and plain words.
- Keep one topic per page. If a page answers two questions, split it.
- Put every command in a fenced code block, complete, so that it can be copied and run from the repository root. Say what result to expect.
- Write file paths, names and values in code formatting, exactly as they are typed.
- Write a runbook for someone under time pressure: numbered steps, one action per step.
- Do not guess. If you do not have the information, write a line that starts with `TODO:` and says what is missing. Remove the line when you add the information.

List the open `TODO:` lines with:

```bash
grep -rn "TODO:" --include="*.md" .
```

### ADR lifecycle

Write an ADR for a decision that is not obvious or is hard to reverse. Copy [docs/adr/template.md](docs/adr/template.md).

An ADR has one of three statuses: Proposed, Accepted, or Superseded by a later ADR.

TODO: state who accepts an ADR and when its status changes from Proposed to Accepted.

An accepted ADR is not rewritten. It records what was decided at that time and why. To change a decision:

1. Write a new ADR with the next free number. In its Context section, name the ADR that it supersedes and link to it.
2. In the old ADR, change the Status section to "Superseded by NNNN", with a link to the new ADR and the date. Change nothing else.
3. Update the docs that describe the old decision, and add the new ADR to the index in [docs/README.md](docs/README.md).

The two ADRs link to each other. The old one stays in the repository, so that a reader can follow how the decision changed.

Apart from the Status section, edit an accepted ADR only to correct it without changing the decision: fix a typo or a broken link, or replace a `TODO:` line with the missing fact.

### Reviewing docs

Docs are reviewed in the pull request, together with the code and by the same reviewers. The reviewer checks that:

1. Every doc that [the table](#if-you-change-this-update-that) names for this change is updated. If the pull request says that no doc is affected, check that this is true.
2. Each changed doc matches the code in the pull request: names, paths, values and defaults are the same, and commands work when copied.
3. No other doc is made wrong. Search the docs for the names that the pull request changes or removes.
4. A new document is in the right location, follows the format, and is in the index.
5. Unknown information is marked `TODO:` and not guessed. A `TODO:` that the pull request resolves is removed.

The docs have the same owners as the code: the code owners in `.github/CODEOWNERS`. No owner is set yet. See the TODO in [Code review](#code-review).

### Company style guide

TODO: add the link to the company-wide documentation style guide. Where it differs from the rules above, say which one applies.
