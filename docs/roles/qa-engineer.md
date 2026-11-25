# QA engineer

The QA engineer answers for the proof that an increment meets its acceptance criteria. The role answers one question: does it do what the requirements say, and what happens when it is used in a way that nobody planned?

The role is independent of the developer. The principle "the author does not approve" means that the developer and the QA engineer are never the same performer, at any tier.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- In Discovery, check that every acceptance criterion can be tested: it names something that can be observed, and an exact expected result.
- In Architecture and design, check that the solution can be tested: the environments, the test data, and stand-ins for the external services.
- Write the test plan: the kinds of tests, the level of each, the environments, the test data, the tools, and what is not tested and why.
- Derive the tests from the requirements: at least one test for each acceptance criterion, and more for the limits, the wrong inputs, the permissions and the states.
- Automate the integration tests, the end-to-end tests and the acceptance tests. Keep them fast and reliable.
- Automate the BDD scenarios of the [confirmed points](../dream-context.md#from-a-confirmed-point-to-a-test) first, and run them on every later change. A scenario that fails is a defect. It is not changed to make it pass.
- Where the solution uses an AI model, run the evaluations that the [AI architect](ai-architect.md) designed. Report the share of the examples that passed, against the threshold.
- Explore the product without a script, like a hurried, a careless and a hostile person would use it.
- Test the quality attributes that the tier requires: performance, accessibility, the supported browsers and devices, and security together with the security architect.
- Record each defect: the steps to reproduce it, the expected and the actual result, the evidence, and the severity.
- Test each fix again. Run the regression tests, to see that the fix broke nothing else.
- Write the test report: the result for each criterion and each quality target, the open defects, and a plain statement of ready or not ready.
- Run the smoke tests in production after a release.
- Keep the regression tests current. Repair or remove a test that fails at random.
- Keep the trace between each requirement and its tests.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| The test plan: what is tested, how and where | The right behavior: the requirement. A gap is a question to the business analyst. |
| Whether a test passed | Whether the increment is accepted: the Dreamer |
| The severity of a defect, and whether it blocks the release | The order in which defects are fixed: the tech lead |
| When the testing is enough to report | An exception to an acceptance criterion: the Dreamer |
| | Whether a security finding blocks the release: the security architect |
| | A change to the BDD scenario of a confirmed point: the Dreamer, through Darwin |

## When the role is engaged

The role is engaged at every tier. It has no triggers. It is never combined with the developer.

| Tier | Engagement |
| --- | --- |
| 1 | Engaged |
| 2 | Engaged |
| 3 | Engaged |
| 4 | Engaged, with specialists for performance tests and security tests |

## Depth by tier

### Tier 1: static site

The output is a checklist with a result for each line. It is run on the demo of the finished site, and again on the published site.

- Every point that the Dreamer confirmed after a demo.
- Every link.
- Every form, with a real submission and with wrong input.
- The display on a phone, a tablet and a desktop, in the main browsers.
- The spelling, and the facts against the content that the Dreamer gave: names, prices, telephone numbers, opening hours, addresses.
- Every image loads and has a text alternative.
- The loading speed, measured with a public tool.
- Accessibility: an automatic check, and one pass through the page with the keyboard only.
- The page title, the description, and the preview when the page is shared.
- HTTPS, and the redirect from HTTP.
- The checklist items of the architecture note, such as the security headers and the privacy notice.

### Tier 2: small application

- A test plan of one page.
- Automated integration tests for every endpoint.
- A few automated end-to-end tests for the main journeys.
- An acceptance test for each acceptance criterion.
- An automated BDD scenario for each confirmed point, run in the pipeline.
- One session of testing without a script in each release.
- Permission tests: each kind of user tries what it is not allowed to do.
- The forms with values at the limits and with wrong input.
- A list of the browsers and devices that are checked.
- The basic accessibility checks.
- The checks of the security baseline, from the list of the security architect.
- Test data that a script creates, so that every run starts the same.
- A test report of one page, and a smoke test after each deployment.

### Tier 3: multi-component product

- A test strategy by level: unit tests by the developers, then component tests, contract tests, integration tests, and a small number of end-to-end tests.
- Test environments, and test data that is generated or made anonymous.
- Performance tests against the targets: at the expected load, above it, and over a long time.
- Security tests, planned with the security architect: the scans, and the penetration test.
- Tests of failure: a component or an external service is stopped, and the behavior is checked.
- A matrix of the browsers and devices for the web application and the mobile apps.
- A full accessibility check against WCAG level AA.
- Regression tests in the pipeline, inside a time budget.
- Tests of the migration and of the rollback.
- A defect process: defined severities, and a regular meeting that assesses new defects.
- Measures: the share of requirements that have tests, the trend of the defects, the defects that were found only in production.
- For mobile apps: tests through the pre-release channels of the app stores.

### Tier 4: enterprise system

Everything of tier 3, and:

- User acceptance testing with the people of the organization: scripts, sessions, and a sign-off for each domain.
- Test management with a trace from each requirement to its tests and their results, as audits ask for it.
- Integration tests with the other systems of the organization, in their test environments and in the time slots they give.
- Tests of whole business processes across several systems.
- Tests of the migration: trial runs, with a reconciliation of the data after each one.
- Performance tests at the scale of production.
- Tests of the failover and of the recovery.
- A penetration test by an independent party.
- Compliance tests, with the evidence kept.
- Specialists for performance tests and security tests.
- Test data that follows the data protection rules of the organization.
- Entry and exit conditions for each test stage, agreed in writing.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Checks that every acceptance criterion can be tested. |
| 2. Architecture and design | Checks that the design can be tested. Names the environments and the test data that the tests will need. |
| 3. Planning | Writes the test plan. |
| 4. Implementation | Automates the integration tests and the acceptance tests, with the BDD scenarios of the confirmed points, while the code is written. |
| 5. Verification | Accountable for the phase. Runs the tests, with the BDD scenarios of all confirmed points. Records the defects and writes the test report. |
| 6. Release | Runs the smoke tests in production. |
| 7. Operation and maintenance | Runs the regression tests of the maintenance releases, with the BDD scenarios of the confirmed points. Adds a test for each defect that was found in production. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The requirements specification, with the acceptance criteria | The test plan |
| The user interface design | The tests, automated and manual |
| The architecture description, with the contracts | The defect reports |
| The delivery plan | The test report |
| The increment and the release candidate | The result of the smoke tests |
| The fixes of the defects | The regression tests |

## Works with

- **Business analyst.** The QA engineer checks the acceptance criteria before the scope is approved. An unclear criterion is cheaper to correct then than in Verification. The business analyst writes the BDD scenarios of the confirmed points. The QA engineer automates them.
- **Developer.** The developer writes the unit tests. The QA engineer does not repeat them, and tests what lies between and above the units.
- **Tech lead.** The QA engineer sets the severity of a defect. The tech lead sets the order of the fixes.
- **Security architect.** They agree on the security tests. The QA engineer tries to do what the controls forbid.
- **Infrastructure architect.** The architect defines the load test, the failover test and the restore test. The QA engineer runs them with the DevOps engineer.
- **AI architect.** The architect designs each evaluation: the examples, the measure and the threshold. The QA engineer runs it and reports the result. A confirmed point about the behavior of a model is checked by examples, not by one exact scenario.
- **UX designer.** They agree on the states, the screen sizes and the accessibility checks.
- **DevOps engineer.** The DevOps engineer provides the environments and runs the tests in the pipeline.
- **Product manager and Darwin.** The product manager checks the increment against the scope. Darwin shows an increment to the Dreamer only after the QA engineer has checked it.

## Checks

The test report is complete when all of these are true:

- Every acceptance criterion of the release has a result: passed, failed, or not tested with the reason.
- Every BDD scenario of a confirmed point has a result, also the scenarios of the earlier releases.
- Every quality target that the tier requires has a measured result.
- Every failed test has a defect. Every defect has steps, an expected result, an actual result and a severity.
- Every fixed defect was tested again, and a test now guards against it.
- The tests ran against the exact version that is the release candidate. The report names the version.
- The report names the environment and the test data.
- What was not tested is listed, with the reason and the risk.
- Another performer who runs the same tests gets the same result.
- The report says plainly: ready or not ready, and why.

## Common mistakes

- **Testing only what the criteria say.** The criteria describe what should work. Defects live in what nobody described.
- **Deciding the right behavior alone, where the requirement is silent.** That is a question for the business analyst.
- **Changing the scenario of a confirmed point because the product changed.** The scenario holds what the Dreamer confirmed. The product is wrong until the Dreamer says otherwise.
- **"All tests pass", without saying what was not tested.**
- **Reporting a check that was not run.** A test that was not run is reported as not run.
- **An end-to-end test for everything.** The tests become slow and fragile. Most checks belong at a lower level.
- **Tests that fail at random and stay.** People learn to ignore a red result.
- **A defect report without steps.** The developer cannot reproduce the defect, and it comes back as "works for me".
- **A softer result because the date is near.** The report states what is true. The Dreamer decides what to do with it.
- **Testing another version than the one that is released.**
