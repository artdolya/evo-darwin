using Evo.Galaxy.Data;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

// Applies the pending migrations to the Galaxy database, then exits.
var builder = Host.CreateApplicationBuilder(args);

// The configuration key is ConnectionStrings:Galaxy (environment variable ConnectionStrings__Galaxy).
var connectionString = builder.Configuration.GetConnectionString("Galaxy");

builder.Services.AddDbContext<GalaxyDbContext>(options => options.UseNpgsql(
    connectionString,
    // The migration classes are in this project, not in the project of the context.
    npgsql => npgsql.MigrationsAssembly(typeof(Program).Assembly)));

using var host = builder.Build();

// The check is after Build() because `dotnet ef` runs this file up to Build() and needs no database.
if (string.IsNullOrWhiteSpace(connectionString))
{
    Console.Error.WriteLine("The connection string is missing. Set the environment variable ConnectionStrings__Galaxy.");
    return 1;
}

await using var scope = host.Services.CreateAsyncScope();
var context = scope.ServiceProvider.GetRequiredService<GalaxyDbContext>();

await context.Database.MigrateAsync();

return 0;
