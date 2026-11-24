# syntax=docker/dockerfile:1

# The build context is the repository root:
#   docker build -f deploy/docker/Dockerfile -t evo-darwin:local .

ARG DOTNET_VERSION=10.0

FROM mcr.microsoft.com/dotnet/sdk:${DOTNET_VERSION} AS build
WORKDIR /source

COPY global.json Directory.Build.props Directory.Packages.props ./
COPY src/ src/

RUN dotnet publish src/Evo.Darwin.Api/Evo.Darwin.Api.csproj \
      --configuration Release \
      --output /app/publish \
      -p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:${DOTNET_VERSION} AS runtime
WORKDIR /app

COPY --from=build /app/publish .

# APP_UID is the non-root user defined by the .NET base images (UID 1654).
USER $APP_UID

# The .NET base images set ASPNETCORE_HTTP_PORTS=8080.
EXPOSE 8080

ENTRYPOINT ["dotnet", "Evo.Darwin.Api.dll"]
