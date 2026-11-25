# Dreamer

The Dreamer is the person who brings the idea and owns it. The role answers one question: what do I want, and is this it?

The Dreamer is the customer of Evo, and always a person. Evo expects mainly non-technical Dreamers: people who can turn an idea into income, and want to do it fast. A Dreamer is not expected to know how software is built, and loses interest when the way to the result is long.

The Dreamer talks to [Darwin](darwin.md), and only to Darwin. This document is written for the other roles. It says what the Dreamer decides, what the Dreamer is asked for, and what is never left to the Dreamer.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Describe the idea in their own words and in their own language.
- Answer the questions of Darwin about the purpose, the intended users, the wanted outcome and the limits.
- Say "I do not know" when that is the answer. It becomes an open point or a provisional point.
- Give what only the Dreamer has: texts, images, the brand, existing data, access to accounts, and contact with the intended users.
- Choose between options when Darwin presents them.
- Decide at the gates: confirm the scope, approve the approach, the cost range and the plan, accept each increment, and authorize go-live.
- Try each [demo](../SDLC.md#demos), and say what is right and what is wrong. What the Dreamer confirms after a demo is fixed. It changes only when the Dreamer changes it.
- Pay for the building and the running of the solution, inside the ranges that the Dreamer approved.
- Give feedback when the solution is in use.

The Dreamer is not responsible for a technical decision, for the wording of a requirement, or for testing.

## Decisions

| The Dreamer decides | The Dreamer does not decide |
| --- | --- |
| What the Dream is, including a solution that the Dreamer names | How a requirement is worded: the business analyst |
| What is in the first release, what is later and what is out | How the solution is built: the architects |
| An option that changes the cost, the vendor or the scope | The order of the work inside a release: the project manager and the tech lead |
| The cost ranges for building and for running | Whether a change is merged: the tech lead |
| The plan of the next release | Whether a test passed: the QA engineer |
| Whether an increment is accepted, and an exception to an acceptance criterion | Which security finding blocks a release: the security architect |
| Go-live | A legal requirement: nobody on the project can waive it |
| The acceptance of a remaining risk | |
| The retirement of the solution | |
| Whether a provisional point is right, after trying it in a demo | |
| A change to a point that the Dreamer confirmed before | |

A technical choice becomes a decision of the Dreamer when it changes what the Dreamer pays, ties the Dreamer to a vendor, or changes what the product does. The role that owns the choice then prepares it as options, and Darwin presents them.

## When the role is engaged

The Dreamer takes part in every project, at every tier. The role has no triggers.

| Tier | Who the Dreamer is |
| --- | --- |
| 1 | One person |
| 2 | One person |
| 3 | One person, or a few people. One of them is named as the decision-maker. |
| 4 | Several stakeholders of an organization. One of them is named as the decision-maker of each gate. |

## Depth by tier

Each tier asks a different amount of the Dreamer's time. No role asks the Dreamer for more than the tier needs.

### Tier 1: static site

- One short conversation about the purpose, the audience, the content and the look.
- The content: texts, images, the logo. The site cannot be finished without it.
- The address of the site: which name, and in whose account it is registered.
- A demo early: a first version of the page, and one or two questions about it.
- Two decisions. The Dreamer approves one summary of what is built, what it costs and when it is ready. Later the Dreamer tries the demo of the finished site and approves the publication.

### Tier 2: small application

- Several short conversations in Discovery.
- A decision at each gate: the scope, the approach with the cost range, the plan of each release, the acceptance of each increment, go-live.
- A few choices in plain words, for example how people sign in, or which payment provider is used.
- Accounts that must belong to the Dreamer: the domain, the hosting, the payment provider, the app store.
- A demo in Discovery and a demo at the end of each release, each with a few follow-up questions.

### Tier 3: multi-component product

Everything of tier 2, and:

- Choices about quality targets, each with its price: how much downtime is acceptable, how fast a page must load, how many users are expected.
- A status at a fixed rhythm, and several releases to plan and to accept.
- A few people who answer for different areas. One decision-maker is still named, so that two answers do not contradict each other.
- Access to intended users, for tests of the design and for feedback.

### Tier 4: enterprise system

The Dreamer is an organization. The role is split among named people:

- The sponsor, who pays and decides on the budget.
- A business owner for each domain, who decides the scope in that domain.
- Representatives of the people who will work with the system.
- The architecture, security, compliance and operations functions of the organization, each of which approves in its area.

Each gate has one named decision-maker and a formal, recorded sign-off. A change after a sign-off goes through the change control of the organization.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Describes the idea and answers questions. Tries the demos, and says what is right and what is wrong. Confirms the scope. |
| 2. Architecture and design | Chooses between the options that change cost, vendor or scope. Approves the approach and the cost range. |
| 3. Planning | Approves the plan of the next release. |
| 4. Implementation | Answers the questions that come up. Decides on trade-offs. Receives the status. Gives the content and the access that the work needs. |
| 5. Verification | Tries the demo. Accepts the increment or asks for changes. |
| 6. Release | Authorizes go-live. |
| 7. Operation and maintenance | Gives feedback. Is told about incidents. Decides on new work and on retirement. |

## Inputs and outputs

| Receives | Gives |
| --- | --- |
| The questions of Darwin | The description of the idea |
| The summary of the scope, with the points that are still provisional | Answers, and "I do not know" where that is true |
| The options, each with its cost and its consequence | Content, brand, existing data, access to accounts |
| The plan and the status | The decision at each gate |
| The demos, and the follow-up questions after each one | Confirmations and corrections after a demo |
| The release notes, the news about incidents and the remaining risks | Feedback from use |

The Dreamer does not receive [DreamContext](../dream-context.md). It is an internal document of Evo.

## Works with

- **Darwin.** The only role that the Dreamer talks to. Darwin asks, answers, presents every decision and reports the state of the work.
- **The DreamTeam.** Every other role works behind Darwin. A role that needs something from the Dreamer gives its question to Darwin, with the reason for it and the options it sees.

## Checks

A decision of the Dreamer counts when all of these are true:

- The Dreamer saw the exact version that the decision is about.
- The content was in the language of the Dreamer and in plain words. The Dreamer did not have to look up a term.
- A choice came as options, each with its cost and its consequence. A recommendation came with it when the Dreamer asked for one.
- The Dreamer said yes in words. Silence is not an approval.
- A confirmation after a demo names the point. "Looks good" about the whole demo confirms no single point.
- The decision is recorded: what was decided, on which version, and when.
- When the approved content changes later, the approval is asked again for the changed part.

## Common mistakes

These are mistakes of the roles that work for the Dreamer.

- **Going around Darwin.** A role that writes to the Dreamer directly brings a second voice, other words and questions that were already answered.
- **Asking a technical question.** "A relational or a document database?" is not a question for the Dreamer. "Option A costs less each month, option B handles ten times the visitors" is.
- **A questionnaire.** Twenty questions at once are answered badly or not at all. The Dreamer drives the conversation.
- **Replacing the idea of the Dreamer with a better one.** The Dreamer asked for an Android app. Evo builds an Android app, unless the Dreamer asks what Evo would do.
- **Asking what is already answered.** Read DreamContext before asking.
- **Treating enthusiasm as approval.** "Sounds great" in a conversation is not the confirmation of a scope.
- **Presenting an assumption as something the Dreamer said.** The Dreamer then approves a statement that was never theirs.
- **Changing a confirmed point without the Dreamer.** The Dreamer said where the menu belongs. A role that moves it for a good reason still breaks a promise. The reason goes to Darwin as a trade-off.
- **Asking for a decision without its price.** A scope change or a higher quality target has a cost. The Dreamer needs it to decide.
- **Deciding for the Dreamer because asking is slow.** The Dreamer carries the consequence.
- **Keeping bad news for the gate.** A problem is reported when it is known, with what it changes.
