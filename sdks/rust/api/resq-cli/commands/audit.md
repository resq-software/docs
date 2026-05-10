**resq_cli > commands > audit**

# Module: commands::audit

## Contents

**Structs**

- [`AuditArgs`](#auditargs) - CLI arguments for the security and quality audit command.

**Functions**

- [`run`](#run) - Run the security and quality audit.

---

## resq_cli::commands::audit::AuditArgs

*Struct*

CLI arguments for the security and quality audit command.

**Fields:**
- `root: std::path::PathBuf` - Root directory to start search from
- `level: String` - Minimum npm vulnerability severity to fail on (critical, high, moderate, low)
- `report_type: String` - audit-ci report verbosity (important, full, summary)
- `skip_prepare: bool` - Skip the yarn.lock generation step required by audit-ci
- `skip_npm: bool` - Skip the npm audit-ci pass
- `skip_osv: bool` - Skip the Google OSV Scanner pass (covers Rust, npm, Python, .NET, C/C++)
- `osv_format: String` - OSV Scanner output format (table, json, sarif, gh-annotations)
- `skip_react: bool` - Skip the react-doctor pass on the web dashboard
- `react_target: Option<std::path::PathBuf>` - Path to the React/Next.js project for react-doctor
- `react_diff: Option<String>` - Only scan React files changed vs this base branch (e.g. "main")
- `react_min_score: u8` - Minimum react-doctor health score to pass (0–100)

**Trait Implementations:**

- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`
- **FromArgMatches**
  - `fn from_arg_matches(__clap_arg_matches: &clap::ArgMatches) -> ::std::result::Result<Self, clap::Error>`
  - `fn from_arg_matches_mut(__clap_arg_matches: & mut clap::ArgMatches) -> ::std::result::Result<Self, clap::Error>`
  - `fn update_from_arg_matches(self: & mut Self, __clap_arg_matches: &clap::ArgMatches) -> ::std::result::Result<(), clap::Error>`
  - `fn update_from_arg_matches_mut(self: & mut Self, __clap_arg_matches: & mut clap::ArgMatches) -> ::std::result::Result<(), clap::Error>`
- **Args**
  - `fn group_id() -> Option<clap::Id>`
  - `fn augment_args<'b>(__clap_app: clap::Command) -> clap::Command`
  - `fn augment_args_for_update<'b>(__clap_app: clap::Command) -> clap::Command`



## resq_cli::commands::audit::run

*Function*

Run the security and quality audit.

```rust
fn run(args: AuditArgs) -> anyhow::Result<()>
```



