# Data architect

The data architect designs the data of the solution. The role answers one question: which data do we keep, in which shape, where, and for how long?

The role answers for data that is correct, findable, recoverable, and not kept longer than allowed. Data outlives code: a component can be rewritten in a week, and the data it wrote stays for years. A mistake in the data model is the most expensive one to correct after the first release.

The process, its phases and the tiers are described in [SDLC.md](../SDLC.md).

## Responsibilities

- Describe the business entities and the relations between them, in the terms of the Dreamer. Keep one glossary, so that one word means one thing.
- Design the data model: tables or collections, keys, constraints and indexes.
- Choose the type of data store for each kind of data: relational, document, key-value, search index, object storage, time series. A relational database is the default. Another type needs a reason.
- Make sure that every piece of data has one source of truth. A copy is marked as a copy, with the way it is refreshed.
- Describe the data flows: how data moves between the components, and to and from external systems.
- Define the life of each class of data: how long it is kept, when it is archived, how it is deleted, and what is recorded for audit.
- Define what must stay consistent: inside one transaction, and across data stores that have no common transaction.
- Define how the schema changes: the migration tool, and the rules that let a new version be deployed without downtime.
- Design the migration of data from an existing system: mapping, cleaning, cut-over, and the check that nothing was lost.
- Estimate the volume and the growth of the data. Design indexes, partitions and archives to match.
- State what must be recoverable after a failure and how much data may be lost. The infrastructure architect designs the backup.
- Decide where reports and analytics read from, so that they do not slow down the application.
- Define how the tests get their data, without real personal data.

## Decisions

| The role decides | The role does not decide |
| --- | --- |
| The data model | Which component owns which data: the solution architect |
| The type of each data store | The product and the hosting of a data store: the infrastructure architect |
| How the schema changes, and the migration rules | The code that reads and writes the data: the software architect |
| How long each class of data is kept, and how it is deleted | Which class a piece of data belongs to, and how it is protected: the security architect |
| The consistency rules | Which data the product collects at all: the product manager and the Dreamer |
| The plan to migrate the data of an existing system | The backup mechanism: the infrastructure architect |

The full list of owners is in [Who decides what](README.md#who-decides-what).

## When the role is engaged

| Tier | Engagement |
| --- | --- |
| 1 | Covered by the solution architect, with the checklist below |
| 2 | Covered by the software architect, with the checklist below |
| 3 | Engaged |
| 4 | Engaged |

Triggers that engage the role at tier 1 or 2:

- Data is imported from an existing system.
- The solution needs more than one data store.
- The Dreamer needs reports or analytics beyond simple lists.
- The data is large or grows fast: media files, event logs, measurements.
- The data must be kept or deleted by law: financial records, health records, an audit trail.
- Several customers share one database, and their data must stay apart.

## Depth by tier

### Tier 1: static site

The role is covered. The solution architect works through this checklist:

- Where the content lives: the files of the site, in version control.
- Whether the site collects any data: a contact form, a newsletter sign-up, analytics.
- For each kind of collected data: which service receives it, who can read it, and when it is deleted.
- Whether the collected data needs a privacy notice or a consent banner. The security architect's checklist has the same question.

### Tier 2: small application

The role is covered, unless a trigger engages it. The software architect works through this checklist:

- One relational database.
- An entity model with the tables, the keys and the relations. Use the words of the glossary for the names.
- Constraints in the database, not only in the code: required fields, unique values, foreign keys.
- An index for each frequent lookup.
- A migration tool. Every schema change is a migration in version control. Nobody changes the schema by hand.
- Automatic backups, and one restore that was tried.
- For personal data: collect only what a requirement needs, and have a way to delete the data of one person.
- Files that users upload go to object storage, not into the database.

### Tier 3: multi-component product

The output is the data part of the architecture description.

- The conceptual model: the entities and relations in business terms.
- The data model of each data store.
- The type of each data store, with the reason. A second type of store is justified by a requirement that the first cannot meet.
- The owner of each entity: the one component that writes it. Other components read it through the owner or keep a marked copy.
- A data flow diagram: what moves between the components and the external systems, in which direction, and how often.
- The consistency rules across components: what is correct at once, what becomes correct after a delay, and how long the delay may be.
- The migration rules for deployment without downtime: first add the new structure, then move the code and the data, then remove the old structure in a later release.
- The retention and the deletion of each class of data.
- What must be recoverable, how much data may be lost, and how fast the data must be back.
- A growth model: the expected rows and bytes for each main entity after one year and after three years.
- Where reports read from: a read replica or a separate store.
- The test data: how it is generated, and how production data is made anonymous if it is used.

### Tier 4: enterprise system

Everything of tier 3, and:

- The alignment with the data model of the organization, and with its master data: customers, products, employees. The solution uses the master record and does not create a second one.
- The data governance: an owner for each data set, an entry in the data catalog of the organization, and the lineage of each important figure back to its source.
- The integration with the data warehouse or the data lake of the organization.
- The migration from the legacy system as a plan of its own: mapping, cleaning, trial runs, a period where both systems run in parallel, a reconciliation after each run, and a way back.
- The retention that the regulations require, including a hold on deletion for legal cases.
- The location of the data: which data must stay in which country or region.
- Data contracts between teams: the schema and the quality that a team promises to those who read its data.
- The monitoring of data quality in production.

## Work in each phase

| Phase | Work |
| --- | --- |
| 1. Discovery | Names the data requirements: what is stored, for how long, what is imported, exported and reported, and how much data is expected. Starts the glossary with the business analyst. At tiers 3 and 4, names the existing data sources that the idea depends on. |
| 2. Architecture and design | Designs the data model, the data stores, the data flows, the life of the data and the migration rules. |
| 3. Planning | Orders the schema work and the migration work. Plans the test data. |
| 4. Implementation | Reviews every schema change and every migration. Reviews the queries of the main operations. |
| 5. Verification | Checks the migration on data that is like production in size and shape. Checks the data integrity tests, the restore test, and the performance with realistic volumes. |
| 6. Release | Reviews the migration plan of the release: the backup before it, the cut-over, the data check after it, and the way back. |
| 7. Operation and maintenance | Watches the growth, the slow queries and the data quality. Checks that retention and deletion run. Plans changes to indexes, partitions and archives. |

## Inputs and outputs

| Reads | Produces |
| --- | --- |
| The requirements specification, with the glossary | The architecture description: data model |
| The solution design: which component owns which data | The data flow diagram |
| The classification of the data, from the security architect | The rules for retention and deletion |
| The schema and the data of an existing system | The migration rules, and the plan for a legacy migration |
| The schema changes and the migrations in review | The recovery needs: what, how much loss, how fast |
| The metrics of the data stores | The growth model |

## Works with

- **Solution architect.** The solution architect decides which component owns which data. The data architect reports when a boundary cuts through data that must change in one transaction.
- **Software architect.** The data architect owns the schema. The software architect owns the code that reads and writes it. They agree on the mapping between the two.
- **Security architect.** The security architect classifies the data and sets the protection of each class. The data architect applies the class to each field, and designs retention and deletion to match.
- **Infrastructure architect.** The data architect states the type of each store, its size and its recovery needs. The infrastructure architect chooses the product, sizes it and designs the backup.
- **AI architect.** They agree on the data that a model may read, on the permissions that apply to it, and on how long conversations with a model are kept.
- **Business analyst.** They keep one glossary. An entity in the data model has the name that the Dreamer uses for it.
- **QA engineer.** They agree on the test data and on the checks that prove the data is intact after a migration.

## Checks

The output of the role is complete when all of these are true:

- Every entity has a name from the glossary, a key, and one component that owns it.
- Every piece of data has one source of truth. Every copy is marked, with the way it is refreshed.
- Every rule that the data must obey is a constraint in the database, or the document says where else it is enforced and why.
- Every data store that is not relational has a reason.
- Every class of data has a retention period and a way to delete it.
- The data of one person can be found and deleted, where the law gives the person that right.
- Every schema change is a migration that can be applied without stopping the solution, at the tiers that require it.
- The recovery needs are stated: what must be back, how much may be lost, how fast.
- The growth model exists, and the design holds for the three-year figure.
- No real personal data is in a test environment.

## Common mistakes

- **Modeling the screens and not the business.** A table for each form gives a schema that breaks with the next change to the user interface.
- **Adding a second type of data store for convenience.** Each store has to be operated, backed up, secured and kept consistent with the others.
- **Rules only in the code.** The second program that writes to the database does not know them.
- **Keeping everything forever.** Data that is not needed is a cost and a risk. In many countries, keeping personal data without a reason is against the law.
- **Treating a migration as a script for the last day.** Old data is dirtier than anyone remembers. A migration is tried on real volumes early and more than once.
- **A schema change that needs the old code and the new code to stop at the same moment.** It turns every release into downtime.
