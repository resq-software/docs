**resq_cli > commands**

# Module: commands

## Contents

**Modules**

- [`audit`](#audit) - Blockchain event auditing.
- [`commit`](#commit) - AI-powered commit message generation.
- [`completions`](#completions) - Shell-completion emitter (`resq completions <shell>`).
- [`copyright`](#copyright) - Copyright header management.
- [`dev`](#dev) - Development server management.
- [`docs`](#docs) - Documentation management and publication.
- [`explore`](#explore) - Service exploration and operations.
- [`format`](#format) - Polyglot source formatting (Rust, TS, Python, C++, C#).
- [`hook_templates`](#hook_templates) - Canonical git-hook templates embedded for scaffolding and drift detection.
- [`hooks`](#hooks) - Hooks lifecycle (`resq hooks install/scaffold-local/doctor/update/status`).
- [`pre_commit`](#pre_commit) - Pre-commit hook logic.
- [`secrets`](#secrets) - Secret management.
- [`version`](#version) - Version management and changesets.

---

## Module: audit

Blockchain event auditing.
Blockchain audit command.

Queries Neo N3 and Solana blockchains for ResQ event records,
providing audit trails for incident response and delivery verification.



## Module: commit

AI-powered commit message generation.
AI-powered commit message generation from staged diffs.



## Module: completions

Shell-completion emitter (`resq completions <shell>`).
Shell-completion emitter.

Generates completion scripts for bash, zsh, fish, elvish, and powershell
by introspecting the `clap`-derived top-level `Cli` parser. Users wire the
output into their shell's completion loader, e.g.:

```bash
resq completions bash > /usr/local/share/bash-completion/completions/resq
```



## Module: copyright

Copyright header management.
Copyright header command.

Checks and updates copyright headers in source files to ensure
proper licensing and attribution.



## Module: dev

Development server management.
ResQ Dev commands — Repository and development utilities.



## Module: docs

Documentation management and publication.



## Module: explore

Service exploration and operations.
ResQ Explore commands — Unified TUI launcher.



## Module: format

Polyglot source formatting (Rust, TS, Python, C++, C#).
`resq format` — polyglot formatter with a shared implementation that
powers both the standalone command and the pre-commit format steps.

Design: each language exports `format_<lang>(root, files, check)` —
pre-commit calls these on its staged file list and then restages; the
CLI wrapper (`resq format`) calls them on an empty list, which tells
each formatter to operate on the whole project.



## Module: hook_templates

Canonical git-hook templates embedded for scaffolding and drift detection.
Canonical git-hook templates embedded via `include_str!`.

Both `resq dev install-hooks` (scaffolding) and `resq hooks doctor`
(drift detection) read from this single source. The templates are kept
in sync with &lt;https://github.com/resq-software/dev/tree/main/scripts/git-hooks>
and the repo-local `.git-hooks/` — CI workflows in both repos enforce
byte equality.



## Module: hooks

Hooks lifecycle (`resq hooks install/scaffold-local/doctor/update/status`).
`resq hooks` — visibility and maintenance for installed git hooks.

- `resq hooks doctor` reports drift between installed `.git-hooks/<file>`
  and the canonical content embedded in this binary.
- `resq hooks update` rewrites the canonical hooks (preserving any
  `local-*` files the repo committed).
- `resq hooks status` prints a one-line summary suitable for shells.



## Module: pre_commit

Pre-commit hook logic.
Unified pre-commit hook logic with an optimized ratatui TUI.



## Module: secrets

Secret management.
Secret scanning command for detecting hardcoded credentials.

Scans source files for potential secrets like API keys, passwords, tokens,
and other sensitive information using pattern matching and entropy analysis.



## Module: version

Version management and changesets.
Version management command - Polyglot Changeset Implementation.



