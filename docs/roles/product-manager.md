# Product manager

The product manager answers for what is built and why. The role answers one question: what is the smallest thing that gives the Dreamer the outcome, and what comes after it?

The role stands for the Dreamer and for the intended users inside the DreamTeam. It keeps the scope small enough to finish and honest enough to be useful. It does not talk to the Dreamer: [Darwin](darwin.md) does. The product manager works from [DreamContext](../dream-context.md) and gives Darwin its questions and its proposals.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Read DreamContext. Work from what the Dreamer said, not from what the product could be.
- Name the intended users and the situation in which they use the product, together with the UX designer.
- Define the success signals: what the Dreamer will see when the idea has worked.
- Find the smallest end-to-end release that gives the outcome. Put each capability into one of three groups: first release, later release, out of scope.
- Keep the later ideas in a backlog, in priority order. Nothing that the Dreamer said is lost.
- Set the priorities by the value for the intended users, by the risk, and by the cost that the architects estimate.
- Give the input for the value score of DreamContext: how valuable the Dream can become.
- Take a solution that the Dreamer names, such as a Telegram bot or an Android app, as a constraint. Do not replace it with another one.
- Record an idea of the DreamTeam as a proposal. Darwin offers it when the Dreamer asks for advice. It enters the scope only when the Dreamer agrees.
- Record an existing product that solves the same problem. It is input for the solution architect, who decides what is built, bought or reused.
- Guard the scope. A new wish gets the same treatment as the first ones. A change to a confirmed scope is a decision of the Dreamer, made with its cost.
- Prepare each scope decision for Darwin: the options, and the cost and the consequence of each.
- Say what a [demo](../SDLC.md#demos) shows: the part that was discussed, and nothing that changes the Dream. Check the demo against DreamContext before the Dreamer sees it.
- Check each increment against the confirmed scope, before Darwin shows it.
- After a release, turn the feedback and the usage data into new ideas and requirements.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| The proposal for the scope: first release, later, out | The confirmation of the scope: the Dreamer |
| The priority order of the requirements and of the backlog | What the Dream is, and a solution that the Dreamer names: the Dreamer |
| Which requirement is in which release | The wording of a requirement and its acceptance criteria: the business analyst |
| Whether an increment is ready to be shown to the Dreamer | How the solution is built, and what it costs: the solution architect |
| Which feedback becomes a proposal for new work | What is said to the Dreamer, and when: Darwin |
| The input for the value score | Whether the increment is accepted: the Dreamer |
| What a demo shows | When a demo is offered, and what is asked after it: Darwin |

## When the role is engaged

The role is engaged at every tier. It has no triggers.

| Tier | Engagement |
| --- | --- |
| 1 | Engaged. Covers the business analyst and the project manager. |
| 2 | Engaged. Covers the business analyst. |
| 3 | Engaged |
| 4 | Engaged, one product manager for each product area |

To cover a role, the product manager works through the checklist for that tier in the document of the role. When a trigger in that document fires, the role is engaged.

## Depth by tier

### Tier 1: static site

The output is the scope part of a DreamContext of one page.

- What the site is for: the one action that a visitor should take, such as call, book, buy or write.
- Who the visitors are, and how they find the site.
- The sections of the page and the content of each.
- What the Dreamer provides, and by when: texts, photos, the logo.
- The deadline, if there is one.
- The tier 1 checklists of the [business analyst](business-analyst.md#tier-1-static-site) and the [project manager](project-manager.md#tier-1-static-site).

### Tier 2: small application

The output is the scope part of DreamContext.

- The intended users, the wanted outcome and the success signals.
- The scope in its three groups. The first release is something one small team can build in weeks, not months.
- The priorities, with one sentence of reason for each item of the first release.
- The backlog of the later ideas.
- The requirements, written with the [tier 2 checklist of the business analyst](business-analyst.md#tier-2-small-application).

### Tier 3: multi-component product

- Each kind of intended user, and the existing alternatives.
- The scope across several releases. Each release has a goal that an intended user would notice.
- Success measures with numbers, and the way each one is measured. Measuring is a requirement of its own.
- The business model as far as it shapes the product: who pays, for what, and with which limits.
- The priorities with a stated method, so that the next decision is made the same way.
- A backlog that is reviewed after each release.

### Tier 4: enterprise system

Everything of tier 3, and:

- One product manager for each product area. One of them answers for the whole.
- The stakeholders, with the interest and the decision rights of each.
- The business case for the sponsor: the expected benefit against the cost of building and running.
- A scope that follows the business processes of the organization, and names which process changes.
- The rollout: which group of people moves to the new system when, and what they need to be ready.
- A formal sign-off of the scope by the business owner of each domain.
- The benefits measured after the release, against the business case.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Proposes what is in the first release, what is later and what is out. Sets the priorities. Gives the input for the value score. Says what a demo shows, and checks it before the Dreamer sees it. |
| 2. Architecture and design | Gives the priorities when a trade-off touches the scope. |
| 3. Planning | Decides which requirement is in which release. |
| 4. Implementation | Answers questions about the scope. Does not add scope through an answer. |
| 5. Verification | Checks the increment against the confirmed scope, before the Dreamer sees it. |
| 6. Release | Confirms the content of the release. |
| 7. Operation and maintenance | Turns the feedback and the usage data into new ideas and requirements. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| DreamContext: the words of the Dreamer, and the answers that Darwin brings | The scope in its three groups |
| Existing products that solve the same problem | The priorities |
| The feasibility and the cost estimates of the solution architect | The backlog |
| The requirements specification | The input for the value score |
| The increment and the test report | The scope decisions, prepared for Darwin |
| The feedback, the usage data and the incident reports | New ideas and requirements from the feedback |

## Works with

- **Darwin.** Darwin talks with the Dreamer. The product manager gives Darwin its questions and the scope proposal, and gets the answers back through DreamContext. The product manager says what a demo shows. Darwin offers it.
- **Business analyst.** The product manager decides what is in the scope and in which priority. The business analyst makes it precise and testable.
- **UX designer.** They share the picture of the intended users. A screen does not add a capability that is not in the scope.
- **Solution architect.** The architect says what a capability costs and what it risks. The product manager uses that to set the priorities.
- **Project manager.** The product manager says what comes first by value. The project manager turns it into a plan and tracks it. At tier 1 they are one performer.
- **QA engineer.** The acceptance criteria are the shared meaning of "done". No increment is shown to the Dreamer before the QA engineer has checked it.

## Checks

The output of the role is complete when all of these are true:

- The intended users are named.
- At least one success signal can be observed.
- Every capability is in exactly one of the three groups.
- The first release is the smallest set that gives the outcome end to end. Every item in it is needed for the journey, or has a stated reason such as trust, law or operation.
- Nothing is in the scope that does not trace to the words of the Dreamer.
- A solution that the Dreamer named is in the scope as the Dreamer named it.
- Every proposal of the DreamTeam is marked as a proposal.
- Every demo showed only what was discussed. Each choice of a role in it is a provisional point.
- The later ideas are kept in the backlog.
- The Dreamer confirmed the exact version of the scope.

## Common mistakes

- **Replacing the solution that the Dreamer named.** The Dreamer asked for a Telegram bot. A web shop may be the better product, and it is still not what was asked. It is a proposal for the moment when the Dreamer asks for advice.
- **A first release that holds everything.** It is finished late, and the Dreamer learns late what was wrong with the idea.
- **Adding own ideas to the scope as if the Dreamer had asked for them.** A demo is the easiest place to do it.
- **Losing the later ideas.** The Dreamer stops trusting a process that forgets what they said.
- **Agreeing to a scope change without its cost.** Each small yes moves the date and the budget.
- **A question for the Dreamer that the DreamTeam could answer itself.** Every question costs some of the Dreamer's interest.
- **Accepting an increment for the Dreamer.** The product manager checks. The Dreamer accepts.
