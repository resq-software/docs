# resq_cli

> **Version:** `v0.3.0` · **License:** `Apache-2.0` · **Crate:** [crates.io](https://crates.io/crates/resq-cli) · **API docs:** [docs.rs](https://docs.rs/resq-cli/0.3.0)

`ResQ` CLI - Command-line interface for managing `ResQ` services.

This crate provides a unified CLI for interacting with the `ResQ` platform,
including service management, blockchain queries, and deployment operations.

# Commands

Grouped:
- `scan audit` — run cargo/bun/uv audit across the workspace
- `scan secrets` — scan for leaked credentials
- `scan copyright` — check or apply license headers
- `tui explore` / `logs` / `health` / `deploy` / `clean` / `asm` — TUI explorers

Top-level:
- `format` — format Rust / TS / Python / C++ / C# in one pass
- `pre-commit` — full pre-commit gate (copyright, secrets, audit, format)
- `hooks` — inspect / update installed git hooks
- `dev` — repository utilities (workspace ops)
- `version` / `docs` / `commit` — release + docs + AI commit messages
- `completions` — emit shell completions for bash/zsh/fish/elvish/powershell

Legacy flat forms (`resq audit`, `resq explore`, etc.) remain as hidden
aliases for one release cycle.

# Usage

```bash
resq scan audit
resq format --check
resq pre-commit
resq tui health
resq completions bash > /usr/local/share/bash-completion/completions/resq
```

## Modules

### [`resq_cli`](resq_cli.md)

*3 modules*

### [`commands`](commands.md)

*13 modules*

### [`commands::audit`](commands/audit.md)

*1 function, 1 struct*

### [`commands::commit`](commands/commit.md)

*1 function, 1 struct*

### [`commands::completions`](commands/completions.md)

*1 function, 1 struct*

### [`commands::copyright`](commands/copyright.md)

*1 function, 1 struct*

### [`commands::dev`](commands/dev.md)

*1 enum, 3 functions, 5 structs*

### [`commands::docs`](commands/docs.md)

*1 function, 1 struct*

### [`commands::explore`](commands/explore.md)

*6 functions, 6 structs*

### [`commands::format`](commands/format.md)

*1 enum, 1 struct, 6 functions*

### [`commands::hook_templates`](commands/hook_templates.md)

*1 constant, 1 function*

### [`commands::hooks`](commands/hooks.md)

*1 enum, 1 struct, 2 functions*

### [`commands::pre_commit`](commands/pre_commit.md)

*1 function, 1 struct*

### [`commands::secrets`](commands/secrets.md)

*1 function, 1 struct*

### [`commands::version`](commands/version.md)

*1 enum, 1 function, 3 structs*

### [`gitignore`](gitignore.md)

*2 functions*

### [`utils`](utils.md)

*1 function*

