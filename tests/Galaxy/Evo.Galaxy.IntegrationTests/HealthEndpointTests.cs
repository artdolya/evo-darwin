using System.Net;
using Microsoft.AspNetCore.Mvc.Testing;

namespace Evo.Galaxy.IntegrationTests;

// Starts the Api in memory and calls it over HTTP.
public class HealthEndpointTests(WebApplicationFactory<Program> factory)
    : IClassFixture<WebApplicationFactory<Program>>
{
    [Fact]
    public async Task Get_health_returns_200()
    {
        using var client = factory.CreateClient();

        using var response = await client.GetAsync("/health");

        Assert.Equal(HttpStatusCode.OK, response.StatusCode);
    }
}
