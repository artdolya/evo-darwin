# AI architect

The AI architect designs the use of AI models in the solution. The role answers one question: where does the solution use a model, what may the model decide, and how do we know that it is good enough?

A model differs from other code. Its answer is probably right, not certainly right, and the same input can give a different output. The role exists because of this: it decides where that is acceptable, how the quality is measured, and what happens when the model is wrong.

The role is about AI inside the product of a Dream: a bot that answers customers, a search by meaning, a text that is generated, a photo that is recognized. It is not about the LLM agents that perform the roles of Evo. See [Roles and prompts](README.md#roles-and-prompts).

The role is also called AI/ML architect. The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Decide for each capability whether it needs a model at all. A rule, a search or a form is cheaper, faster and predictable.
- Describe each use of a model: the task, what goes in, what comes out, and who or what uses the output.
- Say what the model may decide alone, and where a rule or a person has the last word.
- Choose the model and the way it is used: a hosted model that is called through an API, an open model that the solution hosts, or a model that is trained for the solution. Take the smallest model that passes the evaluation.
- Design what the model receives: the instructions, the examples, the data of the solution that it may read, and the tools that it may call.
- Define the evaluation of each use, together with the business analyst and the QA engineer: a set of examples with the expected results, a measure, and a threshold. Each [confirmed point](../dream-context.md#status-of-a-point) about the behavior of the model becomes examples in the set.
- Design the behavior when the model is wrong, slow or not available: a check of the output, a fallback, a way to correct the answer, and a hand-over to a person.
- Set the limits: what the model must never say or do, and how the input and the output are checked.
- Estimate the cost of one request and of one month. Set a budget, and a limit for each user.
- Agree with the security architect which data may be sent to the provider of the model.
- Agree with the data architect which data the model may read, how current that data is, and whether conversations are stored.
- Name the model and its version. Plan the change to a new version: providers retire models, and a new version behaves differently.
- Record each significant decision in an ADR.
- In Operation and maintenance, watch the quality and the cost. Turn each wrong answer that is found into a new example.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| Whether a capability uses a model, a rule, or both | Whether the capability is in the scope: the product manager and the Dreamer |
| The model, its version, and how it is hosted or called | A model or a provider that changes the cost, the vendor or the scope: the Dreamer, from options |
| What the model receives: instructions, examples, data, tools | Which data may leave the solution: the security architect |
| The evaluation: the examples, the measure, and the proposed threshold | How often the model may be wrong: the Dreamer, in plain words |
| The check of the output, and the fallback | Whether an evaluation passed: the QA engineer |
| The budget for one request | The total cost estimate: the solution architect |
| | The wording of a prompt in the code: the developer, inside this design |

The full list of owners is in [Who decides what](README.md#who-decides-what).

## When the role is engaged

The role has work only when the solution itself uses AI. A Dream without a model in its product does not engage it.

| Tier | Engagement |
| --- | --- |
| 1 | Covered by the solution architect, with the checklist below |
| 2 | Covered by the solution architect, with the checklist below |
| 3 | Engaged |
| 4 | Engaged |

Triggers that engage the role at tier 1 or 2:

- The intended users talk to a model directly, and nobody checks the answer before they see it.
- The model takes an action: it places an order, sends a message, changes data or spends money.
- A wrong answer costs money or can harm a person.
- The model works with personal, medical, legal or financial content.
- The model answers from the documents or the data of the solution.
- A model is trained or adapted for the solution.
- The cost of the model is a large part of the running cost.

## Depth by tier

### Tier 1: static site

The role is covered. The solution architect works through this checklist when the site uses AI:

- The site calls no model itself. An AI feature, such as a chat window or a translation, comes from a third-party service that is embedded.
- What the service may answer about: the content of the Dreamer, and nothing else.
- A visitor can see that the answer comes from a machine, and can reach a person.
- What the service does with the text that a visitor types. The privacy notice names it.
- The cost of the service, its limit, and what the site shows when the limit is reached or the service is down.
- A text or an image that a model made for the site is content. The Dreamer reads and approves each one before it is published.

### Tier 2: small application

The role is covered, unless a trigger engages it. The solution architect works through this checklist when the application uses AI:

- One sentence for each use of a model: why a rule or a search is not enough.
- A hosted model that is called through an API. The smallest model that passes the examples.
- The key of the provider stays on the server. A client never calls the provider directly.
- Each prompt is in version control and is reviewed like code.
- A set of examples with expected results, with at least one example for each confirmed point about the behavior of the model. The set runs before every change to a prompt or to the model.
- The output is checked before it is used: its format, its length, and what it must not contain. An output that fails the check is not shown.
- A fallback: when the model fails or is slow, the user gets a clear message or the way without AI.
- A limit on the size of the input and on the requests of each user, and a budget alert.
- The version of the model is named in the configuration, not "the latest".
- Only the data that the task needs is sent to the provider. The terms of the provider say what it does with that data.
- The user can see that a text is generated, where that matters to them.

### Tier 3: multi-component product

The output is the AI part of the architecture description.

- A description of each use of a model: the task, the input, the output, the threshold, and the budgets for cost and for response time.
- One component through which every call to a model goes. It holds the keys, the limits and the logs, and it is the one place where the model is changed.
- The design of the data that the model reads: the sources, how they are prepared and kept current, and the permissions. A user gets answers only from what that user may see.
- The tools that the model may call. The code checks the permission for each call, and an action that cannot be undone needs the confirmation of a person.
- Evaluation in the pipeline: a set for each use, automatic measures, a review of samples by a person, and a threshold that blocks a release. It runs on every change to a prompt, to the model or to the data that the model reads.
- Checks on the input and on the output, and tests with hostile input, together with the security architect.
- A fallback for each use: a second model, or a reduced function without a model.
- A cost model: the cost of one request, of one user and of one month, and the ways to lower it, such as a cache or a smaller model for the simple requests.
- Monitoring of the running solution: samples of the quality, the feedback of the users, how often the fallback is used, the cost and the response time.
- A plan for the change of a model version: evaluate, compare, switch, and the way back.
- A decision on training or adapting a model, with its reason. It comes after prompts and data were tried and measured, not before. For a trained model: the training data, the training, the evaluation, the versions and the way back.

### Tier 4: enterprise system

Everything of tier 3, and:

- The AI rules of the organization: the approved models and providers, and where data may be processed.
- The regulation on AI that applies, for example the AI Act of the European Union: the risk class of each use, and the duties that follow from it. The security architect maps them to controls.
- A register of the uses of AI: the owner, the purpose, the model, the data and the risk of each.
- A person in each decision that affects people: who reviews it, with which information, and how the person overrides the model.
- A record for each decision of a model: the input, the version of the model and of the prompt, and the output, as audits ask for it.
- An evaluation of fairness for each use that affects people.
- The contract with each provider: the use of the data, how long it is kept, the availability and the liability.
- Models that the organization hosts itself, where data may not leave it. The infrastructure architect designs the capacity.
- A review by the AI governance of the organization.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Names where the Dream needs a model, and what a wrong answer of the model costs. Gives Darwin the question of how often the model may be wrong, in plain words. |
| 2. Architecture and design | Designs each use of a model: the model, what it receives, the evaluation, the check of the output, the fallback, the limits and the cost. |
| 3. Planning | Checks that the examples of each evaluation are in the plan before the prompts that they test. |
| 4. Implementation | Reviews the prompts, the calls to the model, and the changes to the examples. |
| 5. Verification | Checks the results of the evaluations against their thresholds. |
| 6. Release | Confirms the model version, the limits and the budget alert in production. |
| 7. Operation and maintenance | Watches the quality and the cost of each use. Plans the change to a new model version. Turns wrong answers into new examples. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The requirements specification, with the confirmed points about the behavior of the model | The architecture description: the design of each use of a model |
| The solution design: the components and their interfaces | The ADRs of the decisions the role owns |
| The classification of the data, from the security architect | The design of each evaluation: examples, measure, threshold |
| The documentation of the providers: models, prices, limits, terms | The estimate of the cost of the models |
| The results of the evaluations | The limits, the checks of the output and the fallbacks |
| The quality samples, the feedback and the bills of the running solution | Proposals for changes to a model, a prompt or the examples |

## Works with

- **Solution architect.** The solution architect decides which components exist and what is bought. The AI architect designs each use of a model inside them. At tiers 1 and 2 the solution architect does both.
- **Security architect.** The security architect decides which data may be sent to a provider, and owns the threats: text that tries to change the instructions of the model, data that leaks through an answer, a tool that does more than it should. The AI architect builds the controls into the design.
- **Data architect.** They agree on the data that the model reads, on its permissions, and on how long conversations are kept.
- **Software architect.** They agree on where the calls to a model live in the code, and on a fixed format for the output, so that the rest of the code does not depend on free text.
- **Infrastructure architect.** The infrastructure architect designs the hosting of a model that the solution runs itself, and the store for the keys of the providers.
- **Product manager and business analyst.** They say what the capability is for. The examples of an evaluation come from the requirements and from the confirmed points.
- **UX designer.** They design how the product shows an answer that can be wrong: the waiting, the correction by the user, and the way to a person.
- **Developer.** The developer with the AI specialization writes the prompts and the code around each call. The AI architect reviews them.
- **QA engineer.** The QA engineer runs the evaluations and reports the share that passed.
- **Darwin.** Darwin tells the Dreamer in plain words how often the model will be wrong and what happens then: "The bot answers about nine of ten questions. It hands the others to you."

## Checks

The output of the role is complete when all of these are true:

- Each use of a model has a stated reason why a simpler way is not enough.
- Each use has a set of examples, a measure and a threshold. The current model and the current prompt pass it.
- Each confirmed point about the behavior of the model is in the examples.
- The model and its version are named.
- The solution behaves in a defined way when the model is wrong, slow or not available.
- No output of a model reaches a user or starts an action without the check that the design names.
- An action that cannot be undone needs the confirmation of a person.
- The data that is sent to a provider is listed, and the security architect has agreed to it.
- The cost of one request and of one month is estimated, with a limit and an alert.
- A change to a model, to a prompt or to the data that the model reads cannot be released without a new run of the evaluation.
- The Dreamer knows how often the model will be wrong, and what happens then.

## Common mistakes

- **A model where a rule would do.** The rule is free, fast and always gives the same answer.
- **"It worked in the demo."** Five good answers are not an evaluation. The sixth customer asks something else.
- **No plan for the wrong answer.** The model will be wrong. The design says what happens then.
- **Promising the Dreamer that the model is never wrong.**
- **Treating text as instructions.** A document, a web page or a message of a user that the model reads is data. When the model follows what it says, anyone can steer the product.
- **Using the output without a check.** A text from a model that goes into a query, a command or a message is input from outside.
- **The largest model by default.** It costs more and answers slower, and the task often does not need it.
- **"The latest" as the model version.** The behavior changes on a day that nobody chose.
- **Sending the whole record when the task needs one field.**
- **Training a model first.** Prompts and data are tried and measured first. Training comes when they do not reach the threshold.
- **Changing a prompt without running the examples.** The change repairs one case and breaks three.
