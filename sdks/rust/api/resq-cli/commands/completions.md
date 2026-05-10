**resq_cli > commands > completions**

# Module: commands::completions

## Contents

**Structs**

- [`CompletionsArgs`](#completionsargs) - Arguments for `resq completions <shell>`.

**Functions**

- [`run`](#run) - Emit a completion script for the given shell to `stdout`.

---

## resq_cli::commands::completions::CompletionsArgs

*Struct*

Arguments for `resq completions <shell>`.

**Fields:**
- `shell: clap_complete::Shell` - Target shell.

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



## resq_cli::commands::completions::run

*Function*

Emit a completion script for the given shell to `stdout`.

Takes the already-built root `Command` so the caller (`main`) owns the parser
definition and this module stays decoupled from the `Cli` struct layout.

```rust
fn run(args: CompletionsArgs, cmd: clap::Command) -> anyhow::Result<()>
```



