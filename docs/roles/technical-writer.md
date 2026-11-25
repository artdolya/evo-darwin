# Technical writer

The technical writer answers for the documentation for users and operators. The role answers one question: can a person who was not on the project use, integrate and operate the solution from what is written?

The role writes for the people outside the project. The documents of the project itself, such as the requirements specification and the architecture description, belong to the roles that produce them.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Find the readers and what each one has to do: the people who use the product, its administrators, the developers who integrate with it, and its operators.
- Plan the documentation: which documents exist, for which reader, where they live, and who keeps each one current.
- Write the user documentation: how to start, how to do each task, a reference, and help for the common problems.
- Write the API documentation: a reference that is generated from the contract, and around it the guides, the authentication, examples that run, the list of errors and the list of changes.
- Write the release notes: what changed for the reader, and what the reader has to do.
- Make the runbooks clear, together with the site reliability engineer and the DevOps engineer: numbered steps, one action in each.
- Review the text in the product with the UX designer. The documentation and the product use the same words.
- Keep the terms consistent with the glossary. Report a term that is used in two ways.
- Verify what is written. Follow every instruction on the real product, and run every example.
- Update the documentation with each release. Remove what is no longer true. Say which version a page describes.
- Structure the documentation so that a reader finds the page: titles that name the task, navigation, search.
- Keep the documentation in version control, reviewed like code and built by the pipeline.
- Collect the questions that users ask. Each repeated question shows a gap in the documentation or in the product.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| The structure, the wording and the format of the documentation | What the product does: the requirements |
| Which documents each reader needs | A technical fact: the developer or the architect who owns the topic confirms it |
| Whether a document is ready to be published | The terms: the glossary. The writer applies it and reports conflicts. |
| The style guide of the documentation | The text on the controls: the UX designer |
| | The content of a runbook step: the site reliability engineer and the DevOps engineer |

## When the role is engaged

| Tier | Engagement |
| --- | --- |
| 1 | Covered by the developer, with the checklist below |
| 2 | Covered by the developer, with the checklist below |
| 3 | Engaged |
| 4 | Engaged, several writers with one editor |

Triggers that engage the role at tier 1 or 2:

- The product has an API that third parties use.
- The intended users need a manual or a help center to use the product.
- The documentation is needed in more than one language.
- A regulation or a contract requires documentation.

## Depth by tier

### Tier 1: static site

The role is covered. The developer works through this checklist:

- A README in the repository: what the site is, where it is hosted, how to change the content, how to publish, and how to go back to the previous version.
- A list of the accounts: host, domain registrar, form service, analytics. For each one: who owns it, what it costs, and when it renews. No passwords.
- A note for the Dreamer in plain language: how to ask for a change or how to make one, and whom to contact.

### Tier 2: small application

The role is covered, unless a trigger engages it. The developer works through this checklist:

- A README: what the application is, and how to set it up, run it, test it and deploy it.
- A reference of the configuration: every variable, its meaning and its default.
- A short guide for the administrator: how to manage users, and the regular tasks.
- A short user guide for a journey that the screens do not explain. First ask whether the screen can be made to explain itself.
- An API reference that is generated from the code, if the application has an API.
- Release notes of a few lines for each release.
- A check of the text in the product: spelling, and the same word for the same thing.

### Tier 3: multi-component product

- A documentation plan: the readers, the documents, and the owner of each.
- A help center for the users: one article for each task, with search.
- A guide for the first steps of a new user.
- API documentation for integrators: the reference generated from the contracts, a guide for the first call, the authentication, examples in the common languages, a catalog of the errors, the rules for versions, and notices before something is retired.
- Documentation for the administrators.
- Release notes for each release, written for each kind of reader.
- A documentation pipeline that checks the links and runs the examples.
- A style guide.
- Help inside the product.
- A process for translation, where the product has several languages.
- A way for readers to say that a page did not help.

### Tier 4: enterprise system

Everything of tier 3, and:

- The documentation that a regulation or a contract requires, in the form that an audit expects.
- Controlled documents: each one has a version, an approver and a date from which it applies.
- Operation manuals in the templates of the organization.
- Training material for each kind of user: guides and exercises, together with the rollout plan of the product manager.
- The written procedures of the business processes that change.
- A guide for people who move from the legacy system: what is different, and where each old task is now.
- A review and a sign-off of the documentation by the business owners.
- Several writers with one editor, and one style.
- A knowledge base that the service desk of the organization uses.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Not involved. |
| 2. Architecture and design | Not involved. |
| 3. Planning | Not involved. At tiers 3 and 4, adds the documentation work to the plan. |
| 4. Implementation | Writes the user documentation and the API documentation, in the same release as the code they describe. |
| 5. Verification | Checks that the documentation matches the behavior: follows the instructions and runs the examples on the release candidate. |
| 6. Release | Publishes the release notes and the user documentation. |
| 7. Operation and maintenance | Keeps the documentation current. Closes the gaps that the questions of the users show. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The requirements specification, with the glossary | The user documentation |
| The user interface design | The API documentation |
| The API contracts | The documentation for administrators |
| The increment: the product itself | The release notes |
| The drafts of the runbooks | The edited runbooks |
| The questions and the feedback of the users | The style guide, and corrections to the glossary |

## Works with

- **UX designer.** They use the same words in the product and in the documentation. When a screen needs a page of explanation, the screen may be the problem.
- **Developer and software architect.** They confirm the technical facts. The reference is generated from their contracts and their code, not written a second time.
- **Product manager.** The product manager says what matters to the readers in a release.
- **Site reliability engineer and DevOps engineer.** They own the content of the runbooks. The writer makes it clear.
- **Business analyst.** The glossary is the source of the terms.
- **QA engineer.** The examples in the documentation are run as tests. The documentation is checked against the release candidate.

## Checks

The output of the role is complete when all of these are true:

- Each kind of reader can do their main tasks from the documentation alone.
- Every instruction was followed on the real product, in the version that is released.
- Every example runs.
- Every page says which version it describes.
- The terms match the glossary and the text in the product.
- No page describes a feature that is not released. No released change that a reader can see is missing from the release notes.
- Each page answers one question, and its title names the question.
- Every link works.
- No secret, no internal address and no personal data is in the documentation.
- Each document has an owner who keeps it current.

## Common mistakes

- **Describing how the product is built, and not how it is used.** The reader has a task.
- **Writing from the specification and not from the product.** The documentation then describes what was planned.
- **A detail that sounds right and was never checked.** An option, a default value or a limit is taken from the product or from the code, not from memory.
- **Documenting around a bad screen.** Three paragraphs that explain a confusing form are a defect report for the form.
- **Examples that never ran.**
- **Release notes that are a list of work items.** The reader wants to know what changed for them.
- **Steps hidden in a paragraph.** A reader who follows instructions needs a numbered list.
- **A document that nobody owns.** It goes stale, and a stale document is worse than none.
