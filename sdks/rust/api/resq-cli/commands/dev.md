**resq_cli > commands > dev**

# Module: commands::dev

## Contents

**Structs**

- [`DevArgs`](#devargs) - Arguments for the 'dev' command.
- [`KillPortsArgs`](#killportsargs) - Arguments for the 'kill-ports' command.
- [`ScaffoldLocalHookArgs`](#scaffoldlocalhookargs) - Arguments for the `scaffold-local-hook` command.
- [`SyncEnvArgs`](#syncenvargs) - Arguments for the 'sync-env' command.
- [`UpgradeArgs`](#upgradeargs) - Arguments for the 'upgrade' command.

**Enums**

- [`DevCommands`](#devcommands) - Developer subcommands.

**Functions**

- [`run`](#run) - Executes the dev command.
- [`run_install_hooks_impl`](#run_install_hooks_impl) - Install the canonical git hooks into the current project's `.git-hooks/`.
- [`run_scaffold_local_hook_impl`](#run_scaffold_local_hook_impl) - Scaffold a repo-specific `.git-hooks/local-<hook>` file from a kind template.

---

## resq_cli::commands::dev::DevArgs

*Struct*

Arguments for the 'dev' command.

**Fields:**
- `command: DevCommands` - Dev subcommand to execute

**Traits:** Parser

**Trait Implementations:**

- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`
- **CommandFactory**
  - `fn command<'b>() -> clap::Command`
  - `fn command_for_update<'b>() -> clap::Command`
- **Args**
  - `fn group_id() -> Option<clap::Id>`
  - `fn augment_args<'b>(__clap_app: clap::Command) -> clap::Command`
  - `fn augment_args_for_update<'b>(__clap_app: clap::Command) -> clap::Command`
- **FromArgMatches**
  - `fn from_arg_matches(__clap_arg_matches: &clap::ArgMatches) -> ::std::result::Result<Self, clap::Error>`
  - `fn from_arg_matches_mut(__clap_arg_matches: & mut clap::ArgMatches) -> ::std::result::Result<Self, clap::Error>`
  - `fn update_from_arg_matches(self: & mut Self, __clap_arg_matches: &clap::ArgMatches) -> ::std::result::Result<(), clap::Error>`
  - `fn update_from_arg_matches_mut(self: & mut Self, __clap_arg_matches: & mut clap::ArgMatches) -> ::std::result::Result<(), clap::Error>`



## resq_cli::commands::dev::DevCommands

*Enum*

Developer subcommands.

**Variants:**
- `KillPorts(KillPortsArgs)` - Kill processes listening on specified ports
- `SyncEnv(SyncEnvArgs)` - Sync environment variables from .env.example files to turbo.json
- `Upgrade(UpgradeArgs)` - Upgrade dependencies across all monorepo silos
- `InstallHooks` - Install git hooks from .git-hooks directory
- `ScaffoldLocalHook(ScaffoldLocalHookArgs)` - Scaffold a repo-specific `.git-hooks/local-<hook>` file

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



## resq_cli::commands::dev::KillPortsArgs

*Struct*

Arguments for the 'kill-ports' command.

**Fields:**
- `targets: Vec<String>` - Ports or ranges (e.g. 8000 or 8000..8010)
- `force: bool` - Use SIGKILL instead of default SIGTERM
- `yes: bool` - Skip confirmation prompt

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



## resq_cli::commands::dev::ScaffoldLocalHookArgs

*Struct*

Arguments for the `scaffold-local-hook` command.

**Fields:**
- `kind: String` - Project kind. `auto` detects from root marker files
- `hook: String` - Which hook to scaffold a local override for (e.g. `pre-push`).
- `force: bool` - Overwrite an existing `local-<hook>` file.

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



## resq_cli::commands::dev::SyncEnvArgs

*Struct*

Arguments for the 'sync-env' command.

**Fields:**
- `tasks: String` - Tasks to update in turbo.json (comma-separated)
- `dry_run: bool` - Preview changes without writing to turbo.json
- `max_depth: usize` - Maximum directory depth to search

**Traits:** Parser

**Trait Implementations:**

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
- **CommandFactory**
  - `fn command<'b>() -> clap::Command`
  - `fn command_for_update<'b>() -> clap::Command`



## resq_cli::commands::dev::UpgradeArgs

*Struct*

Arguments for the 'upgrade' command.

**Fields:**
- `silo: String` - Specific silo to upgrade (python, rust, js, cpp, csharp, nix, or all)

**Traits:** Parser

**Trait Implementations:**

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
- **CommandFactory**
  - `fn command<'b>() -> clap::Command`
  - `fn command_for_update<'b>() -> clap::Command`



## resq_cli::commands::dev::run

*Function*

Executes the dev command.

```rust
fn run(args: DevArgs) -> anyhow::Result<()>
```



## resq_cli::commands::dev::run_install_hooks_impl

*Function*

Install the canonical git hooks into the current project's `.git-hooks/`.

# Errors
Returns an error if filesystem access or `git config` invocation fails.

```rust
fn run_install_hooks_impl() -> anyhow::Result<()>
```



## resq_cli::commands::dev::run_scaffold_local_hook_impl

*Function*

Scaffold a repo-specific `.git-hooks/local-<hook>` file from a kind template.

# Errors
Returns an error if the kind is unknown, the template is missing, or
filesystem access fails.

```rust
fn run_scaffold_local_hook_impl(args: ScaffoldLocalHookArgs) -> anyhow::Result<()>
```



