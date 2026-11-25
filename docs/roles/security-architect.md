# Security architect

The security architect makes sure that the solution protects its users, its data and itself, in proportion to the risk. The role answers one question: what can go wrong, who could cause it, and what stops them?

The role answers for the security controls of the solution and for the compliance with the rules that apply to it. It does not accept risk in the name of the Dreamer. It describes each remaining risk so that [Darwin](darwin.md) can explain it in plain words, and the Dreamer decides.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Classify the data and the other assets: what needs protection, and from whom.
- Write the threat model of the design: the trust boundaries, the entry points, the threats, and the control against each threat.
- Design authentication: an established identity provider or library, sessions, and a second factor where the risk asks for it. The solution never builds its own password handling when a proven one exists.
- Design authorization: the roles and permissions, where they are checked, and how the data of one customer is kept apart from the data of another.
- Set the protection of the data: encryption in transit and at rest, the handling of keys and secrets, and personal data that stays out of logs.
- Set the security requirements for the code: validation of input, encoding of output, safe handling of uploads, limits on the rate of requests. A public standard is the baseline, such as the OWASP Application Security Verification Standard (ASVS).
- Set the checks in the pipeline: scans of the code, of the dependencies, of the container images, and for secrets in the repository. Say which finding stops the pipeline.
- Set the rules for the infrastructure: who may reach what in the network, the smallest set of permissions for each component and each person, and patching.
- Find the laws and standards that apply, such as GDPR, PCI DSS or HIPAA. Map each one to the controls that meet it.
- Design the security logging: which events are recorded for audit, who is alerted, and what happens in an incident.
- Define the security tests. Review their results and follow each finding until it is closed.
- Where the solution itself calls an LLM: design the controls against instructions hidden in the input, and against data that leaks through the model.
- Keep the list of the remaining risks. Give each one to Darwin, who presents it to the Dreamer for a decision.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| The class of each kind of data, and the protection of each class | Which data the product collects at all: the product manager and the Dreamer |
| The minimum controls of the tier | The acceptance of a remaining risk: the Dreamer |
| How users are authenticated and authorized | How the controls are placed in the code structure: the software architect |
| The rules for secrets, keys, access and the network | The store for secrets and the network layout that implement the rules: the infrastructure architect |
| Which finding of a scan or a test blocks a release | How long data is kept: the data architect, inside the legal limits |
| Which laws and standards apply | Whether the product enters a market where a law applies: the Dreamer |

Two limits protect the decisions of the role. A minimum control can be waived only by the Dreamer, as a recorded acceptance of the risk. A legal requirement cannot be waived by anyone on the project.

The full list of owners is in [Who decides what](README.md#who-decides-what).

## When the role is engaged

| Tier | Engagement |
| --- | --- |
| 1 | Covered by the solution architect, with the checklist below |
| 2 | Engaged, for a baseline review |
| 3 | Engaged |
| 4 | Engaged |

Triggers that engage the role at tier 1:

- The site takes payments.
- The site collects sensitive personal data: health, finances, identity documents, or data of children.
- A part of the site is behind a sign-in.
- Visitors can upload files or publish content.
- The site embeds a chat or another feature that passes the input of visitors to an LLM.

Triggers that move a tier 2 project from the baseline review to the depth of tier 3:

- A law or a standard with audits applies, such as PCI DSS or HIPAA.
- Several customers share the application, and their data must stay apart.
- The application offers a public API.

## Depth by tier

### Tier 1: static site

The role is covered, unless a trigger engages it. The solution architect works through this checklist:

- HTTPS on every page, with a redirect from HTTP.
- No secret in the repository or in the source of a page. A key in browser code is public.
- The security headers that the host allows, with a content security policy among them.
- As few third-party scripts as possible, each from a source that is trusted, and each pinned to a version.
- A form sends its data to a trusted service and has protection against spam.
- A privacy notice, and a consent banner where the law asks for one, when a form or analytics collects personal data.
- The accounts of the domain registrar and of the host have a second factor and a named owner.
- The tools that build the site are current.

### Tier 2: small application

The output is a baseline review: a threat model of one page, and a list of controls.

- The threat model: the assets, the entry points, and the most likely threats with the control against each.
- Sign-in through an established identity provider or the proven library of the framework. If the application stores passwords, it stores them with a slow, salted hash made for passwords.
- Every permission check runs on the server. Hiding a button is not a control.
- ASVS level 1 as the list of requirements for the code.
- Secrets in the secret store of the platform. None in the repository.
- Scans of the dependencies and for secrets in the pipeline.
- Encryption in transit everywhere, and at rest for the database and the backups.
- Personal data: only what a requirement needs, a privacy notice, and a way to delete the data of one person.
- Payments through the hosted page or the hosted fields of a payment provider, so that card data never touches the application. This keeps most of PCI DSS out of scope.
- An audit record of sign-ins and of changes to permissions.

### Tier 3: multi-component product

The output is the security part of the architecture description.

- A threat model for each component and each trust boundary, made with a method such as STRIDE. Every threat has a control or is on the list of remaining risks.
- ASVS level 2 as the list of requirements for the code.
- The authorization model, including the separation of customers, with tests that try to cross the separation.
- The security of the APIs: authentication between components, schemas for the input, limits on the rate of requests.
- The handling of secrets and keys: where they are stored, who can read them, how they are rotated.
- The scans in the pipeline, with the thresholds that stop it: code, dependencies, container images, infrastructure code, secrets.
- Security logging with alerts, and a runbook for a security incident.
- A penetration test before the first release to production.
- A time limit for fixing a vulnerability, by severity.
- An assessment of the effect on privacy, where the solution processes personal data on a large scale.

### Tier 4: enterprise system

Everything of tier 3, and:

- Each compliance framework that applies, mapped to controls, with the evidence that an audit asks for.
- Integration with the security systems of the organization: its identity system and single sign-on, its central log analysis, its security operations team.
- A network in segments, where no part trusts another because of its location.
- Control of privileged access: who can act as an administrator, for how long, and with which record.
- Separation of duties: the person who writes a change is not the one who approves it or deploys it to production.
- Keys in hardware that the organization controls, where a regulation asks for it.
- An assessment of each vendor whose service handles the data.
- ASVS level 3 for the components where a failure does the most harm.
- A formal risk register, and a sign-off by the security function of the organization.
- Penetration tests and audits on a schedule, not only before the first release.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Classifies the data. Names the compliance and security requirements, and writes them as acceptance criteria. Adds the ways in which the product could be abused. When the idea is in a regulated field such as health, finance or services for children, names early the rules that will shape the project. |
| 2. Architecture and design | Writes the threat model. Designs authentication, authorization and the other controls. Reviews the parts of the other architects. |
| 3. Planning | Checks that the security work and the security tests are in the plan of the release where they are needed, and not in a later one. |
| 4. Implementation | Reviews changes to authentication, authorization, cryptography, input handling, secrets and dependencies. Assesses the findings of the scans. |
| 5. Verification | Reviews the results of the security tests. Decides which findings block the release. Checks that every control of the threat model exists in the built solution. |
| 6. Release | Confirms that no blocking finding is open, and that access and secrets in production are right. Gives Darwin the remaining risks for the Dreamer. |
| 7. Operation and maintenance | Follows new vulnerabilities in the dependencies. Reviews security incidents. Updates the threat model when the solution changes. Reviews who has access. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The idea brief: the field and the market of the product | The classification of the data |
| The requirements specification | The security and compliance requirements |
| The solution design, the code structure, the data model, the infrastructure design | The architecture description: threat model and security controls |
| The changes in review, and the findings of the scans | The mapping of the laws and standards to the controls |
| The results of the security tests | The decision on each finding: blocking or not |
| The incident reports and the new vulnerabilities | The list of remaining risks, for the Dreamer |

## Works with

- **Solution architect.** The security architect sets the controls. The solution architect fits them into the design. When a control conflicts with another quality target, they prepare the options for the Dreamer.
- **Software architect.** The security architect states the rules for authentication, authorization and input handling. The software architect builds them into the structure, so that a developer gets them by default.
- **Data architect.** The security architect sets the class of the data and its protection. The data architect applies the class to each field, and designs retention and deletion.
- **Infrastructure architect.** The security architect sets the rules for the network, for access and for secrets. The infrastructure architect provides the mechanisms.
- **AI architect.** The security architect decides which data may be sent to the provider of a model, and owns the threats of a model: text that tries to change its instructions, data that leaks through an answer, a tool that does more than it should. The AI architect builds the controls into each use of a model.
- **Product manager and business analyst.** A security requirement is a requirement like any other: it has acceptance criteria, and it is in the scope that the Dreamer approves.
- **QA engineer.** They agree on the security tests, and on the tests that try to do what the controls forbid.
- **Darwin and the Dreamer.** The role describes a risk as what could happen, how likely it is, and what it would cost. Darwin explains it. The Dreamer accepts the risk or pays for the control.

## Checks

The output of the role is complete when all of these are true:

- Every kind of data has a class, and every class has its protection.
- Every entry point of the solution is in the threat model.
- Every threat has a control, or is on the list of remaining risks with a decision of the Dreamer.
- Every control is in the design, in a work item and in a test.
- Authentication uses an established provider or library.
- Every permission is checked on the server, and a test tries to pass without the permission.
- No secret is in the repository, in an image, in a log or in browser code.
- Every law and standard that applies is named and mapped to controls.
- The pipeline has the scans of the tier, and the thresholds that stop it are set.
- The remaining risks are written in plain language.

## Common mistakes

- **Starting in Verification.** A missing control that is found by a penetration test costs a redesign. The same control costs a paragraph in Architecture and design.
- **The same controls for every project.** A threat model for a page with opening hours is noise. The checklist of the tier exists so that the work matches the risk.
- **Building authentication.** Sign-in, password storage and session handling have failed in every way already. The proven ones contain the lessons.
- **Controls only in the user interface.** An attacker does not use the user interface.
- **A list of findings without a decision.** Each finding is fixed, or is accepted by the Dreamer, or is shown to be wrong. A finding with no owner stays open forever.
- **Accepting a risk for the Dreamer.** The role can advise. The Dreamer carries the consequence, so the Dreamer decides.
- **Forgetting the people.** The account of the domain registrar with a weak password takes down the best-protected site.
