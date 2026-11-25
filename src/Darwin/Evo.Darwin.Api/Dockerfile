# syntax=docker/dockerfile:1

# The image of Evo.Darwin.Api for the local stack in src/Docker/docker-compose.yml.
# The build context is the repository root.
#
# The image that is deployed is built from deploy/docker/Dockerfile, not from this file.

# Visual Studio builds only this stage when it debugs. It runs the project output of the
# host in it.
FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS base
USER $APP_UID
WORKDIR /app
EXPOSE 8080

FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /source

COPY global.json Directory.Build.props Directory.Packages.props ./
COPY src/ src/

# The cache keeps the NuGet packages between builds. One build uses it at a time.
RUN --mount=type=cache,id=evo-nuget,target=/root/.nuget/packages,sharing=locked \
    dotnet publish src/Darwin/Evo.Darwin.Api/Evo.Darwin.Api.csproj \
      --configuration "$BUILD_CONFIGURATION" \
      --output /app/publish \
      -p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "Evo.Darwin.Api.dll"]
