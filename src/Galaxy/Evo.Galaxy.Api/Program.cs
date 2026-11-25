var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOpenApi();
builder.Services.AddHealthChecks();

var app = builder.Build();

// The OpenAPI document is served at /openapi/v1.json. See docs/api/README.md.
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

// Health check. Evo.Galaxy.Api is not deployed yet, so no probe calls it.
app.MapHealthChecks("/health");

app.Run();
