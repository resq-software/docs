# Changelog notes

Editorial prose for the SDK changelog, keyed by month. `scripts/build_changelog.py`
splices each `## YYYY-MM` section into that month's `<Update>` entry, above the
version tables. The version tables themselves are generated from release data
and must not be hand-edited.

Add a section only when a release deserves narrative — a migration, a new
package, a breaking change. Months with no section render as version tables
alone.

Note bodies must not use `##` headings: the generator emits one `##` per
ecosystem for the version tables, and a note heading at the same level would
collide. Use bold leads and prose instead. Markdown is emitted verbatim, so
keep it valid MDX.

## 2026-07

**npm scope moved to `@resq-systems`.** The TypeScript packages moved from the
`@resq-sw` scope to `@resq-systems` on 12 July 2026, restarting at `1.0.0`.
**`@resq-sw` is not deprecated on npm, so installs still resolve — silently, to
stale versions.** See the [TypeScript SDK](/sdks/typescript) page for migration
steps. `@resq-systems/math` and `@resq-systems/types` are new packages with no
`@resq-sw` predecessor.

## 2026-04

**Rust CLI tools renamed.** The seven CLI tools were renamed on 3 April 2026.
The old crate names stopped at `0.1.9` and are no longer published; the new
names continue the version series.

| Was | Now |
|-----|-----|
| `resq-bin-explorer` | `resq-bin` |
| `resq-cleanup` | `resq-clean` |
| `resq-deploy-cli` | `resq-deploy` |
| `resq-flamegraph` | `resq-flame` |
| `resq-health-checker` | `resq-health` |
| `resq-log-viewer` | `resq-logs` |
| `resq-perf-monitor` | `resq-perf` |

## 2026-03

First public releases across the SDK ecosystems.
