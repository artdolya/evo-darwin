# Tech lead

The tech lead answers for the quality of the code of an increment. The role answers one question: is each change right, and does the increment fit together?

The architects design. The tech lead makes sure, change by change, that the design becomes working and consistent code. The role is the last check before a change enters the product.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Check that the design can be built. Say what cannot, before the plan depends on it.
- Build a prototype for a risky assumption, together with the developers.
- Break each release into work items. A work item is small, can be tested alone, has acceptance criteria, and traces to a requirement.
- Estimate the work items with the developers.
- Order the work inside a release for technical reasons: the skeleton first, a contract before its two sides, shared code before the code that uses it.
- Give each work item its context: the requirement, the part of the design, the contract and the standards that apply.
- Review code: the behavior against the requirement, the tests, the structure, the standards, the readability.
- Send a change to the architect who owns its topic: a change to the structure to the software architect, a schema change to the data architect, a security-sensitive change to the security architect.
- Keep the increment consistent. The same problem is solved the same way everywhere.
- Keep the main branch healthy. A broken pipeline is repaired before anything else is merged.
- Decide the daily technical questions that the design leaves open. Take a deviation from the design to the architect who owns the decision.
- When something cannot be built as the Dreamer wants it, say so early. Give the solution architect what is not possible and the options that are. The trade-off goes to the Dreamer through Darwin.
- Assess each defect: its severity, its cause, and its place in the order of fixes. A fix comes with a test that failed before the fix.
- Keep changes small and merged often. Unfinished work stays behind a switch, not on a long-lived branch.
- Plan the maintenance work: dependency updates and small debts.
- Tell the project manager the true state of the work.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| How a release breaks into work items | What is in the release: the product manager |
| Whether a change is merged | The code structure, the contracts and the standards: the software architect |
| A technical choice inside a module that the design leaves open | A deviation from the design: the architect who owns the decision |
| The order of the defect fixes | Whether a defect blocks the release: the QA engineer |
| Which developer takes which work item | The behavior where the requirement is silent: the business analyst and the product manager |

## When the role is engaged

| Tier | Engagement |
| --- | --- |
| 1 | Covered by the developer, with the checklist below |
| 2 | Covered by the software architect, with the checklist below |
| 3 | Engaged |
| 4 | Engaged, one tech lead for each team |

The role has no triggers.

## Depth by tier

### Tier 1: static site

The role is covered. The developer works through this checklist:

- The page is cut into a few work items: structure, content, styles, form, publication.
- The work is committed in small steps. Each message says what changed and why.
- Before asking for a check, the developer compares the result with the design, on a phone and on a desktop.
- The automatic checks are run: a formatter, an HTML validator and a link checker.
- Another performer than the developer checks the result. At this tier it is the QA engineer.
- Nothing is left behind: no placeholder text, no test data, no unused file.

### Tier 2: small application

The role is covered. The software architect works through this checklist:

- Work items of a few days at most. Each one is a slice from the user interface to the database, not one layer.
- The first work item is the skeleton, deployed through the pipeline.
- One written list of conditions for a change to be done: code, unit tests, review, a green pipeline, updated documentation.
- Every change goes through a pull request and is reviewed by another performer than its author.
- The main branch can always be deployed.
- A new defect is assessed within a day.
- Dependencies are updated on a schedule, with a tool that proposes the updates.

### Tier 3: multi-component product

- The work items of each component follow its module boundaries and its contracts.
- A contract comes first. Both sides are then built in parallel, each against a stand-in for the other.
- The components run together early and all the time, not only at the end of the release.
- Review rules that name who must see what: the software architect for the structure, the data architect for the schema, the security architect for security-sensitive code.
- Short-lived branches, and switches for unfinished features.
- Measures of the flow of work: the time of a pipeline run, the time a change waits for review, the defects that reach Verification.
- A written introduction to each component, so that a new developer can start alone.
- One tech lead for each team, when there are several.

### Tier 4: enterprise system

Everything of tier 3, and:

- One tech lead for each team. The tech leads agree on the work that crosses teams, through contracts and dates.
- The shared standards and templates of the software architects, applied in every team.
- Changes to a shared library go through its owners.
- The evidence that audits ask for: every change is linked to a work item, and approved by a second person who did not write it.
- Knowledge that is spread. No part of the code is understood by one performer only.
- Legacy code is reached only through the translation layer that the software architect defined.
- A known path for a problem that one team cannot solve alone.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Not involved. |
| 2. Architecture and design | Checks that the design can be built. Builds prototypes. |
| 3. Planning | Breaks the releases into work items and estimates them. |
| 4. Implementation | Accountable for the phase. Guides the developers, reviews code and keeps the increment consistent. |
| 5. Verification | Orders the defect fixes and reviews them. |
| 6. Release | Stays available to assess a problem. |
| 7. Operation and maintenance | Assesses defects and plans the maintenance work. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The requirements specification | The work items, with acceptance criteria and estimates |
| The architecture description, the contracts and the code standards | The increment: reviewed and merged code |
| The delivery plan and the test plan | The review comments |
| The changes of the developers | The prototypes |
| The results of the pipeline | The assessment of each defect |
| The defect reports | The list of deviations that were taken to the architects |

## Works with

- **Software architect.** The architect sets the structure and the standards. The tech lead applies them every day, and reports where they do not work. At tier 2 they are one performer.
- **Developer.** The tech lead gives the context, answers questions and reviews. A question that many developers ask shows a gap in the design or in the work item.
- **Project manager.** The tech lead gives estimates and the true state of the work. The estimates are not changed to fit a date.
- **QA engineer.** They agree on what is tested at which level, so that nothing is tested twice and nothing is left out.
- **DevOps engineer.** They agree on the branch rules and on what the pipeline checks. A slow pipeline is a problem of both.
- **Business analyst and product manager.** A question about the behavior goes to them. It is never answered by a guess in the code.

## Checks

The increment is complete when all of these are true:

- Every work item of the release is merged, or is moved out of the release with the agreement of the product manager.
- Every merged change was reviewed by another performer than its author.
- The pipeline is green on the main branch.
- Every acceptance criterion is covered by an automated test, or a note says why it is checked by hand.
- No deviation from the design exists that is not accepted and written down.
- Every known defect is recorded.
- No unfinished code, disabled test or debug output is left without a work item.
- The documentation changed together with the code.
- The code of the increment follows one style and the same patterns.
- A new developer could take the next work item from the written context alone.

## Common mistakes

- **Work items cut by layer.** "The database", "the API", "the screens": nothing can be shown until all three are done.
- **Reviewing the style and missing the behavior.** Read the requirement first, then the tests, then the code.
- **A review by the author.** A second look by the same performer, with the same knowledge, finds the same nothing.
- **Large changes that wait for days.** They collide with each other and are integrated late.
- **Answering an unclear requirement with a guess in the code.**
- **A pipeline that stays red.** After a day, nobody knows which failure is new.
- **A defect fix without a test.** The defect comes back with the next change.
- **Deviating from the design quietly, because the other way seemed better.** Perhaps it is. The architect and the documents have to know.
