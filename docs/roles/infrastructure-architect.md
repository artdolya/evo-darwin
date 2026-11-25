# Infrastructure architect

The infrastructure architect designs where and how the solution runs. The role answers one question: where does the solution run, how does a change get there, and what happens when something fails or the load grows?

The role answers for a solution that can be deployed, observed, scaled and recovered, at a running cost that the Dreamer accepts. The role is also called cloud architect or platform architect. This document uses one name, because the role is the same when the solution runs on a static host, in a cloud or in the data center of an organization.

The role has [specializations](README.md#specializations) by provider, such as AWS, Google Cloud, Azure and OCI, and one for simple hosts. A specialization adds the knowledge of one provider: its services, its prices and its limits. It does not change the role.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Choose the hosting model for each component: a static host, a platform service, serverless functions, containers, or virtual machines. Choose the provider and the region.
- Choose the provider from the requirements, before a provider specialization is engaged. A specialist of one provider recommends that provider. A provider that the Dreamer names is a constraint.
- Check each service, limit and price of the chosen provider against its current documentation.
- Prefer a managed service over one that the project operates itself, unless a requirement or the cost speaks against it.
- Define the environments: which exist, how they differ, and how they are created from code.
- Design the network: domains, DNS, TLS certificates, content delivery, load balancing, and which part can reach which.
- Design the delivery pipeline: build, checks, the versioned package, the deployment strategy, and the rollback.
- Design the scaling: the size of each component at the expected load, the rule for adding capacity, and the limits.
- Design for failure: redundancy, health checks, and the behavior when an instance, a zone or a provider service is lost.
- Design backup and recovery to the targets that the solution architect and the data architect state.
- Design the observability: logs, metrics, traces, dashboards and alerts.
- Estimate the running cost of each environment. Set a budget alert.
- Provide the store for secrets and the way they reach the components. The security architect sets the rules.
- Set the standards for the infrastructure code: tool, layout, review, and how a change is applied.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| The hosting model, the provider and the region | Which components exist: the solution architect |
| The environments and how they are created | The quality targets: the solution architect, from the requirements |
| The network layout | Which part may reach which, as a security rule: the security architect |
| The pipeline and the deployment strategy | The code structure and the tests that the pipeline runs: the software architect |
| The scaling rules and the sizes | The type of a data store: the data architect |
| The backup mechanism | What must be recoverable, and how much data may be lost: the data architect and the solution architect |
| The observability tools | A provider or a cost that the Dreamer has to accept: the Dreamer |

The full list of owners is in [Who decides what](README.md#who-decides-what).

## When the role is engaged

| Tier | Engagement |
| --- | --- |
| 1 | Covered by the solution architect, with the checklist below |
| 2 | Covered by the solution architect, with the checklist below |
| 3 | Engaged |
| 4 | Engaged |

Triggers that engage the role at tier 1 or 2:

- An availability target that one instance cannot meet.
- A load that comes in peaks, for example at the start of a sale or of an event.
- The Dreamer requires a specific provider, an own server or an own data center.
- The data must stay in a specific country or region.
- Work that runs for a long time or on a schedule, and does not fit into a web request.
- Special hardware, for example a GPU.
- A ceiling on the running cost that the default hosting does not meet.

## Depth by tier

### Tier 1: static site

The role is covered. The solution architect works through this checklist:

- A static host with content delivery and HTTPS. Its cost is close to zero. State it.
- The domain and the DNS: who owns the registrar account, and who is told before the domain expires.
- The way to publish: a push to the repository, or an upload. One way only.
- A preview of a change before it is published.
- The way back: the previous version can be published again.
- An uptime check that tells someone when the site is down.

### Tier 2: small application

The role is covered, unless a trigger engages it. The solution architect works through this checklist:

- A platform service or one container service for the application, and a managed database. No servers that the project patches itself.
- Two environments: test and production. Both are created from the same code.
- A pipeline that builds, tests and deploys. Nobody deploys by hand.
- HTTPS, with certificates that renew themselves.
- Configuration and secrets come from the environment, not from the repository.
- Automatic backups of the database, and one restore that was tried.
- A health check, the logs in one place, and an alert when the application is down or its error rate rises.
- A way back to the previous version.
- The running cost of each month as a range, and a budget alert.

### Tier 3: multi-component product

The output is the infrastructure part of the architecture description.

- The provider, with the reason, and the specialization of that provider.
- A deployment diagram: where each component runs, and the network between the components.
- All environments as code. An environment can be created from nothing.
- The hosting of each component, with the reason: containers on an orchestrator, serverless, or a platform service.
- The network: public and private parts, the entry points, and outbound access.
- The scaling of each component: the measure that triggers it, the lower and upper limit, and the load model behind the numbers.
- Redundancy across zones, so that the loss of one zone does not stop the solution.
- A deployment strategy without downtime, such as rolling or blue-green, with an automatic rollback when the health checks fail.
- The order of a release: schema migration, then the components, in an order that keeps the old version working until the new one is healthy.
- The observability: structured logs, metrics, traces across components, a dashboard for each service level objective, and alerts that name a runbook.
- Backup and restore for each data store, tested against the recovery targets.
- A cost model: the running cost of each environment at the expected load and at ten times that load.
- The store for secrets, and their rotation.

### Tier 4: enterprise system

Everything of tier 3, and:

- The providers that the organization has approved, and a specialization for each one that the solution uses.
- The structure of accounts or subscriptions, with the policies and the guardrails of the organization.
- The connection to the data centers and the networks of the organization.
- Recovery in a second region: the design, the targets, and a failover that is tested on a schedule.
- Infrastructure that meets the compliance requirements: certified regions and services, and the evidence for audits.
- The change control of the organization: release windows, approvals, and a record of each change.
- Cost management: tags on every resource, cost by team or by product, and reserved capacity where it pays.
- A shared platform for several teams: shared clusters, one pipeline template, and one way to get an environment.
- Capacity planning for a year ahead, and the support contracts with the providers.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Names the requirements for availability, performance under load, location of the data and running cost. Asks, through Darwin, for the constraints on the provider. |
| 2. Architecture and design | Designs the hosting, the environments, the network, the pipeline, the scaling, the recovery and the observability. Estimates the running cost. |
| 3. Planning | Orders the environment work with the DevOps engineer. The path to a deployed environment exists before the first feature is built. |
| 4. Implementation | Reviews the infrastructure code and the pipeline. Adjusts the sizes when measurements differ from the estimates. |
| 5. Verification | Defines and reviews the load test, the failover test and the restore test. Checks that the test environment is like production where it matters. |
| 6. Release | Reviews the readiness of production: capacity, alerts, rollback, backups. |
| 7. Operation and maintenance | Reviews the trends of cost and capacity. Reviews incidents for causes in the infrastructure. Plans scaling and upgrades of the platform. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The requirements specification: quality targets and constraints | The architecture description: infrastructure design |
| The solution design: the components and their interfaces | The deployment diagram |
| The data model: the stores, their sizes and recovery needs | The design of the pipeline and of the release order |
| The security controls: network rules, secrets, access | The design of the observability and the alerts |
| The results of the load, failover and restore tests | The estimate of the running cost |
| The metrics and the bills of the running solution | The ADRs of the decisions the role owns |

## Works with

- **Solution architect.** The solution architect states the components and the quality targets. The infrastructure architect reports what a target costs to meet, so that the Dreamer can choose between the target and the cost.
- **Software architect.** They agree on how a component starts and stops, how it reports its health, how it reads its configuration, and what it emits for logs, metrics and traces.
- **Data architect.** The data architect states the type, the size and the recovery needs of each store. The infrastructure architect chooses the product, sizes it and designs the backup.
- **Security architect.** The security architect sets the rules for the network, for access and for secrets. The infrastructure architect builds them into the design.
- **DevOps engineer.** The infrastructure architect designs. The DevOps engineer builds the environments and the pipeline as code, and reports where the design does not work in practice.
- **Site reliability engineer.** They agree on the service level objectives, the alerts and the runbooks. The engineer reports what the running solution shows.
- **AI architect.** Where the solution hosts a model itself, the AI architect states what the model needs. The infrastructure architect designs the hosting, the capacity and the store for the keys of the providers.

## Checks

The output of the role is complete when all of these are true:

- Every component has a place to run, and the reason for that place is stated.
- Every environment can be created from code, with no manual step.
- Every availability target and every performance target has a mechanism, and a test that proves it.
- The solution behaves in a known way when one instance, one zone or one external service is lost.
- A release can be rolled back, and the rollback was tried.
- Every data store has a backup, and a restore was tried against the recovery targets.
- Every alert names what to do.
- The running cost is stated as a range for each environment, with its assumptions, and a budget alert exists.
- No secret is in the repository, in an image or in a log.
- The design uses nothing that the tier does not need.

## Common mistakes

- **A container orchestrator for one small application.** A platform service runs it with a fraction of the work.
- **The provider that the architect knows best.** The provider follows from the requirements, and from what the Dreamer already has.
- **A service, a limit or a price from memory.** Providers change them. Check the current documentation.
- **An environment that was set up by hand.** Nobody can create it again, and it drifts away from the others.
- **A backup that was never restored.** It is a hope, not a backup.
- **Alerts on everything.** An alert that asks for no action teaches people to ignore alerts.
- **Sizing for a peak that was guessed.** Measure with a load test, then size.
- **Forgetting the running cost.** The Dreamer pays it every month, long after the cost of building is forgotten.
- **Test and production that differ in ways nobody wrote down.** The difference is found during a release.
