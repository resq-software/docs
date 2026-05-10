**resq_cli > commands > pre_commit**

# Module: commands::pre_commit

## Contents

**Structs**

- [`PreCommitArgs`](#precommitargs) - Run all pre-commit checks with TUI progress output.

**Functions**

- [`run`](#run) - Main entry point for the pre-commit command.

---

## resq_cli::commands::pre_commit::PreCommitArgs

*Struct*

Run all pre-commit checks with TUI progress output.

**Fields:**
- `root: std::path::PathBuf` - Project root (defaults to auto-detected)
- `skip_audit: bool` - Skip security audit (osv-scanner + npm audit-ci)
- `skip_format: bool` - Skip formatting step
- `skip_versioning: bool` - Skip changeset/versioning prompt
- `max_file_size: u64` - Maximum file size in bytes (default: 10 MiB)
- `no_tui: bool` - Disable TUI (plain output for CI or piped stderr)

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
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`



## resq_cli::commands::pre_commit::run

*Function*

Main entry point for the pre-commit command.

Runs verification checks and formatters with a TUI progress dashboard.

```rust
fn run(args: PreCommitArgs) -> anyhow::Result<()>
```



