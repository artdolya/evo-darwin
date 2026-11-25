# syntax=docker/dockerfile:1

# The image of Evo.Darwin.Worker for the local stack in src/Docker/docker-compose.yml.
#
# There are two build contexts: the repository root, and the Krapka checkout under the
# name "krapka". docker-compose.yml passes both.

# Visual Studio builds only this stage when it debugs. It runs the project output of the
# host in it.
FROM mcr.microsoft.com/dotnet/runtime:10.0 AS base
USER $APP_UID
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /source

COPY global.json Directory.Build.props Directory.Packages.props ./
COPY src/ src/

# The Krapka libraries are built from source, at the path that the link src/Krapka has
# on the host. The build output of the host is left out.
COPY --from=krapka --exclude=**/bin --exclude=**/obj src/Net/ src/Krapka/src/Net/

# The cache keeps the NuGet packages between builds. One build uses it at a time.
RUN --mount=type=cache,id=evo-nuget,target=/root/.nuget/packages,sharing=locked \
    dotnet publish src/Darwin/Evo.Darwin.Worker/Evo.Darwin.Worker.csproj \
      --configuration "$BUILD_CONFIGURATION" \
      --output /app/publish \
      -p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "Evo.Darwin.Worker.dll"]
