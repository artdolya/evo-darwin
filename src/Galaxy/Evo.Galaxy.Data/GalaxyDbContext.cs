using KrapkaNet.EntityFramework.Abstractions;
using Microsoft.EntityFrameworkCore;

namespace Evo.Galaxy.Data;

// The EF Core context of the Galaxy database. It has no tables yet.
public sealed class GalaxyDbContext(DbContextOptions<GalaxyDbContext> options) : ApplicationDbContext(options)
{
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        // Picks up every IEntityTypeConfiguration<T> class in this project.
        modelBuilder.ApplyConfigurationsFromAssembly(typeof(GalaxyDbContext).Assembly);
    }
}
