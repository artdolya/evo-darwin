using KrapkaNet.EntityFramework.Abstractions;
using Microsoft.EntityFrameworkCore;

namespace Evo.Darwin.Data;

// The EF Core context of the Darwin database. It has no tables yet.
public sealed class DarwinDbContext(DbContextOptions<DarwinDbContext> options) : ApplicationDbContext(options)
{
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        // Picks up every IEntityTypeConfiguration<T> class in this project.
        modelBuilder.ApplyConfigurationsFromAssembly(typeof(DarwinDbContext).Assembly);
    }
}
