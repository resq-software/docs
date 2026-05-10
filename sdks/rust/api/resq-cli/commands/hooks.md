**resq_cli > commands > hooks**

# Module: commands::hooks

## Contents

**Structs**

- [`HooksArgs`](#hooksargs) - Arguments for the `hooks` command.

**Enums**

- [`HooksCommands`](#hookscommands) - Hooks subcommands.

**Functions**

- [`canonical_count`](#canonical_count) - Returns the canonical hook count — used by docs/tests.
- [`run`](#run) - Executes a `hooks` subcommand.

---

## resq_cli::commands::hooks::HooksArgs

*Struct*

Arguments for the `hooks` command.

**Fields:**
- `command: HooksCommands` - Hooks subcommand to execute.

**Traits:** Parser

**Trait Implementations:**

- **CommandFactory**
  - `fn command<'b>() -> clap::Command`
  - `fn command_for_update<'b>() -> clap::Command`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`
- **Args**
  - `fn group_id() -> Option<clap::Id>`
  - `fn augment_args<'b>(__clap_app: clap::Command) -> clap::Command`
  - `fn augment_args_for_update<'b>(__clap_app: clap::Command) -> clap::Command`
- **FromArgMatches**
  - `fn from_arg_matches(__clap_arg_matches: &clap::ArgMatches) -> ::std::result::Result<Self, clap::Error>`
  - `fn from_arg_matches_mut(__clap_arg_matches: & mut clap::ArgMatches) -> ::std::result::Result<Self, clap::Error>`
  - `fn update_from_arg_matches(self: & mut Self, __clap_arg_matches: &clap::ArgMatches) -> ::std::result::Result<(), clap::Error>`
  - `fn update_from_arg_matches_mut(self: & mut Self, __clap_arg_matches: & mut clap::ArgMatches) -> ::std::result::Result<(), clap::Error>`



## resq_cli::commands::hooks::HooksCommands

*Enum*

Hooks subcommands.

**Variants:**
- `Install` - Install canonical hooks into `.git-hooks/` and set `core.hooksPath`.
- `ScaffoldLocal(crate::commands::dev::ScaffoldLocalHookArgs)` - Scaffold a repo-specific `.git-hooks/local-<hook>` from a kind template.
- `Doctor` - Report installed hook status; exit 1 if any drift / missing file detected.
- `Update` - Rewrite installed canonical hooks from embedded templates (preserves `local-*`).
- `Status` - Print a one-line summary for scripts (e.g. `installed=clean local=pre-push`).

**Trait Implementations:**

- **Subcommand**
  - `fn augment_subcommands<'b>(__clap_app: clap::Command) -> clap::Command`
  - `fn augment_subcommands_for_update<'b>(__clap_app: clap::Command) -> clap::Command`
  - `fn has_subcommand(__clap_name: &str) -> bool`
- **FromArgMatches**
  - `fn from_arg_matches(__clap_arg_matches: &clap::ArgMatches) -> ::std::result::Result<Self, clap::Error>`
  - `fn from_arg_matches_mut(__clap_arg_matches: & mut clap::ArgMatches) -> ::std::result::Result<Self, clap::Error>`
  - `fn update_from_arg_matches(self: & mut Self, __clap_arg_matches: &clap::ArgMatches) -> ::std::result::Result<(), clap::Error>`
  - `fn update_from_arg_matches_mut<'b>(self: & mut Self, __clap_arg_matches: & mut clap::ArgMatches) -> ::std::result::Result<(), clap::Error>`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`



## resq_cli::commands::hooks::canonical_count

*Function*

Returns the canonical hook count — used by docs/tests.

```rust
fn canonical_count() -> usize
```



## resq_cli::commands::hooks::run

*Function*

Executes a `hooks` subcommand.

# Errors
Returns an error if filesystem access or `git config` invocation fails.

```rust
fn run(args: HooksArgs) -> anyhow::Result<()>
```



