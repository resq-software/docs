**resq_cli > commands > copyright**

# Module: commands::copyright

## Contents

**Structs**

- [`CopyrightArgs`](#copyrightargs) - CLI arguments for the copyright header management command.

**Functions**

- [`run`](#run) - Run the copyright header management command.

---

## resq_cli::commands::copyright::CopyrightArgs

*Struct*

CLI arguments for the copyright header management command.

**Fields:**
- `license: String` - License type (apache-2.0, mit, gpl-3.0, bsd-3-clause)
- `author: String` - Copyright holder name
- `year: Option<String>` - Copyright year (defaults to current year)
- `force: bool` - Overwrite existing headers
- `dry_run: bool` - Preview changes without writing files
- `check: bool` - Check for missing headers (CI mode, exits non-zero if any missing)
- `verbose: bool` - Print detailed processing info
- `glob: Vec<String>` - Glob patterns to match files (e.g. "src/**/*.rs")
- `ext: Vec<String>` - File extensions to include (e.g. --ext rs,js,py)
- `exclude: Vec<String>` - Patterns to exclude from processing

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



## resq_cli::commands::copyright::run

*Function*

Run the copyright header management command.
Runs the copyright tool with the provided arguments.

# Errors
Returns an error if the license year is invalid, the license file cannot be read,
or if processing any of the files fails.

```rust
fn run(args: &CopyrightArgs) -> anyhow::Result<()>
```



