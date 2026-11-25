# Site reliability engineer

The site reliability engineer answers for the running solution. The role answers one question: does the solution work for its users right now, and will it still work next month?

The role starts where the release ends. It watches the solution, responds when it fails, and brings what it learns back to the roles that design and build.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Review the design for operation: what can be monitored, how each part fails, and how it recovers.
- Turn the quality targets into measures of the running solution, together with the solution architect: what is measured, and which value is good enough.
- Set up the monitoring: availability, response time, errors, and how full each limited resource is.
- Monitor from the outside as well: a check that walks through a main journey like a user.
- Set up the alerts. An alert reports a problem that users notice, asks for an action, and names its runbook.
- Write the runbooks and keep them current.
- Check before a release that the solution is ready to be operated.
- Watch each release, with the criteria for a rollback agreed before the deployment.
- Handle incidents: notice, restore the service first, find the cause afterwards. Give Darwin what happened, for the Dreamer.
- Write a review of each incident, without blame: the timeline, the cause, and the actions with their owners. Follow the actions until they are done.
- Watch the capacity and its trends. Act before a limit is reached.
- Check that the backups run. Try a restore at a fixed rhythm.
- Watch the dates that end something: domains, certificates, keys, contracts.
- Watch the running cost, with the infrastructure architect.
- Automate the operations that are done by hand again and again.
- Report the service levels to the product manager, and through Darwin to the Dreamer.
- Shut the solution down when it is retired.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| What is monitored and when an alert fires, inside the observability design | The quality targets: the solution architect and the Dreamer |
| How an incident is handled: the steps to restore the service, including a rollback | The observability tools and the recovery design: the infrastructure architect |
| Whether the solution is ready to be operated | Go-live: the Dreamer |
| The content of the runbooks | The fix of a cause in the code: the tech lead and the developers |
| | Reliability work against new features: the product manager and the Dreamer, on the recommendation of this role |

## When the role is engaged

| Tier | Engagement |
| --- | --- |
| 1 | Covered by the developer, with the checklist below |
| 2 | Covered by the DevOps engineer, with the checklist below |
| 3 | Engaged |
| 4 | Engaged |

Triggers that engage the role at tier 1 or 2:

- An availability target with a number.
- Someone has to respond outside working hours.
- A service level is promised in a contract.
- Downtime means a direct loss, for example lost bookings or lost sales.

## Depth by tier

### Tier 1: static site

The role is covered. The developer works through this checklist:

- An uptime check from the outside, every few minutes, that tells a named person when the site is down.
- The domain renews itself, with a valid means of payment, and a named person is told before it expires.
- The certificate renews itself.
- A test submission of each form at a fixed rhythm. A form that stopped delivering shows no error.
- A note on how to publish the previous version again.
- The contact of the host, for a problem that is on their side.

### Tier 2: small application

The role is covered, unless a trigger engages it. The DevOps engineer works through this checklist:

- A health endpoint that checks the application and the database.
- An uptime check, with an alert to a named person.
- Error tracking, with an alert on a new error and on a rising rate of errors.
- Logs that can be searched in one place, kept for a stated time.
- One dashboard: requests, errors, response time, the size of the database.
- Daily backups. A restore that was tried, and is tried again after a large schema change.
- Alerts on a failed backup, on storage that is nearly full, and on a certificate that is about to expire.
- A runbook of one page: how to deploy, to roll back and to restore, and whom to call.
- A budget alert.
- Updates of the dependencies on a schedule, and at once for a critical vulnerability.
- A short note after each outage: what happened, and what was changed.

### Tier 3: multi-component product

- A service level objective for each service that users touch, taken from the quality targets, with the amount of failure that is still acceptable.
- A dashboard for each objective.
- Alerts on the objective: on how fast the acceptable failure is used up, not on every single cause.
- Traces that follow a request across the components.
- Checks from the outside that walk through the main journeys.
- An on-call duty, with a path to the next person when the first does not answer.
- An incident process: roles, severities, communication to the users, a review within days, and tracked actions.
- A runbook for each alert.
- A readiness review before the first release of each component.
- Regular capacity reviews.
- A checked behavior under overload: the solution sheds work in a planned way and does not collapse.
- Restore tests and failover tests on a schedule.
- Exercises in which a failure is caused on purpose.
- A watched release, with criteria that roll it back automatically.

### Tier 4: enterprise system

Everything of tier 3, and:

- Contractual service levels: the measurement, the report, and the consequences.
- Operation inside the processes of the organization: its service desk, its incident and problem management, its register of systems, and its procedure for a major incident.
- Support around the clock, in shifts.
- Recovery drills together with the organization, and a part in its business continuity plans.
- The evidence that audits ask for: access logs and change records of the operation.
- Capacity planning for a year ahead, with the budget.
- A formal acceptance by the operations department of the organization.
- Maintenance windows that are announced.
- The contacts at each vendor for a problem that needs them.
- Regular operational reports to the management.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Not involved. |
| 2. Architecture and design | Checks that the solution can be operated: what is monitored, and how it fails. |
| 3. Planning | Not involved. |
| 4. Implementation | Not involved. At tiers 3 and 4, starts to build the monitoring while the components are built. |
| 5. Verification | Checks that the solution is ready to be operated: monitoring, alerts, runbooks. |
| 6. Release | Sets up the monitoring and the alerts. Watches the release. Owns the runbooks. |
| 7. Operation and maintenance | Accountable for the phase. Monitors the solution, handles incidents and watches the capacity. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The quality targets | The monitoring and the alerts |
| The architecture description: infrastructure design, observability | The service level objectives, and the reports on them |
| The release candidate and the steps of the release | The runbooks |
| The metrics, the logs and the alerts | The result of the readiness check |
| The incidents | The incident reports |
| The bills and the limits of the services | Observations on capacity and cost, and proposals for reliability work |

## Works with

- **Infrastructure architect.** The architect designs the observability and the recovery. The site reliability engineer operates them, and reports what the running solution shows.
- **DevOps engineer.** They agree on the monitoring, the alerts and the rollback before a release. At tier 2 they are one performer.
- **Tech lead and developer.** The cause of an incident is often in the code. They agree on what the code writes to the logs and reports as metrics.
- **Product manager.** The site reliability engineer reports the service levels. When the solution fails too often, the choice between reliability work and new features goes to the Dreamer through Darwin.
- **Security architect.** A security incident follows the plan of the security architect. They review together who has access to production.
- **Technical writer.** The writer makes the runbooks clear for someone under time pressure.
- **Darwin.** Darwin tells the Dreamer about each incident in plain words: what happened, who was affected, and what was done. The site reliability engineer gives Darwin the facts.

## Checks

The output of the role is complete when all of these are true:

- Every quality target for availability and performance has a measurement.
- A failure that users notice triggers an alert. This was tried by causing the failure.
- Every alert names a runbook and reaches a named person.
- Every runbook was followed once by someone who did not write it.
- The backups run, and a restore was tried inside the agreed period.
- The criteria for a rollback are set before each deployment.
- Every incident has a written review with its cause and its actions, and every action has an owner.
- Every date that ends something is watched: domains, certificates, keys, contracts.
- The free capacity of every limited resource is known.
- The Dreamer was told about every incident that affected the users of the solution.

## Common mistakes

- **Monitoring the servers and not the experience of the users.** Every dashboard is green while nobody can sign in.
- **Alerts that nobody acts on.** After a week, the one that matters is ignored with the rest.
- **Looking for the cause while the users wait.** Restore the service first, for example with a rollback. Analyze afterwards.
- **An incident review that names a person as the cause.** The next person hides the next mistake. The question is what made the mistake possible.
- **Actions from a review that are never done.** The same incident returns.
- **A backup that was never restored.**
- **Watching only for crashes.** The quiet failures do the most harm: a form that stopped delivering, a job that stopped running, a certificate that expires on Sunday. Monitor that things happen, not only that nothing breaks.
- **One performer who knows how it all works.** What is not in a runbook is lost with that performer.
