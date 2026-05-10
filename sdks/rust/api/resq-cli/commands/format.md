**resq_cli > commands > format**

# Module: commands::format

## Contents

**Structs**

- [`FormatArgs`](#formatargs) - Arguments for the `format` command.

**Enums**

- [`FormatOutcome`](#formatoutcome) - Outcome of a per-language format step.

**Functions**

- [`format_cpp`](#format_cpp) - Format C/C++ files via `clang-format`.
- [`format_csharp`](#format_csharp) - Format C# via `dotnet format`.
- [`format_python`](#format_python) - Format Python files via `ruff format`.
- [`format_rust`](#format_rust) - Format Rust files via `cargo fmt` (runs against the whole workspace
- [`format_ts`](#format_ts) - Format JS/TS/JSON/CSS files via Biome (preferring `biome` over `bunx --bun biome`).
- [`run`](#run) - Executes the `format` command.

---

## resq_cli::commands::format::FormatArgs

*Struct*

Arguments for the `format` command.

**Fields:**
- `language: Option<String>` - Language to format. If omitted, runs every detected language.
- `check: bool` - Report issues without rewriting files. Exits non-zero if any found.

**Traits:** Parser

**Trait Implementations:**

- **Args**
  - `fn group_id() -> Option<clap::Id>`
  - `fn augment_args<'b>(__clap_app: clap::Command) -> clap::Command`
  - `fn augment_args_for_update<'b>(__clap_app: clap::Command) -> clap::Command`
- **FromArgMatches**
  - `fn from_arg_matches(__clap_arg_matches: &clap::ArgMatches) -> ::std::result::Result<Self, clap::Error>`
  - `fn from_arg_matches_mut(__clap_arg_matches: & mut clap::ArgMatches) -> ::std::result::Result<Self, clap::Error>`
  - `fn update_from_arg_matches(self: & mut Self, __clap_arg_matches: &clap::ArgMatches) -> ::std::result::Result<(), clap::Error>`
  - `fn update_from_arg_matches_mut(self: & mut Self, __clap_arg_matches: & mut clap::ArgMatches) -> ::std::result::Result<(), clap::Error>`
- **CommandFactory**
  - `fn command<'b>() -> clap::Command`
  - `fn command_for_update<'b>() -> clap::Command`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`



## resq_cli::commands::format::FormatOutcome

*Enum*

Outcome of a per-language format step.

**Variants:**
- `Clean` - The formatter ran and made no changes (or found no issues in `--check`).
- `Formatted` - The formatter ran and either rewrote files or — in `--check` — found issues.
- `Skipped(String)` - Skipped: either no matching files or the required tool isn't installed.
- `Failed(String)` - Formatter exited with a non-zero status unexpectedly.

**Methods:**

- `fn passed(self: &Self) -> bool` - `true` iff the step should be treated as a pass for pre-commit gating.

**Traits:** Eq

**Trait Implementations:**

- **PartialEq**
  - `fn eq(self: &Self, other: &FormatOutcome) -> bool`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`



## resq_cli::commands::format::format_cpp

*Function*

Format C/C++ files via `clang-format`.

# Errors
Never — failures are reported via `FormatOutcome::Failed(stderr)`.

```rust
fn format_cpp(root: &std::path::Path, files: &[String], check: bool) -> anyhow::Result<FormatOutcome>
```



## resq_cli::commands::format::format_csharp

*Function*

Format C# via `dotnet format`.

# Errors
Never — failures are reported via `FormatOutcome::Failed(stderr)`.

```rust
fn format_csharp(root: &std::path::Path, files: &[String], check: bool) -> anyhow::Result<FormatOutcome>
```



## resq_cli::commands::format::format_python

*Function*

Format Python files via `ruff format`.

# Errors
Never — failures are reported via `FormatOutcome::Failed(stderr)`.

```rust
fn format_python(root: &std::path::Path, files: &[String], check: bool) -> anyhow::Result<FormatOutcome>
```



## resq_cli::commands::format::format_rust

*Function*

Format Rust files via `cargo fmt` (runs against the whole workspace
when `files` is empty).

# Errors
Never — failures are reported via `FormatOutcome::Failed(stderr)`.

```rust
fn format_rust(root: &std::path::Path, files: &[String], check: bool) -> anyhow::Result<FormatOutcome>
```



## resq_cli::commands::format::format_ts

*Function*

Format JS/TS/JSON/CSS files via Biome (preferring `biome` over `bunx --bun biome`).

# Errors
Never — failures are reported via `FormatOutcome::Failed(stderr)`.

```rust
fn format_ts(root: &std::path::Path, files: &[String], check: bool) -> anyhow::Result<FormatOutcome>
```



## resq_cli::commands::format::run

*Function*

Executes the `format` command.

# Errors
Returns an error only if the argument validation fails. Per-language
failures are reported on stderr and accumulate into the CLI exit code.

```rust
fn run(args: FormatArgs) -> anyhow::Result<()>
```



