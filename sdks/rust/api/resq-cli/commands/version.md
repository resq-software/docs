**resq_cli > commands > version**

# Module: commands::version

## Contents

**Structs**

- [`AddArgs`](#addargs) - Arguments for adding a changeset.
- [`ApplyArgs`](#applyargs) - Arguments for applying version bumps.
- [`VersionArgs`](#versionargs) - Arguments for the version command.

**Enums**

- [`VersionCommands`](#versioncommands) - Commands for version management.

**Functions**

- [`run`](#run) - Run the version command

---

## resq_cli::commands::version::AddArgs

*Struct*

Arguments for adding a changeset.

**Fields:**
- `bump: String` - Type of change (patch, minor, major)
- `message: String` - Summary of what changed

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



## resq_cli::commands::version::ApplyArgs

*Struct*

Arguments for applying version bumps.

**Fields:**
- `dry_run: bool` - Dry run - see what would change without modifying files

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



## resq_cli::commands::version::VersionArgs

*Struct*

Arguments for the version command.

**Fields:**
- `command: VersionCommands` - Subcommand to execute.

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



## resq_cli::commands::version::VersionCommands

*Enum*

Commands for version management.

**Variants:**
- `Add(AddArgs)` - Create a new changeset (intent to change version)
- `Apply(ApplyArgs)` - Consume changesets and apply version bumps across the monorepo
- `Check` - Check if all versions are synchronized

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



## resq_cli::commands::version::run

*Function*

Run the version command

```rust
fn run(args: VersionArgs) -> anyhow::Result<()>
```



