# Project manager

The project manager answers for the plan and its progress. The role answers one question: in which order is the work done, where does it stand, and what threatens it?

The role manages the plan, the dependencies, the risks and the flow of decisions. It does not decide what is built or how. It makes sure that everyone knows the true state of the project. The Dreamer learns it from [Darwin](darwin.md), who gets it from the project manager.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Build the delivery plan from the approved scope and the design: the releases, the work items, the order and the dependencies.
- Make each release end with something that the Dreamer can see working.
- Find the dependencies: between work items, on the Dreamer, and on third parties.
- Start early what has a waiting time outside the project: the registration or transfer of a domain, the verification of a payment account, the review of an app by an app store.
- Keep the risk list. Each risk has a likelihood, an effect, an owner and a response.
- Track the progress from evidence: merged work items and passed tests, not statements.
- Remove blockers. Send each question to the role that owns the answer.
- Track what the project needs from the Dreamer: content, access and decisions, each with a date. Give the list to Darwin.
- Give Darwin the status for the Dreamer, in the same form every time: what is done, what comes next, what is at risk, and what the Dreamer has to do.
- Track the cost against the approved range. Say early when the range will not hold.
- Handle changes. A change to the approved scope or plan goes to the product manager, and through Darwin to the Dreamer, with its effect on the date and the cost.
- Coordinate the go or no-go decision of a release: collect the confirmations of the roles and give them to Darwin, who asks the Dreamer for go-live.
- Keep the record of the gates: who approved what, on which version, and when.
- Close each release: what was planned, what was delivered, and what to do differently.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| The structure of the plan, and the order of the work inside the priorities and the technical advice | What is in a release: the product manager and the Dreamer |
| When a risk or a blocker goes to Darwin for the Dreamer | How the work is built: the architects and the tech lead |
| The form and the rhythm of the status report | An estimate: the tech lead and the developers. The project manager does not change it. |
| Whether the conditions of a gate are met, so that the Dreamer can be asked | The approval at a gate: the Dreamer |
| | Whether a test passed, or a finding blocks: the QA engineer and the security architect |

## When the role is engaged

| Tier | Engagement |
| --- | --- |
| 1 | Covered by the product manager, with the checklist below |
| 2 | Engaged |
| 3 | Engaged |
| 4 | Engaged, with one plan across the teams |

Triggers that engage the role at tier 1:

- A fixed date, such as an event, an opening or a campaign.
- The work depends on deliveries of third parties, such as a photographer, a translator, or the previous owner of the domain.

## Depth by tier

### Tier 1: static site

The role is covered. The product manager works through this checklist:

- One list of work items, in order.
- What the Dreamer provides, and by when: texts, photos, the logo, access to the domain.
- The things with a waiting time are started first: the registration or the transfer of the domain, and the DNS change.
- The date of the demo of the finished site and the date of the publication.
- Who is told when the site is live.

### Tier 2: small application

- A plan of a few releases. Each release has a goal, its work items and their order.
- The first release starts with a thin slice through the whole application that is deployed.
- The dependencies, with the accounts that take time to open: the payment provider, the e-mail domain, the app stores.
- A short risk list with the five risks that matter most.
- A status report after each release, or every week.
- The cost tracked against the approved range.
- The record of the gates.

### Tier 3: multi-component product

- A release plan with a workstream for each component or team.
- The dependencies between the workstreams, each with the contract that lets both sides work in parallel.
- The points where the components first run together. They are early in the plan, not at its end.
- A risk register with owners and a regular review.
- A status report with measures: scope done, open defects, cost used.
- A change log of the scope.
- A calendar of the external dependencies.
- A go or no-go checklist for each release.

### Tier 4: enterprise system

Everything of tier 3, and:

- One plan across all teams, with the dependencies between them.
- The governance of the organization: a steering group, and a fixed rhythm of reports to it.
- The dependencies on other projects and departments of the organization.
- The change control of the organization: release windows, and approvals that need lead time.
- The people of the organization that the project needs: experts of the business, and users for the tests. Their time is planned.
- A cut-over plan for the migration: rehearsals, a schedule by the hour, and the points where the decision to go back is still possible.
- A plan for training and communication, together with the product manager.
- The budget reported in the form of the organization.
- Formal acceptance documents.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Informed. Learns the scope and the limits: the budget and the deadline. |
| 2. Architecture and design | Informed. Learns the design, the cost range and the risks. |
| 3. Planning | Accountable for the phase. Builds the plan. Tracks the dependencies and the risks. Gives Darwin the plan to present to the Dreamer. |
| 4. Implementation | Tracks the progress and removes blockers. Gives Darwin the status. |
| 5. Verification | Informed. Learns the test results and the answer of the Dreamer. Changes the plan when defects move work. |
| 6. Release | Coordinates the go or no-go decision of the roles. Gives Darwin the result for the Dreamer. |
| 7. Operation and maintenance | Informed. A new release starts a new plan. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The approved scope and the priorities | The delivery plan |
| The architecture description, the cost estimate and the risk list | The updated risk list |
| The work items and the estimates of the tech lead | The status reports |
| The test plan | The record of the gates |
| The state of the work items, and the test results | The change log |
| The decisions of the Dreamer | The go or no-go summary, and the closing note of each release |

## Works with

- **Product manager.** The product manager says what comes first by value. The project manager says when it can be done, and what it moves. At tier 1 they are one performer.
- **Tech lead.** The tech lead breaks the work down and estimates it. The project manager plans with those estimates and does not change them.
- **Solution architect.** The architect advises on the order by technical risk and names the dependencies between components.
- **QA engineer.** The test plan is part of the plan. Verification has its own time, not the time that is left over.
- **DevOps engineer.** The environments are ready before the work that needs them. The steps of a release are in the plan.
- **Darwin.** Darwin tells the Dreamer the state of the project and what the project is waiting for. Both come from the project manager.

## Checks

The output of the role is complete when all of these are true:

- Every requirement of the release is covered by at least one work item.
- Every work item traces to a requirement, or is named as enabling work, such as the skeleton or the pipeline.
- Every work item has acceptance criteria and an estimate, and is small enough to build, to check and to show.
- Every release ends with something that the Dreamer can see.
- The thin end-to-end slice is first. The highest technical risk comes next.
- Every dependency has an owner and a date. The things with a waiting time are started early.
- Every risk has an owner and a response.
- Verification and Release have time of their own in the plan.
- What the Dreamer has to provide and to decide is listed with dates.
- The status report states facts with their evidence, and says what is at risk.
- Every decision at a gate is recorded with its version.

## Common mistakes

- **Progress from statements.** "Ninety percent done" is not a state. A work item is done, or it is not.
- **A plan where everything meets at the end.** The components run together for the first time a week before the release, and do not fit.
- **Forgetting the waiting times outside the project.** The site is ready, and the domain transfer takes five more days.
- **Taking the time from Verification when Implementation is late.**
- **Hiding a delay until the gate.** The Dreamer can react to a delay that is known early.
- **Changing an estimate to fit the date.** The work does not get smaller.
- **Tracking the work and not the decisions.** The project waits a week for an answer of the Dreamer, who did not know that anyone was waiting.
- **More plan than the tier needs.** A one-page site needs a list, not a schedule with phases and milestones.
