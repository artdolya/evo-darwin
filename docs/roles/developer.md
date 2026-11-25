# Developer

The developer writes the code. The role answers one question: does this work item do what its acceptance criteria say, in the way the design prescribes?

The role has [specializations](README.md#specializations): frontend, backend, mobile and AI. At tiers 1 and 2 one developer works on all parts. From tier 3 the developers specialize. The AI specialization writes the prompts and the code around each call to a model, where the solution uses one.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Before writing, read the work item, the requirement behind it, the part of the design, the contract and the standards.
- Ask when something is unclear or contradicts something else. Do not guess.
- Write code that meets the acceptance criteria and follows the structure and the standards.
- Write the unit tests together with the code. Test the cases that fail, not only the case that works.
- Keep a change small: one work item, one purpose.
- Run the tests and the checks before asking for a review. Run the code itself, and see it work.
- Describe each change: what it does, why, and how it was tested. Link it to its work item.
- Review the changes of other developers.
- Fix defects: reproduce the defect, write a test that fails, fix the cause, and check that nothing else broke.
- Handle errors, validate input and write logs the way the standards say. Keep secrets and personal data out of the code and out of the logs.
- Update the documentation that the change affects.
- Report a deviation before making it. When the design cannot be followed, the architect who owns it decides.
- Estimate work items.
- Build the [demos](../SDLC.md#demos) of Discovery: a working preview of what was discussed, built fast. Give Darwin the list of the details that were the developer's own choice.
- Build prototypes. A prototype is thrown away. It does not become the product by staying. The code of a demo is kept only when the solution architect decides so.
- Where the solution uses a model: write each prompt inside the design of the [AI architect](ai-architect.md), keep it in version control, and run the examples of the evaluation before and after each change.
- Use only the accepted dependencies. Ask before adding a new one.
- Check each function of a library against its documentation for the version in use.
- Update dependencies and apply patches in Operation and maintenance.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| How the code of a work item is written, inside the structure and the standards | The behavior: the requirement. A gap is a question, not a choice. |
| The unit tests of the own code | The structure, a contract or a new dependency: the software architect |
| The names and the small design of functions and classes | The schema: the data architect, through a reviewed migration |
| The comments in the review of another developer's change | Whether the own change is merged: the reviewer |
| The wording of a prompt, inside the design of the AI architect | The model, and what the model may decide: the AI architect |
| | Whether the code of a demo is kept: the solution architect |
| | A change to a point that the Dreamer confirmed: the Dreamer |
| | Skipping a test or a check: nobody decides that alone |

## When the role is engaged

The role is engaged at every tier. It has no triggers.

| Tier | Engagement |
| --- | --- |
| 1 | Engaged, one developer. Covers the tech lead, the DevOps engineer, the site reliability engineer and the technical writer. |
| 2 | Engaged. Covers the technical writer. |
| 3 | Engaged, several developers by specialization |
| 4 | Engaged, several teams |

To cover a role, the developer works through the checklist for that tier in the document of the role. When a trigger in that document fires, the role is engaged.

## Depth by tier

### Tier 1: static site

- The page built from the design: HTML that carries the meaning, CSS for the look, and as little JavaScript as possible.
- The real content. No placeholder text.
- Images in the right size and format, each with a text alternative.
- A layout that works from the smallest phone to a wide desktop.
- The page title, the description, the icon, and the image that appears when the page is shared.
- The form connected to its service, and tested with a real submission.
- A check of the page weight and the loading time.
- No broken link.
- The tier 1 checklists of the [tech lead](tech-lead.md#tier-1-static-site), the [DevOps engineer](devops-engineer.md#tier-1-static-site), the [site reliability engineer](site-reliability-engineer.md#tier-1-static-site) and the [technical writer](technical-writer.md#tier-1-static-site).

### Tier 2: small application

- One work item is one slice, from the user interface to the database.
- The conventions of the framework, wherever the design does not say otherwise.
- Unit tests for the business rules. Integration tests for the endpoints, with a real database.
- A migration for every schema change.
- Input validated on the server, whatever the browser has already checked.
- A permission check on the server for every endpoint.
- Configuration read from the environment.
- Errors handled and logged in one way.
- Every change in a pull request, reviewed by another performer.
- The [tier 2 checklist of the technical writer](technical-writer.md#tier-2-small-application).

### Tier 3: multi-component product

- A specialization: frontend, backend, mobile or AI.
- Work against the contracts. Each side is built and tested against a stand-in for the other, and contract tests prove that the sides still fit.
- A message handler gives the same result when a message arrives twice.
- Changes that stay compatible: the old version and the new version run side by side during a deployment.
- Switches for unfinished features.
- Structured logs, metrics and trace identifiers, as the standards say.
- A time limit on every call to another component or service, and a limited number of retries.
- Performance measured against the budget of the operation, not guessed.
- For the frontend: the accessibility that the design asks for, built and checked.

### Tier 4: enterprise system

Everything of tier 3, and:

- Work inside the domain of the team. A change to another domain goes through its team.
- The templates and the platform libraries of the organization.
- Every change linked to a work item and approved by a second person, as audits ask for it.
- The secure coding standard of the organization.
- Legacy systems reached only through the translation layer.
- Data handled by its class. Real personal data is not used outside production.
- The knowledge of the domain written down, where the code alone does not explain it.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Builds the demos of what was discussed. |
| 2. Architecture and design | Builds prototypes for the assumptions that the architects want tested. |
| 3. Planning | Estimates work items. Says what a work item depends on. |
| 4. Implementation | Writes code and unit tests. Reviews the code of other developers. |
| 5. Verification | Fixes defects. |
| 6. Release | Stays available to fix a problem. |
| 7. Operation and maintenance | Fixes defects and updates dependencies. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The work item with its acceptance criteria | The code |
| The requirement behind the work item | The unit tests |
| The architecture description: code structure, contracts, data model | The description of each change |
| The user interface design | The updated documentation |
| The code standards | The review comments on the changes of others |
| The review comments and the defect reports | Estimates, prototypes, questions and reports of deviations |
| DreamContext, for a demo in Discovery | The demos, each with the list of the developer's own choices |

## Works with

- **Tech lead.** The tech lead gives the work item and its context, and reviews the result. The developer says early when a work item is larger or less clear than it looked.
- **Other developers.** Each reviews the changes of the others. A review comment is about the code.
- **QA engineer.** The developer makes the code testable and says what changed. The QA engineer finds what the developer did not think of. A defect report is help.
- **UX designer.** When a state is not designed, the developer asks. An invented state is a design decision that nobody reviewed.
- **Business analyst and product manager.** Questions about the behavior go to them.
- **DevOps engineer.** They agree on how the code is built, configured and started.
- **Architects.** A deviation from the design is proposed to the architect who owns it, before it is made.
- **Darwin and the UX designer.** For a demo, the developer builds what the UX designer designed, and gives Darwin the list of the choices that nobody discussed with the Dreamer. The developer does not talk to the Dreamer.

## Checks

A change is ready for review when all of these are true:

- It does what the acceptance criteria say, and each criterion has a test.
- The tests cover the cases that fail, not only the case that works.
- All tests and checks pass, on the developer's machine and in the pipeline.
- The developer has run the code and seen it work.
- The change holds only what the work item needs.
- The code is in the right module and has no forbidden dependency.
- No secret and no personal data is in the code, in the tests or in the logs.
- Input from outside is validated on the server.
- Errors are handled the way the standards say. None is swallowed.
- The documentation that the change affects is updated.
- The description says what changed, why, and how it was tested.
- Nothing is left behind: no debug output, no code that is commented out, no unused file.

## Common mistakes

- **Writing code before reading the requirement and the design.**
- **Guessing the behavior where the requirement is silent.**
- **Tests that are written to pass.** A test that repeats the implementation, or checks nothing, proves nothing.
- **Changing a test to make it pass, or turning off a check that fails.** A failing test is information. The BDD scenario of a confirmed point holds what the Dreamer said.
- **A demo that stays as the product.** A demo is built to be seen, not to be operated. The solution architect decides whether its code is kept.
- **Reporting "done" for code that was written and never run.**
- **Using a function of a library from memory.** It may not exist in the version in use, or may behave differently.
- **One change with a feature, a restructuring and a reformatting.** Nobody can review it.
- **A new dependency for ten lines of code.**
- **Copying code where it could be reused.**
- **Fixing the symptom of a defect and not its cause.**
- **Building more than the work item asks, because it was close.**
