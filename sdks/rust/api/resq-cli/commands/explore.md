**resq_cli > commands > explore**

# Module: commands::explore

## Contents

**Structs**

- [`AsmArgs`](#asmargs) - Arguments for the 'asm' (resq-bin) command
- [`CleanArgs`](#cleanargs) - Arguments for the 'clean' (resq-clean) command
- [`ExploreArgs`](#exploreargs) - Arguments for the 'explore' (resq-perf) command

**Functions**

- [`run_asm`](#run_asm) - Run resq-bin (Binary Explorer)
- [`run_clean`](#run_clean) - Run resq-clean (Workspace Cleaner)
- [`run_explore`](#run_explore) - Run resq-perf (Performance Explorer)

---

## resq_cli::commands::explore::AsmArgs

*Struct*

Arguments for the 'asm' (resq-bin) command

**Fields:**
- `file: Option<String>` - Analyze a single binary path
- `dir: Option<String>` - Analyze binaries under a directory
- `recursive: bool` - Recursively traverse directory in batch mode
- `ext: Option<String>` - Optional suffix filter in batch mode (e.g. .so, .o)
- `config: Option<String>` - Optional resq-bin config TOML path
- `no_cache: bool` - Disable cache reads/writes
- `rebuild_cache: bool` - Force cache rebuild
- `no_disasm: bool` - Disable disassembly and only collect metadata
- `max_functions: Option<usize>` - Maximum functions to disassemble per binary
- `tui: bool` - Force interactive TUI mode
- `plain: bool` - Use non-interactive plain output
- `json: bool` - Emit JSON report output

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



## resq_cli::commands::explore::CleanArgs

*Struct*

Arguments for the 'clean' (resq-clean) command

**Fields:**
- `dry_run: bool` - Preview what would be deleted without removing anything

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



## resq_cli::commands::explore::ExploreArgs

*Struct*

Arguments for the 'explore' (resq-perf) command

**Fields:**
- `url: String` - Service URL to monitor
- `refresh_ms: u64` - Refresh rate in milliseconds

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



## resq_cli::commands::explore::run_asm

*Function*

Run resq-bin (Binary Explorer)

```rust
fn run_asm(args: AsmArgs) -> anyhow::Result<()>
```



## resq_cli::commands::explore::run_clean

*Function*

Run resq-clean (Workspace Cleaner)

```rust
fn run_clean(args: CleanArgs) -> anyhow::Result<()>
```



## resq_cli::commands::explore::run_explore

*Function*

Run resq-perf (Performance Explorer)

```rust
fn run_explore(args: ExploreArgs) -> anyhow::Result<()>
```



