**resq_cli > commands > docs**

# Module: commands::docs

## Contents

**Structs**

- [`DocsArgs`](#docsargs) - Arguments for the `docs` command.

**Functions**

- [`run`](#run) - Run the documentation export and publication process.

---

## resq_cli::commands::docs::DocsArgs

*Struct*

Arguments for the `docs` command.

**Fields:**
- `export_only: bool` - Only export the specifications locally without publishing
- `publish: bool` - Publish the specifications to the documentation repository
- `dry_run: bool` - Dry run: show what would be done without executing

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



## resq_cli::commands::docs::run

*Function*

Run the documentation export and publication process.

# Errors
Returns an error if any of the export or publication steps fail,
or if there are issues accessing the file system or GitHub API.

```rust
fn run(args: DocsArgs) -> anyhow::Result<()>
```



