**resq_cli > commands > secrets**

# Module: commands::secrets

## Contents

**Structs**

- [`SecretsArgs`](#secretsargs) - CLI arguments for the secrets scanning command.

**Functions**

- [`run`](#run) - Run the secrets scan.

---

## resq_cli::commands::secrets::SecretsArgs

*Struct*

CLI arguments for the secrets scanning command.

**Fields:**
- `root: std::path::PathBuf` - Root directory to scan (defaults to project root)
- `git_only: bool` - Only scan git-tracked files
- `verbose: bool` - Show verbose output (print matched content)
- `allowlist: Option<std::path::PathBuf>` - Path to allowlist file (one pattern per line)
- `staged: bool` - Scan staged changes only (for pre-commit hook integration)
- `history: bool` - Also scan git history (all commits reachable from HEAD)
- `since: Option<String>` - Limit history scan to commits after this rev/date (e.g. "30 days ago", "v1.0.0")

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



## resq_cli::commands::secrets::run

*Function*

Run the secrets scan.

```rust
fn run(args: SecretsArgs) -> anyhow::Result<()>
```



