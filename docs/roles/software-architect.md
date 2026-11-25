# Software architect

The software architect designs the inside of the software. The role answers one question: how is the code structured, and which rules does every developer follow?

The role answers for code that stays correct, testable and cheap to change. The solution architect decides which components exist. The software architect decides how each component is built: its modules, its contracts, its frameworks and its standards.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Choose the structure of each component: its layers or modules, and the responsibility of each one.
- Define which module may depend on which. Choose how the rule is enforced: by project references, by a lint rule, or by a test.
- Choose the languages, the frameworks and the main libraries of each component, inside the technology that the solution architect chose.
- Design the contracts: the endpoints of each API with their request and response types, the error model, the versioning, and the messages between components.
- Define one approach for each concern that crosses the modules: error handling, validation, logging, configuration, transactions, caching, concurrency, and text in several languages.
- Define how the code is tested: what is covered by unit tests, by integration tests and by contract tests.
- Set the code standards: naming, formatting, project layout, and the conditions for a change to be done.
- Define the skeleton of each component: the empty structure that builds, runs its tests and deploys. It is the first work item.
- Set the rules for third-party dependencies: license, maintenance, and who approves a new one.
- Review changes to the structure, the contracts and the dependencies.
- Record the technical debt and plan its payment.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| The structure of the code inside a component | Which components exist, and their boundaries: the solution architect |
| The frameworks and the main libraries | The platform and the main languages of the solution: the solution architect |
| The API contracts and the message contracts | Which component owns which data: the solution architect |
| The patterns for the concerns that cross the modules | The data model and the type of data store: the data architect |
| The code standards and the test approach | How users are authenticated and authorized: the security architect |
| Whether a new third-party dependency is accepted | The pipeline and the environments: the infrastructure architect |

The full list of owners is in [Who decides what](README.md#who-decides-what).

## When the role is engaged

| Tier | Engagement |
| --- | --- |
| 1 | Covered by the solution architect, with the checklist below |
| 2 | Engaged. Also does the work of the tech lead, and covers the data architect. |
| 3 | Engaged |
| 4 | Engaged, one software architect for each domain |

Triggers that engage the role at tier 1:

- The site has logic of its own in the browser, for example a price calculator or a product configurator.
- The content comes from a content management system or from an API at build time.
- The site has more than one language, or more than a few page templates.

## Depth by tier

### Tier 1: static site

The role is covered. The solution architect works through this checklist:

- One folder layout for pages, styles, scripts and images.
- One command that builds the site, or no build at all.
- No framework, unless a requirement needs one.
- Valid HTML that keeps its meaning without CSS: headings in order, labels on form fields, alternative text on images.
- A formatter with its default settings.

### Tier 2: small application

The output is a short document on the code structure.

- The stack with its versions.
- The project layout and the layers. Which layer may depend on which.
- One deployable. The modules inside it are folders or projects, not services.
- The style of the API, one error model for all endpoints, and the validation of input.
- How authentication plugs into the code. The security architect designs it.
- The test approach: what is unit-tested, what is integration-tested, and how the tests get a database.
- The code standards. Take the defaults of the framework and of the formatter. Write down only the deviations.
- The data model of the one database, with the [tier 2 checklist of the data architect](data-architect.md#tier-2-small-application).
- The work of the tech lead, with the [tier 2 checklist of the tech lead](tech-lead.md#tier-2-small-application).

### Tier 3: multi-component product

The output is one document on the code structure for each component, and the contracts.

- The modules of each component and the allowed dependencies, enforced by a tool in the pipeline.
- The API contracts in a machine-readable form, such as OpenAPI for HTTP and AsyncAPI for messages. A contract is agreed before either side is implemented, so that the sides can be built in parallel.
- The rules for changing a contract: what counts as a compatible change, how a version is retired.
- The messaging patterns: a consumer gives the same result when a message arrives twice, failed messages are retried and then set aside, and a message is published in the same transaction as the data change it reports.
- The policy for shared code: what goes into a shared library, who owns it, how it is versioned.
- The tests of each component, including the contract tests between components.
- The performance budget of each main operation, taken from the quality targets.
- The technical debt register.

### Tier 4: enterprise system

Everything of tier 3, and:

- A reference structure and a project template that every team starts from.
- The domains, their boundaries and the relations between them. A translation layer in front of each legacy system, so that its model does not leak into the new code.
- Rules that the pipeline checks automatically in every team: dependency rules, contract compatibility, test coverage of the critical paths.
- The governance of the APIs: one style guide, a review of each new API, and a policy for retiring an API.
- The platform libraries that all teams share, with an owner and a release process.
- The upgrade policy: how fast each team follows new versions of the frameworks.
- The coordination of the software architects of the domains: where they decide together and where each decides alone.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Names the requirements that shape the code structure, such as offline use, several tenants, several languages, or extension by third parties. |
| 2. Architecture and design | Designs the code structure, the contracts and the standards. Reviews the solution design for what it means for the code. |
| 3. Planning | Aligns the work items with the module boundaries and the contracts, so that work can run in parallel. Puts the skeleton first. |
| 4. Implementation | Reviews changes to the structure, the contracts and the dependencies. Answers questions. Keeps the documents current. |
| 5. Verification | Checks that the architecture rules hold in the code: the dependencies, the contracts, the tests of each layer. |
| 6. Release | Confirms that the release keeps the contracts compatible with the clients that are in use. |
| 7. Operation and maintenance | Tracks the technical debt. Plans the upgrades of the frameworks. Reviews defects for causes in the structure. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The requirements specification | The architecture description: code structure |
| The solution design | The API contracts and the message contracts |
| The data model | The code standards and the test approach |
| The security controls | The skeleton of each component, as a specification or as code |
| The code and the review comments | The ADRs of the decisions the role owns |
| The defects | The technical debt register |

## Works with

- **Solution architect.** The solution architect gives the components and their boundaries. The software architect reports when a boundary makes the code harder than it should be.
- **Data architect.** The data architect owns the schema. The software architect owns the code that reads and writes it. They agree on the mapping between the two. At tier 2 the software architect does both.
- **Security architect.** The security architect designs authentication, authorization and input handling as rules. The software architect puts them into the structure, so that a developer cannot skip them by accident.
- **Infrastructure architect.** They agree on what the code emits for logs, metrics and traces, how it reads its configuration, and how it starts and stops.
- **AI architect.** They agree on where the calls to a model live in the code, and on a fixed format for the output of a model, so that the rest of the code does not depend on free text.
- **Tech lead.** The tech lead applies the structure every day and reviews most changes. The software architect reviews the changes that alter the structure. At tier 2 they are one performer.
- **Developer.** A rule that developers keep breaking is a sign that the structure is wrong, or that the rule is not enforced by a tool.

## Checks

The output of the role is complete when all of these are true:

- Every module has one stated responsibility.
- The allowed dependencies between modules are written down, and a tool checks them.
- Every interface between components has a contract that both sides can test against.
- Every endpoint uses the same error model.
- Each concern that crosses the modules has exactly one approach.
- The test approach says for each layer what is tested and how.
- Every framework and main library has a reason and a version.
- A developer who is new to the project can place a new piece of code without asking.
- Nothing in the structure exists only for a requirement that nobody has stated.

## Common mistakes

- **Layers and abstractions for a future that nobody asked for.** An interface with one implementation, a layer that only passes calls on. Each one is code to read and to maintain.
- **Rules that only reviewers enforce.** A rule that no tool checks is broken within weeks.
- **Contracts that are written after the code.** Two sides that are built before the contract exists do not fit, and the mismatch is found in Verification.
- **A different pattern in every module.** The value of a pattern is that the next module looks the same.
- **Choosing a framework because it is new.** A framework is chosen for a requirement, for its maintenance and for the knowledge of those who build with it.
- **Splitting into services to get modularity.** A module boundary inside one deployable gives the same separation without the network between the parts.
