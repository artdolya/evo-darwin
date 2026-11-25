# 0004. Krapka is referenced as source

## Status

Accepted, 2026-11-24.

## Context

Krapka is a set of shared .NET libraries by the owner of this repository. It has its own open-source repository, <https://github.com/artdolya/krapka>, and publishes NuGet packages named `KrapkaNet.*`. The components that Darwin and Galaxy have in common are meant to live there.

Krapka and the Evo services are developed at the same time, and Krapka changes often. The owner gave two requirements:

- Krapka is maintained in one place. Its code is not copied into this repository.
- A change to Krapka must be usable here without publishing a NuGet package and raising its version here first.

Three options were considered:

1. Reference the published NuGet packages. Every change to Krapka then needs a publish and a version bump before it can be used.
2. Copy the Krapka sources into this repository. The same code then has to be maintained in two places.
3. Link to a Krapka checkout and reference its projects as source.

## Decision

We will use option 3 while Krapka changes often.

- `src/Krapka` is a symbolic link to `../../krapka`, a checkout of the Krapka repository in the folder next to this repository. The link is committed.
- A project of this repository references a Krapka project with a `ProjectReference`. The path starts with the property `KrapkaNetRoot`, set in `Directory.Build.props`.
- The referenced Krapka projects are in `Evo.sln`, in the solution folder `Krapka`, so that they can be changed and built together with the Evo code.

When Krapka changes rarely, we will replace each `ProjectReference` with a `PackageReference` to the published package, and remove the link.

Reason: options 1 and 2 each break one of the two requirements. Option 3 meets both.

## Consequences

- A build needs a Krapka checkout next to this repository. Without it the link points nowhere and `dotnet restore` fails. The setup is in the [README](../../README.md#prerequisites).
- This repository does not record which commit of Krapka it was built with. A build takes whatever the checkout holds. The same commit of this repository can build differently on two machines, and a release cannot be rebuilt exactly.
- CI clones the newest commit of the default branch of Krapka. A change pushed to Krapka can break the CI of this repository without a change here.
- A change that needs new Krapka code is two commits in two repositories. The Krapka commit has to be pushed first, or CI fails.
- The Krapka projects build for every target framework they declare, from `net40` to `net9.0`. The Evo projects use the `net9.0` build. The first build after a clone is slower.
- The Krapka projects use the `Directory.Build.props` and the `Directory.Packages.props` of their own repository. Settings and package versions of this repository do not apply to them.
- `dotnet format` treats the linked files as part of the solution and would change them. `make format` and the CI check pass `--exclude src/Krapka`. A plain `dotnet format` must not be run.
- An Evo project has to be the first project in `Evo.sln`. When a Krapka project is first, `dotnet format` reads the `global.json` of Krapka, which asks for .NET SDK 9, and fails.
- A build writes `bin` and `obj` folders into the Krapka checkout.
- On Windows, Git creates the link only when symbolic links are enabled for the clone.
- The image of `Evo.Darwin.Api` does not need Krapka. An image of a Worker or of a Migrations program does, and the Krapka checkout is outside the Docker build context. The Dockerfile of such an image has to receive the Krapka sources as a second build context.
- `.dockerignore` leaves the link out of the build context.

TODO: decide how a release records the Krapka commit it was built with, for example a file with the commit SHA that CI checks out.

TODO: state the condition for the move to NuGet packages, and who decides it.
