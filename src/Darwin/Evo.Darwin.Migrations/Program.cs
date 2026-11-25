using Evo.Darwin.Data;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

// Applies the pending migrations to the Darwin database, then exits.
var builder = Host.CreateApplicationBuilder(args);

// The configuration key is ConnectionStrings:Darwin (environment variable ConnectionStrings__Darwin).
var connectionString = builder.Configuration.GetConnectionString("Darwin");

builder.Services.AddDbContext<DarwinDbContext>(options => options.UseNpgsql(
    connectionString,
    // The migration classes are in this project, not in the project of the context.
    npgsql => npgsql.MigrationsAssembly(typeof(Program).Assembly)));

using var host = builder.Build();

// The check is after Build() because `dotnet ef` runs this file up to Build() and needs no database.
if (string.IsNullOrWhiteSpace(connectionString))
{
    Console.Error.WriteLine("The connection string is missing. Set the environment variable ConnectionStrings__Darwin.");
    return 1;
}

await using var scope = host.Services.CreateAsyncScope();
var context = scope.ServiceProvider.GetRequiredService<DarwinDbContext>();

await context.Database.MigrateAsync();

return 0;
