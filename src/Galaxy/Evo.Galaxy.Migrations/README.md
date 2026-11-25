# Evo.Galaxy.Migrations

The migrations of the Galaxy database (PostgreSQL): a .NET console application. It applies the pending EF Core migrations and exits.

## What belongs here

- The migration classes that EF Core generates, in the folder `Migrations/`.
- `Program.cs`, which applies the pending migrations.

The context belongs in [`Evo.Galaxy.Data`](../Evo.Galaxy.Data/README.md), and the classes that describe the tables in [`Evo.Galaxy.Entities`](../Evo.Galaxy.Entities/README.md). A migration is generated from them.

This project is the only one that changes the schema of the database. `Evo.Galaxy.Worker` reads and writes rows and does not apply migrations.

Today the project has no migration: the context has no tables.

## References

`Evo.Galaxy.Data`. It brings `Evo.Galaxy.Entities` with it.

## Run locally

Run every command from the repository root. Start the local database first: see [Local database](../../../README.md#local-database) in the repository README.

Apply the pending migrations to the local database:

```bash
ConnectionStrings__Galaxy="Host=localhost;Database=galaxy;Username=postgres;Password=postgres" dotnet run --project src/Galaxy/Evo.Galaxy.Migrations
```

The program exits with code 0. The last log line is `No migrations were applied. The database is already up to date.` or, when a migration is pending, the name of each applied migration. The first run creates the table `__EFMigrationsHistory`, in which EF Core records the applied migrations.

Until the first mapping class exists, EF Core logs the warning `No instantiatable types implementing IEntityTypeConfiguration were found`. On the first run it also logs one failed command: the query for the history table that does not exist yet.

Without the connection string the program prints an error and exits with code 1.

### Add a migration

`dotnet ef` is a local tool, listed in `dotnet-tools.json`. Install it once:

```bash
dotnet tool restore
```

After you change an entity or its mapping, generate the migration. Replace `<Name>` with a name that says what changes, for example `AddProjects`:

```bash
dotnet ef migrations add <Name> --project src/Galaxy/Evo.Galaxy.Migrations
```

The command needs no database. It writes the migration to `src/Galaxy/Evo.Galaxy.Migrations/Migrations/`. Commit the generated files.

List the migrations of the project:

```bash
dotnet ef migrations list --project src/Galaxy/Evo.Galaxy.Migrations
```

The program is not built into a container image and is not run by the pipeline. See the [architecture overview](../../../docs/architecture/overview.md#deployment).

## Tests

No tests cover this project today.

TODO: when the first migration is added, describe here how the migrations are tested.

## Environment variables

| Name | Required | Effect |
| --- | --- | --- |
| `ConnectionStrings__Galaxy` | Yes | Connection string of the Galaxy database, in the Npgsql format. The user needs the right to create and change tables. |
| `DOTNET_ENVIRONMENT` | No | Name of the environment. Without a value the program runs as `Production`. |

When you add a variable, add it to [docs/configuration.md](../../../docs/configuration.md) and to the table above in the same pull request.
