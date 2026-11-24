## What and why

<!-- What does this change do, and why is it needed? Link the issue or ticket. -->

## How it was tested

<!-- Tests added or changed, and any checks you ran by hand. -->

## Checklist

- [ ] `dotnet build` and `dotnet test` pass locally.
- [ ] The docs in `docs/` that describe this change are updated in this pull request (rules: `docs/README.md`).
- [ ] The `README.md` of every project this change affects is updated. A new project has a `README.md`.
- [ ] New or changed environment variables and secrets are listed in `docs/configuration.md` and in the README of the project that reads them.
- [ ] `version` in `deploy/helm/evo-darwin/Chart.yaml` is bumped if the chart changed.
- [ ] A decision that changes the structure of the repository or the service is recorded as an ADR in `docs/adr/`.
