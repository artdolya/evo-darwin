# UX designer

The UX designer answers for how the product looks and behaves for the people who use it. The role answers one question: can the intended user reach the outcome, easily, on the device they have?

The role covers both the structure and the look: the journeys and the navigation, and the screens with their colors, type and text. It works for the intended users, who are often not the Dreamer who brings the idea.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Find out who the intended users are: their situation, their device, their abilities, and what they already know. What only the Dreamer knows is asked through Darwin.
- Describe the user journeys: the steps from a need to the outcome.
- Structure the content and the navigation, so that a person finds things where they expect them.
- Sketch the main screens before the visual design, to agree on the structure first.
- Design what a [demo](../SDLC.md#demos) shows. Give Darwin the list of the details that are choices of the designer, such as the place of the menu, so that Darwin can ask the Dreamer about them.
- Design each screen with all its states: empty, loading, error, success, and no permission.
- Design the look inside the brand of the Dreamer: colors, type, spacing, images. Keep it to a small set of styles that repeat.
- Design for each size of screen that the requirements name. Start with the smallest.
- Design for accessibility: contrast, text size, use by keyboard and by screen reader, visible focus, motion that can be turned off. The usual target is level AA of the Web Content Accessibility Guidelines (WCAG).
- Design the forms: labels, help, validation, and messages that say what went wrong and what to do.
- Write the text on the controls and in the messages, in the words of the glossary.
- Test the design before it is built: with intended users where they can be reached, against usability rules where they cannot.
- Hand the design to the developers with what they need: sizes, states, behavior and image files.
- Review the built screens against the design. Accept a deviation or ask for a correction.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| The structure of the navigation and of each screen | What the product does: the product manager and the Dreamer |
| The look, inside the brand | The brand itself, and a question of taste that the Dreamer cares about: the Dreamer |
| The text on the controls and in the messages | The business rules behind a screen: the business analyst |
| Which techniques meet the accessibility target | The accessibility target: a requirement, approved by the Dreamer |
| Whether a built screen matches the design | The frontend technology and the component library: the software architect |

## When the role is engaged

The role is engaged at every tier. It has no triggers.

| Tier | Engagement |
| --- | --- |
| 1 | Engaged |
| 2 | Engaged |
| 3 | Engaged |
| 4 | Engaged, several designers who share one design system |

## Depth by tier

### Tier 1: static site

At this tier the design is most of the product. The output is the design of the page for a phone and for a desktop, or a built demo where the site comes from a template.

- The sections in the order in which a visitor needs them.
- One main action that stands out: call, book, buy or write.
- The look from the brand of the Dreamer, or from two or three sites that the Dreamer likes.
- The real content, not placeholder text. Ask for it early: the design depends on its length and its tone.
- Images in the right size, each with a text alternative.
- Readable text sizes and enough contrast.
- The states of the contact form: empty, wrong input, sent, failed.

### Tier 2: small application

- A journey for each kind of user.
- A map of the screens, and how a person moves between them.
- Sketches of the main screens, agreed before the visual design.
- The visual design on top of an existing component library. A custom component needs a reason.
- All the states of each screen.
- The behavior of the forms.
- The rules for small and large screens.
- The basics of WCAG level AA: contrast, labels, keyboard, focus.
- A clickable prototype of the main journey, where the journey is not obvious.

### Tier 3: multi-component product

- A description of each kind of intended user, from conversations with them or from existing data.
- Journeys that run across the web application and the mobile apps, and stay consistent between them.
- The structure of the content and the navigation of the whole product.
- A design system: the styles, the components with their states, and the patterns. All clients use it.
- A prototype that is tested with intended users before it is built.
- Full WCAG level AA, with a plan of how it is tested.
- Rules for the text: the tone, and the terms of the glossary.
- Design for several languages: text that grows in translation, and scripts that run from right to left where they are needed.
- The conventions of each mobile platform.
- The events that show whether a journey works, agreed with the product manager.

### Tier 4: enterprise system

Everything of tier 3, and:

- The design system of the organization. The design uses it, and a deviation is approved.
- Many kinds of users with different permissions and tasks. Each kind sees what its task needs.
- Screens for people who work in the system all day: dense, fast, usable by keyboard, with actions on many items at once. Speed for the trained person matters more than ease for the first visit.
- Accessibility as a legal requirement, for example Section 508 in the United States or EN 301 549 in the European Union, with the evidence for an audit.
- Usability tests with employees of each kind.
- The differences from the legacy system that people know, named for the training.
- One way of working for the designers of all teams.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Asks, through Darwin, who the intended users are and in which situation they use the product. Describes the user journeys and sketches the main screens. Designs what a demo shows. |
| 2. Architecture and design | Designs the screens, the navigation, the states and the accessibility. Tests the design. |
| 3. Planning | Not involved. The design of a release is finished before its Implementation starts. |
| 4. Implementation | Clarifies the design. Designs a state that was missed. Reviews the built screens. |
| 5. Verification | Checks the screens against the design and the accessibility requirements. |
| 6. Release | Not involved. |
| 7. Operation and maintenance | Not involved. Feedback about the usability returns to Discovery or to Architecture and design. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The idea brief | The user journeys |
| The requirements specification, with the glossary | The map of the screens and the sketches |
| The brand of the Dreamer: logo, colors, photos, texts | The user interface design: every screen with its states |
| The component library that the software architect chose | The styles and the components |
| The built screens | The results of the design tests |
| The feedback and the usage data | The review of the built screens |

## Works with

- **Product manager.** They share the picture of the intended users. A screen does not add a capability that is not in the scope.
- **Business analyst.** Every requirement that a person can see has a place on a screen. Every element on a screen traces to a requirement.
- **Software architect and developer.** They say what the chosen technology makes easy and what it makes expensive. The designer asks before designing a custom component.
- **QA engineer.** They agree on what is checked: the states, the screen sizes, the accessibility.
- **Technical writer.** The text in the product and the text in the documentation use the same words.
- **Darwin and the Dreamer.** The Dreamer sees the look early, in a demo. The designer gives Darwin two versions to show, not ten, and names the details that are still provisional.

## Checks

The output of the role is complete when all of these are true:

- Every journey can be completed with the designed screens. No step is missing.
- Every screen has all its states: empty, loading, error and success.
- Every element on a screen traces to a requirement, and every requirement that a person can see appears on a screen.
- The main action of each screen is clear at first sight.
- The design works on the smallest screen that the requirements name.
- Contrast, labels and keyboard use meet the accessibility target.
- The texts use the terms of the glossary. An error message says what happened and what to do.
- The same thing looks the same and works the same everywhere.
- The design was made with real content.
- The Dreamer saw the look in a demo and confirmed it before the release was built.
- No detail that the Dreamer confirmed was changed without the Dreamer.

## Common mistakes

- **Designing only the full, happy screen.** The first thing a new person sees is the empty state, and the next is an error.
- **Placeholder text.** The real headline has three times the length, and the layout breaks.
- **Decoration over the task.** An animation or a carousel that slows down the one action the page exists for.
- **A custom component where the library has one.** It costs time to build, and its accessibility has to be built again.
- **The desktop first, for a product that is used on phones.**
- **Accessibility at the end.** Contrast and structure are decisions of the first sketch.
- **Adding features through the design.** A dashboard that nobody asked for is a scope change.
- **A design that the chosen technology cannot build at a fair cost.** Ask before the Dreamer has approved it.
