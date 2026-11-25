# DreamContext

DreamContext is the internal document of Evo that holds what is known about one Dream. [Darwin](roles/darwin.md) keeps it, and every role of the DreamTeam works from it. It is the main output of [Discovery](SDLC.md#1-discovery), and it stays current in every later phase.

DreamContext is internal. The Dreamer does not read it. Darwin tells the Dreamer in plain words what it holds.

The terms Dreamer, Dream, Darwin and DreamTeam are defined in [SDLC.md](SDLC.md#terms).

Nothing in this repository creates or stores DreamContext yet.

## What it is for

DreamContext serves several purposes at once:

- **Hand-over.** The solution architect and the rest of the DreamTeam work from DreamContext. No role has to read the conversation to know what the Dreamer wants.
- **Confirmation.** Each point is open, provisional or confirmed. What the Dreamer confirmed is fixed by a test.
- **Readiness.** A score from 0 to 100 says how clear the Dream is. It decides when Discovery is done.
- **Value.** A score says how valuable the Dream can become.
- **Reality.** A score says how real the Dream is today.
- **Memory.** It records the questions, the answers and the decisions, so that nothing is asked twice.

TODO: add the further purposes of DreamContext. A fourth score is planned and not defined yet.

## Parts

| Part | Content | Written by |
| --- | --- | --- |
| Idea brief | The description of the Dreamer, unchanged and in its original language. The purpose, the intended users, the wanted outcome, the success signals and the limits. | Darwin |
| Scope | Each capability in one of three groups: first release, later release, out of scope. | Product manager |
| Requirements specification | The user journeys, the functional requirements with acceptance criteria, the BDD scenarios of the confirmed points, the quality attributes with targets, and the glossary. | Business analyst, with the UX designer and the solution architect |
| Open points | Every gap, ambiguity and contradiction, and every provisional point: what is unclear or not confirmed, which role raised it, and what it blocks. | Every role. Darwin keeps the list. |
| Tier | The tier of the project, its reasons, and the roles that are engaged. | Solution architect |
| Scores | Readiness, value and reality. See [Scores](#scores). | Darwin, with the inputs of the DreamTeam |
| Record of the conversation | The questions that were asked, the answers, each demo with what the Dreamer confirmed after it, and each decision of the Dreamer with its date. | Darwin |

Every point in DreamContext has a status: open, provisional or confirmed. See [Status of a point](#status-of-a-point).

How much each part holds depends on the [tier](SDLC.md#phases-by-tier). For a one-page site, DreamContext is one page.

TODO: state the language of DreamContext when the Dreamer speaks another language than the DreamTeam.

TODO: state the format of DreamContext and where it is stored.

## Status of a point

A point is one statement about the Dream: a requirement, a limit, a detail of a screen. Every point has one of three statuses.

| Status | Meaning | What follows |
| --- | --- | --- |
| Open | Nobody knows the answer yet. | Nothing is built on it. It lowers the readiness score. |
| Provisional | Evo works with it, and the Dreamer has not confirmed it. An assumption of a role is provisional. So is a detail that a demo shows for the first time. | It can be built and shown. It can change at any time, without a decision of the Dreamer. |
| Confirmed | The Dreamer said it in clear words, or agreed to it after seeing it in a demo. | It gets a BDD scenario. It changes only when the Dreamer changes it. |

A point moves between the statuses this way:

- An open point becomes provisional when a role makes an assumption so that the work can go on.
- An open or a provisional point becomes confirmed when the Dreamer states it, or answers a question about it, in clear words.
- A [demo](SDLC.md#demos) is the fastest way to confirm. Darwin shows the provisional points working, and asks about the ones that are expensive to change later.
- A point that the Dreamer saw and did not speak about stays provisional. Silence does not confirm. Neither does "looks good" about the whole demo.
- A confirmed point changes only by a new decision of the Dreamer. Darwin records the decision first. Then the point and its BDD scenario change.

Each confirmed point links to the words of the Dreamer that confirmed it, in the record of the conversation.

## From a confirmed point to a test

A confirmation of the Dreamer is the strongest signal that DreamContext holds. Evo fixes it by a test, so that the confirmed behavior stays true in every later release.

A confirmed point that can be observed in the product gets a BDD scenario: a short example of the behavior in the form Given, When, Then, in the words of the Dreamer's business.

An example. The Dreamer of the workout app tries a demo. Darwin asks: "The menu is at the bottom of the screen. Is that the right place, or do you want it at the top or on the left?" The Dreamer answers: "At the bottom." The point becomes confirmed, and it gets this scenario:

```gherkin
Scenario: The menu is at the bottom of the screen
  Given the app is open
  When a main screen is shown
  Then the menu is at the bottom of the screen
```

The roles handle the scenario this way:

- The business analyst writes the scenario as an acceptance criterion of the requirement, and links it to the answer of the Dreamer.
- The QA engineer automates it. It runs on every later change, in every later release.
- A scenario of a confirmed point that fails is a defect. Nobody changes the scenario to make it pass.
- A provisional point can have acceptance criteria too. They change with the point.
- A confirmed point that cannot be observed in the product, such as a budget, gets no scenario. The role that owns the topic keeps to it.
- A confirmed point about the behavior of an AI model cannot be checked by one exact scenario, because a model can answer the same input in different ways. It becomes examples in an evaluation with a threshold. The [AI architect](roles/ai-architect.md) designs the evaluation.

TODO: state the format of the BDD scenarios and the tool that runs them.

## Scores

### Readiness

The readiness score says how clear the Dream is, from 0 to 100. At 100, the next phase has nothing left to guess: no gap, no ambiguity and no contradiction.

The open points and the provisional points lower the score:

- An answer is missing that the design depends on.
- A word can be read in two ways.
- Two statements contradict each other.
- A requirement has no way to check it.
- A point is provisional: a role assumed it, and the Dreamer has not confirmed it.

The score is used this way:

- DreamContext passes to Architecture and design when the score reaches the threshold.
- Darwin aims for the threshold with the fewest questions. It asks first the question that raises the score most.
- A demo raises the score fast. After one look, the Dreamer can confirm several provisional points.
- A later phase that finds a gap adds an open point. The score falls, and DreamContext returns to Darwin.

TODO: state how the readiness score is calculated from the open points and the provisional points.

TODO: state the readiness score at which DreamContext passes to Architecture and design.

### Value

The value score is internal to Evo. It says how valuable the Dream can become. A new social network that can earn millions scores high. So does a cure for cancer.

The product manager gives the input for it.

### Reality

The reality score says how real the Dream is today: whether it can be built with the technology and the knowledge that exist now. Evo is not interested in star battleships yet.

The reality score is not the tier. The tier says how large a project is. The reality score says whether it can be built at all today.

The solution architect gives the input for it.

TODO: state the scale of the value score and of the reality score, and how each one is calculated.

TODO: state what Evo does with the value score and the reality score, and what Darwin tells the Dreamer when one of them is low.

## The life of DreamContext

1. Darwin creates DreamContext from the first message of the Dreamer.
2. The roles of the DreamTeam read it and give Darwin their open points.
3. Darwin closes each open point. It asks the Dreamer, or it records a provisional point when the gap is small.
4. When enough was discussed to show something, Darwin offers a [demo](SDLC.md#demos). After it, Darwin asks a few follow-up questions. The points that the Dreamer confirms get the status confirmed, and their BDD scenarios.
5. When the readiness score reaches the threshold, the Dreamer confirms the scope, and DreamContext passes to the solution architect.
6. A later phase can send it back. An architect finds a gap. A developer finds that something cannot be built as the Dreamer wants it. The role gives Darwin the open point with the options, Darwin takes the trade-off to the Dreamer, and DreamContext is updated with the decision.
7. The demo of each increment confirms more points, in the same way as a demo in Discovery.
8. DreamContext stays current as long as the solution runs. Feedback and new ideas from Operation and maintenance enter it the same way as the first message.

A change to DreamContext after a gate can make an approval stale. The approval is then asked again for the changed part.

## Examples

Three Dreams as a Dreamer could bring them, and how DreamContext starts. The open points are examples of what the roles would raise, not a script of questions.

| The Dreamer says | Known from the first message | Open points | First tier |
| --- | --- | --- | --- |
| "I want to create a simple site that describes my business. I develop water pumps. Ideally it should be free for me, and recognizable on the internet." | The purpose: present the business. The field: water pumps. The limit: no cost, if possible. The wish: people find and recognize the site. | What the site says and shows. Whether "free" includes the address of the site. What "recognizable" means: found in a search, or a name of its own. How a visitor contacts the Dreamer. | 1 |
| "I want to create a Telegram bot for my customers. Today I send them examples of my shoes by hand, in direct messages. I want a catalog of my shoes, an easy way for me to add shoes, and my customers should be able to order online." | The channel: a Telegram bot. A catalog of shoes. The Dreamer adds shoes in an easy way. The customers order in the bot. Today the Dreamer sends photos by hand. | What an order needs: size, quantity, address. How an order is paid. How the Dreamer learns about a new order. | 2 |
| "I want to create a mobile application that lets me build a sequence of timers for my Tabata and other workouts. It should be available only for Android phones." | A mobile app for Android only. Sequences of timers. The use: workouts such as Tabata. | Whether the app is for the Dreamer alone or for other people too. How a timer signals its end. Whether sequences are saved. | 2 |

In each example the solution that the Dreamer names is taken as given: a site, a Telegram bot, an Android app. Darwin does not propose another one unless the Dreamer asks for advice.

A first demo for each of the three Dreams, and one follow-up question after it. The answer of the Dreamer turns a provisional point into a confirmed one.

| Dream | A first demo could show | A follow-up question |
| --- | --- | --- |
| The site for the water pump business | One page with the name of the business, a short text about the pumps, and a form to write to the Dreamer. | "A visitor can write to you with this form. Is that how you want to be reached, or by telephone?" |
| The Telegram bot with the shoe catalog | A bot with three sample shoes that a customer can look through. | "Each shoe has one photo, a name and a price. Is that what your customers need to see?" |
| The Android app with the workout timers | An app with one sequence of timers that runs. | "The phone makes a sound when a timer ends. Is a sound right, or do you want it to vibrate?" |
