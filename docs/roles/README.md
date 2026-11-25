# Roles

The roles of the [software development life cycle](../SDLC.md) of Evo. A role is a set of responsibilities, decisions and outputs. It is not a person: an LLM agent or a person performs it. The one exception is the Dreamer, who is always a person.

The Dreamer talks to one role only: Darwin. The other roles form the DreamTeam and work behind Darwin. The terms are defined in [SDLC.md](../SDLC.md#terms).

Every role has one document in this folder.

## Role documents

| Group | Role | The question it answers | Also called |
| --- | --- | --- | --- |
| Decision | [Dreamer](dreamer.md) | What do I want, and is this it? | Customer, client |
| Contact | [Darwin](darwin.md) | Does Evo understand what the Dreamer wants, and does the Dreamer know what Evo is doing? | |
| Product | [Product manager](product-manager.md) | What is the smallest thing that gives the Dreamer the outcome, and what comes after it? | Product owner |
| Product | [Business analyst](business-analyst.md) | What exactly must the solution do, and how can anyone check it? | Requirements engineer |
| Product | [UX designer](ux-designer.md) | Can the intended user reach the outcome, easily, on the device they have? | Product designer |
| Delivery | [Project manager](project-manager.md) | In which order is the work done, where does it stand, and what threatens it? | Delivery manager |
| Architecture | [Solution architect](solution-architect.md) | Which parts does the solution have, how do they work together, and why this way? | Solutions architect, system architect |
| Architecture | [Software architect](software-architect.md) | How is the code structured, and which rules does every developer follow? | Application architect |
| Architecture | [Data architect](data-architect.md) | Which data do we keep, in which shape, where, and for how long? | Information architect |
| Architecture | [Infrastructure architect](infrastructure-architect.md) | Where does the solution run, how does a change get there, and what happens when something fails or the load grows? | Cloud architect, platform architect |
| Architecture | [Security architect](security-architect.md) | What can go wrong, who could cause it, and what stops them? | |
| Architecture | [AI architect](ai-architect.md) | Where does the solution use a model, what may the model decide, and how do we know that it is good enough? | AI/ML architect |
| Engineering | [Tech lead](tech-lead.md) | Is each change right, and does the increment fit together? | Lead developer |
| Engineering | [Developer](developer.md) | Does this work item do what its acceptance criteria say, in the way the design prescribes? | Software engineer |
| Quality | [QA engineer](qa-engineer.md) | Does it do what the requirements say, and what happens when it is used in a way that nobody planned? | Test engineer |
| Operations | [DevOps engineer](devops-engineer.md) | Can every accepted change reach production the same safe way every time, and can it be taken back? | Platform engineer, release engineer |
| Operations | [Site reliability engineer](site-reliability-engineer.md) | Does the solution work for its users right now, and will it still work next month? | Operations engineer |
| Documentation | [Technical writer](technical-writer.md) | Can a person who was not on the project use, integrate and operate the solution from what is written? | Documentation engineer |

## When each role is engaged

Evo builds projects of very different size. The [tier](../SDLC.md#project-tiers) of a project decides which roles are performed on their own, which roles are covered by another role, and how deep each one works. The table for all roles and tiers is [Roles by tier](../SDLC.md#roles-by-tier) in SDLC.md.

Two rules complete that table:

- **A trigger engages a role at any tier.** Each role document lists its triggers. A one-page site that takes payments engages the security architect. A small application that imports the data of an old system engages the data architect.
- **A covered role still has its work done.** Each role document has a short checklist for each tier where the role is covered. The covering role works through that checklist.

For a person, an extra role on a project costs a salary. For an LLM agent, it costs one more pass over the documents. So the tier does not ration the roles by price. It limits the depth of the work, because each extra role adds questions for the Dreamer, documents to keep consistent and review rounds.

## Architect roles

Six architect roles share the design of a solution. The AI architect has work only when the solution itself uses AI. This section says how the roles divide the design, which architect roles have no document yet, and which names are not roles of their own.

### Who decides what

Each concern has one owner. The owner decides, after asking the roles in the third column.

| Concern | Owner | Asked before the decision |
| --- | --- | --- |
| The tier of the project, and which architect roles are engaged | Solution architect | |
| The components of the solution and the boundaries between them | Solution architect | Software architect, data architect |
| What is built, bought or reused | Solution architect | All |
| The quality targets, and the trade-offs between them | Solution architect | All |
| The technology of the solution as a whole: platform, main languages | Solution architect | Software architect, infrastructure architect |
| The total cost estimate | Solution architect | Infrastructure architect, for the running cost |
| The structure, the frameworks and the libraries inside a component | Software architect | Solution architect |
| The API contracts and the message contracts | Software architect | Solution architect, data architect, security architect |
| Which component owns which data | Solution architect | Data architect |
| The data model, the type of each data store, the migrations | Data architect | Software architect |
| How long data is kept and how it is deleted | Data architect | Security architect |
| The classification of the data, and the protection each class needs | Security architect | Data architect |
| Authentication and authorization | Security architect | Software architect, solution architect |
| The rules for secrets and keys | Security architect | Infrastructure architect, who provides the store |
| The compliance requirements and the controls that meet them | Security architect | Data architect, infrastructure architect |
| Hosting, environments and networks | Infrastructure architect | Solution architect, security architect |
| The delivery pipeline and the deployment strategy | Infrastructure architect | Software architect, security architect |
| Backup and recovery | Infrastructure architect | Data architect, for what must be recoverable. Solution architect, for the targets. |
| Logs, metrics, traces and alerts | Infrastructure architect | Software architect, for what the code emits. Security architect, for the audit events. |
| Whether a capability uses an AI model, and what the model may decide alone | AI architect | Solution architect |
| The AI model, its version, and what the model receives | AI architect | Solution architect, for the cost and the vendor. Software architect, for the place in the code. |
| How the quality of a model is measured: the examples, the measure and the threshold | AI architect | Solution architect, for the quality targets |
| Which data may be sent to the provider of a model | Security architect | AI architect, data architect |

When two architect roles disagree, the solution architect decides and records the decision in an ADR. There are two exceptions:

- A minimum security control can be waived only by the Dreamer, as a recorded acceptance of the risk. Darwin explains the risk in plain words, from what the security architect describes.
- A legal requirement cannot be waived.

No architect role decides the scope or the priorities. They belong to the product manager and the Dreamer. An architect who finds that a requirement costs far more than its value says so, with the cost, and the Dreamer decides.

### Architect roles that are not described yet

Larger or more specialized projects need more architect roles. Until a role has its own document, the role in the last column carries its concerns.

| Role | Concern | Typically needed | Covered by |
| --- | --- | --- | --- |
| Enterprise architect | The fit of the solution with all the systems, the standards and the strategy of an organization. | Tier 4 | Solution architect |
| Integration architect | The interfaces to other systems: APIs, messaging, file exchange, integration platforms. | Tiers 3 and 4, with many integrations | Solution architect |
| Frontend architect | The structure of the client applications: state, components, design system, performance in the browser. | Tiers 3 and 4, with a rich user interface | Software architect |
| Mobile architect | Native or cross-platform apps: offline use, synchronization, release through the app stores. | Any tier with a mobile app | Software architect |
| Business architect | The business capabilities and processes that the solution supports or changes. | Tier 4 | Business analyst |

At tier 4 the organization of the Dreamer often has an enterprise architect of its own. That person is a stakeholder on the side of the Dreamer. Darwin talks to them, and the solution architect works to their standards.

### Names that are not roles of their own

Evo splits a role when the decisions differ. When only the knowledge differs, it adds a [specialization](#specializations).

| Name | What it is in Evo | Why |
| --- | --- | --- |
| AWS, Google Cloud, Azure or OCI solutions architect | A specialization of the [infrastructure architect](infrastructure-architect.md) | The question and the decisions are the same on every provider. Only the services, the prices and the limits differ. |
| Cloud architect, platform architect | The [infrastructure architect](infrastructure-architect.md) | The same role. Many Dreams run on a simple host and not in a large cloud, so the role is not named after the cloud. |
| Application architect | The [software architect](software-architect.md) | The same role. |
| ML architect | The [AI architect](ai-architect.md) | A model that is trained for the solution is a trigger and a depth of that role. |
| Prompt architect, prompt engineer | For a prompt in the product of a Dream: the [developer](developer.md) with the AI specialization, inside the design of the AI architect. For the prompts of Evo itself: see [Roles and prompts](#roles-and-prompts). | Writing a prompt is a skill. The decisions around it belong to the AI architect. |

## Specializations

A specialization is the same role with more knowledge of one area. It has the same question, the same decisions and the same role document.

| Role | Specializations | What a specialization adds |
| --- | --- | --- |
| Developer | Frontend, backend, mobile, AI | The languages, the frameworks and the tools of the area. For AI: the prompts and the code around a call to a model. The way a prompt is written depends on the model, so this specialization can be narrowed to one family of models. |
| Infrastructure architect | One for each provider, such as AWS, Google Cloud, Azure and OCI. One for simple hosts: static hosts and platform services. | The services, the prices, the limits and the reference designs of the provider. |
| AI architect | One for each family of models | The models of the family, their prices, their limits, and the way they are instructed. |

Two rules apply:

- **The choice comes before the specialization.** A specialist of one provider recommends that provider. So the role without a specialization chooses the provider or the model first, from the requirements. Then the specialization is engaged. When the Dreamer names a provider, it is a constraint, and the specialization is engaged from the start.
- **A specialization is engaged only where its knowledge is needed.** A static site on a static host needs no specialist of a large cloud.

TODO: state how a specialization is given to an LLM agent, and where its knowledge is stored.

## Roles and prompts

A role document says what a role does. It does not depend on a model. When an LLM agent performs a role, it works from a prompt. The prompt is written from the role document, for one model, because each model is instructed in its own way.

- The role document is the source. When the two differ, the role document is right, and the prompt is corrected.
- One role can have several prompts: one for each model that performs it.
- A prompt is tested like code: a set of examples with expected results, run again after each change to the prompt or to the model.
- Writing these prompts is work on Evo itself. It is not a role in the SDLC of a Dream, and it has no role document here.

A prompt inside the product of a Dream is a different thing. It belongs to the Dream: the [AI architect](ai-architect.md) designs it, and the developer with the AI specialization writes it.

Nothing in this repository holds a prompt of a role yet.

TODO: state where the prompts of the roles are stored, and how they are tested for each model.

## Sections of a role document

Every role document in this folder has the same headings, in this order:

1. **Opening paragraph**: what the role is for, and the question it answers.
2. **Responsibilities**: what the role does.
3. **Decisions**: what the role decides, and what it leaves to another role.
4. **When the role is engaged**: the tiers, and the triggers that engage the role at any tier.
5. **Depth by tier**: what the role produces at each tier. Where the role is covered by another role, the checklist for that role.
6. **Work in each phase**: what the role does in each phase of the SDLC.
7. **Inputs and outputs**: the artifacts the role reads and the artifacts it produces.
8. **Works with**: where the role ends and the next role begins.
9. **Checks**: the conditions that the output of the role must meet. A reviewer uses the same list.
10. **Common mistakes**: the errors that the role is most likely to make.

The document of the [Dreamer](dreamer.md) has the same headings. Its checks and its common mistakes are written for the roles that work for the Dreamer.

When you add a role document, add it to the table above, to the role table and the tier table in [SDLC.md](../SDLC.md#roles), and to the index in [docs/README.md](../README.md).
