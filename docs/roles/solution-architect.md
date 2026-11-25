# Solution architect

The solution architect turns the requirements into the design of the whole solution. The role answers one question: which parts does the solution have, how do they work together, and why this way?

The role answers for the fit of the solution as a whole. The solution meets the functional requirements and the quality targets, inside the constraints and the budget of the Dreamer. The other architect roles go deep in one area each. The solution architect keeps the areas consistent.

The role is engaged on every project. The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Set the [tier](../SDLC.md#project-tiers) of the project and record the reasons. Raise the tier when the project outgrows it.
- Give the input for the reality score of [DreamContext](../dream-context.md): whether the Dream can be built with the technology and the knowledge that exist today.
- Decide which architect roles are engaged. Do the work of the roles that are not engaged.
- Find the requirements that shape the architecture: the quality attributes with their targets, the constraints, and the integrations.
- Divide the solution into components. Give each component one responsibility. Define the interfaces between the components and to the external systems.
- Decide for each part whether it is built, bought as a service, or reused from open source.
- Choose the technology of the solution as a whole, together with the software architect and the infrastructure architect.
- Where a choice changes the cost, the vendor or the scope, compare the options and prepare the choice for the Dreamer. [Darwin](darwin.md) presents it in plain words.
- Estimate the cost of building and the cost of running, each as a range with its assumptions.
- Record each significant decision in an ADR: the options, the choice and the reason.
- Join the work of the other architects into one consistent design. Settle the conflicts between them.
- Find the technical risks. Plan a prototype for each assumption that the design depends on and nobody has tested.
- Decide whether the code of a [demo](../SDLC.md#demos) from Discovery is kept or thrown away. A demo is built to be seen, not to be operated.
- During Implementation and Verification, check that the built solution matches the design. Decide on each deviation: accept it, or change the design.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| The tier, and the architect roles that are engaged | The scope and the priorities: the product manager and the Dreamer |
| The components and the boundaries between them | The structure of the code inside a component: the software architect |
| The style of each interface between components: a call that waits for the answer, or a message | The data model: the data architect |
| What is built, bought or reused | The hosting and the environments: the infrastructure architect |
| The technology of the solution as a whole | The security controls: the security architect |
| The trade-offs between quality targets | An option that changes the cost, the vendor or the scope: the Dreamer |
| A deviation from the design that crosses components | The acceptance of a security risk: the Dreamer |
| Whether the code of a demo is kept | A change to a point that the Dreamer confirmed: the Dreamer |

The full list of owners is in [Who decides what](README.md#who-decides-what).

## When the role is engaged

The role is engaged at every tier, from Discovery to Operation and maintenance. It has no triggers.

The role also covers other architect roles:

| Tier | Roles that the solution architect covers |
| --- | --- |
| 1 | Software architect, data architect, infrastructure architect, security architect, AI architect |
| 2 | Infrastructure architect, AI architect |
| 3 and 4 | None |

The AI architect has work only when the solution itself uses AI.

To cover a role, the solution architect works through the checklist for that tier in the document of the role. When a trigger in that document fires, the solution architect engages the role.

## Depth by tier

### Tier 1: static site

The output is a note of about half a page. It has no diagram.

- How the site is built: plain HTML and CSS, a static site generator, or a site builder. Take the simplest one that gives the wanted look.
- Where the site is hosted, and what the hosting costs.
- The domain: who registers it, who owns the account, how HTTPS is provided.
- How the content is updated, and by whom.
- Each third-party embed, such as a form, a map or analytics: the service, the reason, the cost, and what the site shows when the service is down.
- The tier 1 checklists of the [software architect](software-architect.md#tier-1-static-site), the [data architect](data-architect.md#tier-1-static-site), the [infrastructure architect](infrastructure-architect.md#tier-1-static-site) and the [security architect](security-architect.md#tier-1-static-site).
- When the site uses AI: the [tier 1 checklist of the AI architect](ai-architect.md#tier-1-static-site).

Write an ADR only for a choice that is not obvious.

### Tier 2: small application

The output is an architecture description of a few pages.

- The context: the kinds of users and the external systems.
- One diagram that shows the users, the application, the database and the external services.
- The application as one deployable with one database. A second deployable needs a requirement that one deployable cannot meet.
- The technology stack, and the reason for it.
- How users sign in: the identity provider or the library. The security architect designs the details.
- Each external service: what it does, what it costs, and what happens when it is down.
- The hosting model, from the [tier 2 checklist of the infrastructure architect](infrastructure-architect.md#tier-2-small-application).
- When the application uses AI: each use of a model, from the [tier 2 checklist of the AI architect](ai-architect.md#tier-2-small-application).
- The quality attributes that apply, each with a target and with the way the design meets it.
- The cost ranges for building and for running.
- ADRs for the stack, for the hosting, and for each choice that was put to the Dreamer.

### Tier 3: multi-component product

The output is a full architecture description. The parts of the other architects are separate documents that it links to.

- A context diagram and a container diagram, as in levels 1 and 2 of the C4 model.
- The components: the responsibility of each one, the data it owns, and its interfaces.
- The main scenarios at run time as sequence diagrams, including what happens when a component or an external system fails.
- For each quality attribute: a scenario with a measured target, and the mechanism that meets it.
- For each interface between components: the style, the contract, and the behavior on failure. The software architect details the contract.
- An ADR for each significant decision.
- A risk list. Each technical risk has an owner and a way to retire it: a prototype, a test, or an early work item.
- A cost model: the cost of building by component, and the cost of running by environment and by load.
- The growth path: which part changes first when the load grows ten times.

### Tier 4: enterprise system

Everything of tier 3, and:

- The fit with the organization: its existing systems, its technology standards, and its identity system. Each deviation from a standard has a reason and an approval.
- The integrations with the existing systems: the owner of each system, the contract, the volumes, and the service levels.
- The transition: the steps from the current state to the target state, and how the old system and the new one run side by side in each step.
- Boundaries between domains that match the boundaries between teams, so that one team can change its part without the others.
- The trace from each requirement to the components that implement it, as audits need it.
- The mapping of the compliance requirements to the components, together with the security architect.
- A review of the architecture by the architecture board of the organization.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Sets the tier and names the engaged architect roles. Collects the quality attributes and gives each one a target. Records the constraints and the integrations. Checks that each requirement is feasible, and tells Darwin early when the Dream is not feasible or costs far more than the Dreamer expects. Gives the input for the reality score. |
| 2. Architecture and design | Accountable for the phase. Designs the solution. Joins the parts of the other architects. Prepares the options and the cost for the Dreamer. Decides whether the code of a demo is kept. Leads the design review. Gives Darwin every gap that the design finds in DreamContext. |
| 3. Planning | Advises on the order of the work: first a thin slice through all components that can be deployed, then the highest technical risk. Names the dependencies between components. |
| 4. Implementation | Answers design questions. Reviews changes that cross component boundaries. Decides on deviations. Keeps the architecture description and the ADRs current. |
| 5. Verification | Checks that every quality target was tested and met. |
| 6. Release | Confirms that the deployed solution is the accepted design. |
| 7. Operation and maintenance | Reviews incidents and metrics for causes in the design. Reviews the tier when the product grows. Plans how the architecture evolves. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The idea brief | The tier, with its reasons |
| The requirements specification | The list of engaged architect roles, and the input for the reality score |
| The constraints of the Dreamer: budget, deadline, required technology | The architecture description: solution design |
| The parts of the other architects | The ADRs of the decisions the role owns |
| The test report | The cost estimate |
| The incident reports and the metrics | The risk list |

## Works with

- **Darwin.** Every question and every option for the Dreamer goes through Darwin. The solution architect gives Darwin the options with their cost and their consequence, written so that Darwin can put them in plain words.
- **Product manager and business analyst.** They own what is built. The solution architect owns how. When a requirement costs far more than its value, the solution architect says so with the cost, and the Dreamer decides.
- **Software architect.** The solution architect draws the boundaries between components. The software architect owns the inside of each component and details the contracts.
- **Data architect.** The solution architect decides which component owns which data. The data architect decides how the data is modeled and stored.
- **Infrastructure architect.** The solution architect states the components and the quality targets. The infrastructure architect decides where and how the components run to meet the targets.
- **Security architect.** The security architect sets the controls. The solution architect fits them into the design, and cannot waive a minimum control.
- **AI architect.** The solution architect decides which components exist and what is bought. The AI architect designs each use of a model inside them. At tiers 1 and 2 the solution architect does both.
- **Tech lead.** The tech lead says whether the team can build the design, and reports where the code has to deviate from it.

## Checks

The output of the role is complete when all of these are true:

- The tier is recorded with its reasons.
- Every functional requirement maps to at least one component.
- Every component traces to at least one requirement.
- Every quality attribute has a target and a named mechanism that meets it.
- Every external dependency is named, with its reason, its cost, and the behavior of the solution when it is down.
- Every significant decision has an ADR that names the options that were considered.
- The simplest design that could meet the requirements was considered. If it was rejected, the ADR names the requirement it does not meet.
- The cost of building and the cost of running are stated as ranges with their assumptions.
- The parts of the other architects do not contradict each other or the solution design.
- A developer can start from the documents alone.

## Common mistakes

- **Designing for a higher tier than the project has.** Several services, a message bus and a container platform for a booking form. Every component costs money to build, to run and to understand.
- **Choosing the technology before the quality targets are known.** The stack then decides the architecture, and not the requirements.
- **Leaving a quality attribute without a number.** "Fast" and "secure" cannot be designed for and cannot be tested.
- **Hiding a trade-off from the Dreamer.** A choice that changes the cost or ties the Dreamer to a vendor belongs to the Dreamer.
- **Designing only the case where everything works.** The behavior when an external service is down is part of the design.
- **Letting the description go stale.** A deviation that is accepted in Implementation and not written down makes the architecture description wrong for every later reader.
