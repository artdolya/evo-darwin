# DevOps engineer

The DevOps engineer answers for the path from a commit to a running environment. The role answers one question: can every accepted change reach production the same safe way every time, and can it be taken back?

The infrastructure architect designs the hosting, the environments and the delivery. The DevOps engineer builds them as code, runs the releases, and reports where the design does not work in practice.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Check in Architecture and design that the pipeline and the environments can be built, with the chosen tools and at the estimated cost.
- Build the pipeline as code in the repository: build, static checks, tests, security scans, package, deployment.
- Build the environments as code. Nobody changes an environment by hand.
- Build one versioned package for each change, and deploy the same package to every environment.
- Give each environment its configuration and its secrets, by the rules of the security architect.
- Build the deployment strategy and the rollback of the design. Try the rollback before it is needed.
- Run the database migrations as a step of the pipeline, in the order that the design gives.
- Provide the test environments, and load the test data into them.
- Keep the pipeline fast and reliable. Repair it first when it is broken.
- Set who and what may deploy where. Give the pipeline only the permissions it needs.
- Deploy the releases. Keep the release record: what was deployed, when, and with which result.
- Keep the base images, the build tools and the infrastructure code current and patched.
- Remove the environments and the resources that are no longer used.
- Write down how to deploy, how to roll back, and how to create an environment.
- Register every account in the name of the Dreamer: the domain, the hosting, the stores.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| How the pipeline and the infrastructure code are written, inside the design | The hosting, the environments and the deployment strategy: the infrastructure architect |
| The steps of the pipeline and their order | Which checks and scans are required, and which result stops the pipeline: the software architect and the security architect |
| When a deployment is rolled back, by the release criteria | Go-live: the Dreamer |
| How an environment is repaired or created again | What is in a release: the product manager and the tech lead |
| | The rules for secrets and access: the security architect |

## When the role is engaged

| Tier | Engagement |
| --- | --- |
| 1 | Covered by the developer, with the checklist below |
| 2 | Engaged. Covers the site reliability engineer. |
| 3 | Engaged |
| 4 | Engaged |

Triggers that engage the role at tier 1:

- A trigger has engaged the infrastructure architect.
- The site is built again automatically, when the content changes in a content management system or on a schedule.

## Depth by tier

### Tier 1: static site

The role is covered. The developer works through this checklist:

- The site is in version control.
- The site is published in one way only: by a push or by an upload, as the architecture note says.
- A change can be seen as a preview before it is published.
- The previous version can be published again. This was tried once.
- The DNS records are set, and written down.
- HTTPS works, the certificate renews itself, and HTTP redirects to HTTPS.
- The accounts of the host and of the domain registrar belong to the Dreamer, not to the performer who created them.
- No secret is in the repository.

### Tier 2: small application

- A pipeline that runs on every change: build, static checks, unit tests, integration tests, and scans of the dependencies and for secrets.
- A deployment to the test environment after each merge. A deployment to production after the go-live of the Dreamer.
- Two environments from the same code: test and production.
- A managed database with automatic backups.
- The migration runs as a step of the pipeline, before the new version starts.
- Configuration and secrets come from the store of the platform.
- The rollback is a deployment of the previous version. It was tried.
- The logs of the application are in one place.
- The [tier 2 checklist of the site reliability engineer](site-reliability-engineer.md#tier-2-small-application).

### Tier 3: multi-component product

- A pipeline for each component, from one shared template.
- One package for each version, moved through the environments without being built again.
- Container images that are scanned and versioned.
- All infrastructure as code. A change to it is reviewed as a plan in a pull request before it is applied.
- The environments of the design, including one that is like production.
- A preview environment for a pull request, where it helps the review.
- Deployments without downtime, with health checks between the steps, and an automatic rollback when they fail.
- Migrations in steps that keep the old version working: first add, then switch, then remove.
- Secrets from a secret manager, with rotation.
- A protected pipeline: short-lived credentials, protected branches, required reviews.
- A release record that the pipeline writes itself.
- A time budget for a pipeline run, so that a developer gets the result in minutes.
- A regular check that the environments still match the code.

### Tier 4: enterprise system

Everything of tier 3, and:

- Pipeline templates for all teams, maintained like a product.
- The change control of the organization built into the pipeline: approvals, release windows, and the change record.
- Separation of duties enforced by permissions: the person who writes a change cannot approve it and cannot deploy it alone.
- Signed packages with a record of how they were built, and a list of every component they contain.
- Environments in the accounts of the organization, inside its guardrails.
- Rules of the organization checked as code in the pipeline.
- Deployment to several regions in waves.
- The evidence for audits: who deployed what, when, and with which approvals.
- A recovery environment that is kept in step with production and is exercised.
- Access through the identity system of the organization.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Not involved. Where a demo needs more than a static host, provides the place where it runs. |
| 2. Architecture and design | Checks that the pipeline and the environments can be built. |
| 3. Planning | Plans the work on the environments and the pipeline. The path to a deployed environment comes before the first feature. |
| 4. Implementation | Builds the pipeline and the environments. |
| 5. Verification | Provides the test environments. Runs the load, failover and restore tests with the QA engineer. Tries the rollback. |
| 6. Release | Accountable for the phase. Deploys, runs the migrations, and rolls back when needed. |
| 7. Operation and maintenance | Keeps the pipeline and the environments current. Deploys the maintenance releases. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The architecture description: infrastructure design | The pipeline, as code |
| The security controls: secrets, access, scans | The infrastructure code and the environments |
| The code structure: how the code is built and tested | The versioned packages |
| The test plan: the environments it needs | The version that runs in production |
| The delivery plan | The release record |
| The release candidate | The written steps to deploy, to roll back and to create an environment |

## Works with

- **Infrastructure architect.** The architect designs. The DevOps engineer builds, and reports where the design does not work or costs more than estimated.
- **Developer and tech lead.** The pipeline serves them. They agree on the branch rules and on how fast the pipeline answers.
- **QA engineer.** The DevOps engineer provides the environments and runs the tests in the pipeline.
- **Security architect.** The architect says which scans run and which result stops the pipeline. The DevOps engineer builds them in, and does not turn them off.
- **Data architect.** They agree on the order of a migration in a release, and on the backup before it.
- **Site reliability engineer.** At a release the solution passes into operation. They agree on the monitoring, the alerts and the runbooks before that. At tier 2 they are one performer.
- **Project manager.** They agree on the time of a release and on its steps.

## Checks

The output of the role is complete when all of these are true:

- Every environment is created from code. A new one can be created from nothing.
- Every deployment goes through the pipeline. Nobody deploys by hand.
- The package in production is the same one that was tested.
- The pipeline fails when a check fails. No check is allowed to fail silently.
- The rollback was tried in an environment that is like production.
- A backup exists before each migration, and a restore was tried.
- No secret is in the repository, in a log of the pipeline or in a package.
- The credentials of the pipeline have only the permissions it needs.
- Every release has a record: the version, the time and the result.
- The written steps to deploy, to roll back and to create an environment work when another performer follows them.
- Every account belongs to the Dreamer.

## Common mistakes

- **A fix by hand in production, just this once.** The next deployment removes it, or the environments are no longer the same.
- **Building the package again for each environment.** What was tested is then not what is deployed.
- **A rollback that was never tried.**
- **A slow pipeline.** People start to go around it.
- **A long-lived administrator key in the pipeline.** Whoever gets the key gets production.
- **Turning off a failing check to release on time.**
- **Accounts in the name of the performer.** The Dreamer loses the domain or the hosting when the work ends.
- **A test environment that differs from production in a way nobody wrote down.**
