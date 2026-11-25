# Business analyst

The business analyst turns what the Dreamer said into requirements that are precise enough to design, to build and to test. The role answers one question: what exactly must the solution do, and how can anyone check it?

The role answers for requirements that are complete, unambiguous, testable, and traced to the idea. It does not decide what the product should do. It makes sure that what was decided is written so that two readers understand the same thing.

The requirements specification is a part of [DreamContext](../dream-context.md). The business analyst does not talk to the Dreamer: it gives its questions to [Darwin](darwin.md).

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Read DreamContext and the record of the conversation. Check the [status](../dream-context.md#status-of-a-point) of every point: did the Dreamer confirm it, or did a role assume it?
- Find the contradictions, the gaps and the words with two meanings. Give each one to Darwin as an open point, with what it blocks. The open points are what the readiness score counts.
- Write the functional requirements: one behavior in each, in plain language.
- Write the acceptance criteria of each requirement, in a form that can be tested: Given, When, Then.
- Write a BDD scenario for each confirmed point that can be observed in the product, as soon as Darwin records the confirmation. Link it to the words of the Dreamer. Change it only when the Dreamer changes the point.
- Write down the business rules: calculations, conditions, limits, and the states that a thing passes through.
- Describe what happens when something goes wrong: an input that is wrong, missing, late or sent twice, and an action that a person is not allowed to do.
- Write down who may do what: the kinds of users and the permissions of each.
- Put the quality attributes that the architects collect into the same document, each with its target.
- Keep the glossary, together with the data architect. One word has one meaning.
- Keep the trace: from each requirement back to the idea brief, and forward to the work items and the tests.
- When the solution replaces an existing process or system, describe how that one works today.
- Keep the requirements current. A change gets a new version, a mark that shows what changed, and a message to the roles that depend on it.
- Answer the questions of the later phases. When the specification has no answer, give the question to Darwin. Then add the answer to the specification.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| The wording and the structure of the requirements | What is in the scope, and in which priority: the product manager and the Dreamer |
| The wording of the acceptance criteria and of the BDD scenarios | A business rule that the Dreamer has not stated: the Dreamer |
| Whether a requirement is ready: clear, testable and traced | The quality targets: the solution architect proposes them, the Dreamer approves them |
| The terms of the glossary, taken from the words of the Dreamer | How a requirement is implemented: the architects and the developers |
| | How a screen looks: the UX designer |
| | Whether a point is confirmed: the Dreamer. Darwin records it. |

## When the role is engaged

| Tier | Engagement |
| --- | --- |
| 1 | Covered by the product manager, with the checklist below |
| 2 | Covered by the product manager, with the checklist below |
| 3 | Engaged |
| 4 | Engaged, several business analysts, one for each domain |

Triggers that engage the role at tier 1 or 2:

- The domain has rules that take more than a conversation to collect, such as prices with many conditions, tax, insurance, payroll or medical rules.
- The solution replaces an existing process or system, and its behavior has to be described first.
- Groups of intended users have needs that conflict.
- An external party prescribes requirements, such as a regulator, a partner or a marketplace.

## Depth by tier

### Tier 1: static site

The role is covered. The product manager works through this checklist:

- The list of pages and sections. For each one: its purpose, and where its content comes from.
- For each form: its fields, where the data goes, and what the visitor sees after sending it.
- One source for each fact that appears more than once: the name of the business, prices, opening hours, the address.
- What "done" means, as checks that the Dreamer can make: the links work, the page reads well on a phone, the texts are right.
- One check for each point that the Dreamer confirmed after a demo.

### Tier 2: small application

The role is covered, unless a trigger engages it. The product manager works through this checklist:

- The user journeys, as numbered steps.
- Numbered functional requirements, one behavior in each, each marked as first release or later.
- Acceptance criteria for each requirement, with at least one case where something goes wrong.
- A BDD scenario for each confirmed point.
- The kinds of users, and a table of what each kind may do.
- The business rules, as a list.
- The states of the main things, for example of an order or a booking, and what moves a thing from one state to the next.
- A small glossary.
- The trace from each requirement to the idea brief.

### Tier 3: multi-component product

The output is the requirements specification as a document of its own, kept current through the whole project.

- The requirements grouped by capability. Each one has an identifier, a source, a status, a priority, a release and acceptance criteria.
- A BDD scenario for each confirmed point, with the date of the confirmation.
- A catalog of the business rules.
- A state model for each main entity.
- The permission matrix: each kind of user against each action.
- The requirements of each integration: which data, in which direction, when, and what happens on an error.
- The quality attributes of the architects, each with its target and the way it is measured.
- The data requirements, together with the data architect.
- The exceptions and the edge cases of each capability.
- The trace from the idea, through the requirement and the work item, to the test.
- A change log of the requirements.

### Tier 4: enterprise system

Everything of tier 3, and:

- A description of the processes and systems as they are today, of the target, and of the differences between the two.
- The requirements of each domain, with a business owner who signs them.
- The regulations mapped to requirements, together with the security architect.
- The migration requirements: which data moves, how much history, and what the cut-over must guarantee.
- The reporting requirements of the organization.
- The requirements for training and rollout, together with the product manager.
- A formal change process: a change after the sign-off gets an analysis of its effect before it is decided.
- A named decision-maker for a conflict between stakeholders.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Finds the gaps, the ambiguities and the contradictions, and gives them to Darwin as open points. Writes the requirements and the acceptance criteria. Traces each one to the words of the Dreamer. Writes a BDD scenario for each confirmed point, also for a point that the Dreamer confirms after a later demo. Keeps the glossary. |
| 2. Architecture and design | Clarifies the requirements for the architects and the UX designer. Adds what their questions uncover. |
| 3. Planning | Clarifies the acceptance criteria of the work items. |
| 4. Implementation | Clarifies the requirements for the developers. A gap goes to Darwin as an open point. It is not filled with a guess. |
| 5. Verification | Clarifies the expected behavior when a test result is disputed. |
| 6. Release | Not involved. |
| 7. Operation and maintenance | Not involved. A new requirement from the feedback returns to Discovery. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| DreamContext: the idea brief and the record of the conversation | The requirements specification, a part of DreamContext |
| The documents of an existing process or system | The acceptance criteria, with the BDD scenarios of the confirmed points |
| Regulations and the specifications of external parties | The business rules, the state models and the permission table |
| The quality attributes of the architects | The glossary |
| The user journeys of the UX designer | The open points for Darwin: gaps, ambiguities, contradictions |
| The questions of the later phases | The trace and the change log |

## Works with

- **Darwin.** Darwin talks with the Dreamer. The business analyst says what is unclear and what it blocks. Darwin decides whether it becomes a question or a provisional point. Darwin tells the business analyst which points the Dreamer confirmed.
- **Product manager.** The product manager decides what is in the scope. The business analyst makes each item precise, and reports the items that cannot be made precise. At tiers 1 and 2 they are one performer.
- **UX designer.** Each step of a journey has a requirement behind it. Each requirement that a person can see has a place on a screen.
- **QA engineer.** The QA engineer checks that each acceptance criterion can be tested, and turns it into tests. The BDD scenarios of the confirmed points are automated first.
- **Solution architect.** The architect collects the quality attributes. The business analyst keeps them in the specification, with the same care as the functional requirements.
- **Data architect.** They keep one glossary. An entity in the data model has the name that the Dreamer uses for it.
- **AI architect.** A confirmed point about the behavior of a model becomes examples in an evaluation, because one exact scenario cannot check an answer that varies. The business analyst gives each example its expected result.
- **Tech lead and developer.** They ask when the behavior is unclear. A question that comes twice shows a gap in the specification.

## Checks

The output of the role is complete when all of these are true:

- Every requirement states one behavior and has an identifier.
- Every requirement traces to the idea brief.
- Every requirement has at least one acceptance criterion, and one for the failure case where one exists.
- No requirement uses a word such as "fast", "easy" or "user-friendly" without a number or an example.
- Every term has one meaning and is in the glossary.
- No requirement prescribes an implementation, unless it records a constraint of the Dreamer.
- No two requirements contradict each other.
- Every open point is with Darwin. None of them blocks the first release.
- Every point has a status. Every assumption of a role is provisional.
- Every confirmed point that can be observed in the product has a BDD scenario, linked to the words of the Dreamer.
- A tester can derive the tests from the document alone, and a developer can estimate the work.

## Common mistakes

- **Filling a gap with a plausible guess.** The guess reads like a requirement, and nobody asks the Dreamer. A gap is an open point for Darwin. It ends as an answer of the Dreamer or as a provisional point.
- **Marking a provisional point as confirmed.** Its scenario then defends a guess, and a later correction of the Dreamer looks like a defect.
- **Writing only the case where everything goes right.** Most of the code, and most of the defects, are in the other cases.
- **Describing screens and not behavior.** "A blue button in the corner" is a design. "A customer can cancel a booking until one hour before it starts" is a requirement.
- **Five behaviors in one requirement.** It cannot be tested as one, and it cannot be traced.
- **Changing a requirement silently.** The design, the work items and the tests still follow the old one.
- **Three words for one thing.** "Client", "customer" and "account" for the same person end as three tables.
- **Adding requirements because every such product has them.** Each one is a proposal to the product manager, not a part of the scope.
