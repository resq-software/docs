# Source repo doc-generation templates

Each ResQ source repo (`npm`, `dotnet-sdk`, `pypi`, `programs`, `vcpkg`, `viz`)
runs its own native API-doc generator and opens a PR against this docs repo
with the rendered MDX. This folder holds the canonical workflow YAML for
each language so the pattern stays uniform across the org.

This is distinct from the OpenAPI-driven `api-reference/` group, which is
generated from `specs/*.json` at Mintlify build time. These templates
cover per-language SDK reference docs (TypeDoc, DocFX, etc.).

## Pattern

```
source repo (e.g. resq-software/npm)
  └─ .github/workflows/api-docs.yml   <- copy from here
       │
       │ on tag v* or manual dispatch
       ▼
  1. checkout source
  2. run native doc tool (TypeDoc / DocFX / mkdocstrings / ...)
  3. checkout resq-software/docs into ./docs-checkout
  4. rsync generated MDX into ./docs-checkout/sdks/<lang>/api/
  5. peter-evans/create-pull-request opens a PR in resq-software/docs
       │
       ▼
  human reviews + merges PR; Mintlify rebuilds.
```

## Required org secret

All copied workflows reference `secrets.DOCS_REPO_PR_TOKEN`. Set this
once as an org-level GitHub secret with selected-repo visibility,
scoped to a fine-grained PAT or GitHub App with write access to
`resq-software/docs` only.

The credential must be owned by the org's machine user account
[`resq-sw`](https://github.com/resq-sw), not by an individual
contributor. PRs opened by these workflows will appear as authored by
`resq-sw`, which is the expected label.

Generate the PAT while logged in as `resq-sw`, then run (as an org
owner):

Run from a shell where `gh` is authed as a `resq-software` org owner.
The pattern below pipes the token via stdin so it never appears in
shell history or argument lists:

```sh
read -rs -p "Paste resq-sw PAT (input hidden): " TOKEN; echo
printf '%s' "$TOKEN" | gh secret set DOCS_REPO_PR_TOKEN \
  --org resq-software \
  --visibility selected \
  --repos "crates,npm,dotnet-sdk,pypi,programs,vcpkg,viz,docs" \
  --body -
unset TOKEN
```

`crates` is included for parity with the rest of the org even though
it ships its own rustdoc pipeline today.

## Per-language tooling

| Source repo                | Lang   | Tool                     | Template file                |
| -------------------------- | ------ | ------------------------ | ---------------------------- |
| `resq-software/npm`        | TS     | TypeDoc + markdown plug. | `api-docs.typescript.yml`    |
| `resq-software/dotnet-sdk` | C#     | DefaultDocumentation     | `api-docs.dotnet.yml`        |
| `resq-software/pypi`       | Python | pydoc-markdown           | `api-docs.python.yml`        |
| `resq-software/crates`     | Rust   | README + docs.rs links   | `api-docs.rust.yml`          |
| `resq-software/vcpkg`      | C++    | Doxygen + moxygen        | `api-docs.cpp.yml`           |
| `resq-software/programs`   | Rust   | rustdoc + cargo-readme   | _TODO_                       |
| `resq-software/viz`        | C#/web | DefaultDocumentation     | _TODO_                       |

## Syncing changes

Templates here are the canonical version. After editing, push the
update to each source repo with the helper script:

```sh
automation/sync-templates.sh             # all 3
automation/sync-templates.sh --dry-run   # preview diffs
automation/sync-templates.sh python      # one language only
automation/sync-templates.sh --auto-merge  # open PRs with --auto
```

The script clones each target repo shallowly, copies the matching
`api-docs.<lang>.yml`, opens a sync PR on `sync/api-docs-template`,
and reports up-to-date when the workflow already matches.

## Adding a new template

1. Drop the workflow YAML in this folder named `api-docs.<lang>.yml`.
2. Pin every action to a full commit SHA with a `# vX.Y.Z` trailing
   comment. Match the SHA convention used by the **target** repo
   (e.g. `resq-software/npm` pins `actions/checkout@v6.0.2`, this
   docs repo pins `v4.2.2`); the template should match the destination.
3. Use minimal `permissions:` (read at the workflow level, escalate
   per job only when needed).
4. Output goes to `sdks/<lang>/api/` in the docs repo. Keep that path
   stable; it is referenced by `docs.json` navigation.
5. Update the table above with the template filename.

## Tag triggers

`resq-software/npm` is a bun monorepo released via Changesets, with
per-package tags like `@resq-systems/ui@v0.35.6`. The TypeScript template
triggers only on `@resq-systems/ui@v*` so non-UI package releases do not
spam the docs PR queue. When other packages get a docs surface, add
their tag pattern (or convert to a matrix).

Single-package source repos (e.g. `resq-software/dotnet-sdk`) can use
the simpler `tags: ['v*']` form.

## Navigation

For now, navigation entries in `docs.json` are added by hand once per
new top-level module. Future work: have the workflow also write a
`sdks/<lang>/api/_pages.json` index that a small build helper splices
into `docs.json` automatically.

## Gotchas (learned the hard way)

1. **Doc-generator + plugin version pinning.** Pin both at `@latest`
   and install the plugin first so its `peerDependency` selects a
   compatible major. A specific minor pin tends to drift apart from
   the plugin's expected core version and produce
   `SyntaxError: ... does not provide an export named X` on plugin load.
2. **Verify captured length before storing the org secret.** Some
   shells (notably zsh with bracketed paste) can capture only the
   first character of a long PAT silently. Always
   `echo "${#TOKEN}"` before piping into `gh secret set`. A
   fine-grained PAT is 90+ chars; if you see anything below ~80,
   abort and re-paste, or set the value via the GitHub web UI.
3. **`persist-credentials: false` on the docs checkout.** Any step
   that uses `peter-evans/create-pull-request` with a `token:` will
   collide with `actions/checkout`'s extraheader, producing
   `remote: Duplicate header: "Authorization"`. Set
   `persist-credentials: false` on the checkout that targets the
   docs repo and let the PR action handle its own auth.
