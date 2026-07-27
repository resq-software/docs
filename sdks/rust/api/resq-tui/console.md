**resq_tui > console**

# Module: console

## Contents

**Functions**

- [`error`](#error) - Prints an error message to stderr.
- [`format_command`](#format_command) - Formats a command reference: `▶ <command>`
- [`format_count`](#format_count) - Formats a count/metric message: `📊 <message>`
- [`format_error`](#format_error) - Formats an error message: `❌ <message>`
- [`format_info`](#format_info) - Formats an info message: `ℹ️  <message>`
- [`format_list_header`](#format_list_header) - Formats a list header.
- [`format_list_item`](#format_list_item) - Formats a list item: `  • <message>`
- [`format_location`](#format_location) - Formats a location/path message: `📁 <message>`
- [`format_progress`](#format_progress) - Formats a progress/in-flight message: `⏳ <message>`
- [`format_prompt`](#format_prompt) - Formats a prompt message: `? <message>`
- [`format_search`](#format_search) - Formats a search/scan message: `🔍 <message>`
- [`format_section_header`](#format_section_header) - Formats a section header with a rule line.
- [`format_success`](#format_success) - Formats a success message: `✅ <message>`
- [`format_verbose`](#format_verbose) - Formats a verbose/debug message (dim).
- [`format_warning`](#format_warning) - Formats a warning message: `⚠️  <message>`
- [`info`](#info) - Prints an info message to stderr.
- [`progress`](#progress) - Prints a progress message to stderr.
- [`section`](#section) - Prints a section header to stderr.
- [`success`](#success) - Prints a success message to stderr.
- [`verbose`](#verbose) - Prints a verbose/debug message to stderr.
- [`warning`](#warning) - Prints a warning message to stderr.

---

## resq_tui::console::error

*Function*

Prints an error message to stderr.

```rust
fn error(message: &str)
```



## resq_tui::console::format_command

*Function*

Formats a command reference: `▶ <command>`

```rust
fn format_command(command: &str) -> String
```



## resq_tui::console::format_count

*Function*

Formats a count/metric message: `📊 <message>`

```rust
fn format_count(message: &str) -> String
```



## resq_tui::console::format_error

*Function*

Formats an error message: `❌ <message>`

```rust
fn format_error(message: &str) -> String
```



## resq_tui::console::format_info

*Function*

Formats an info message: `ℹ️  <message>`

```rust
fn format_info(message: &str) -> String
```



## resq_tui::console::format_list_header

*Function*

Formats a list header.

```rust
fn format_list_header(header: &str) -> String
```



## resq_tui::console::format_list_item

*Function*

Formats a list item: `  • <message>`

```rust
fn format_list_item(message: &str) -> String
```



## resq_tui::console::format_location

*Function*

Formats a location/path message: `📁 <message>`

```rust
fn format_location(message: &str) -> String
```



## resq_tui::console::format_progress

*Function*

Formats a progress/in-flight message: `⏳ <message>`

```rust
fn format_progress(message: &str) -> String
```



## resq_tui::console::format_prompt

*Function*

Formats a prompt message: `? <message>`

```rust
fn format_prompt(message: &str) -> String
```



## resq_tui::console::format_search

*Function*

Formats a search/scan message: `🔍 <message>`

```rust
fn format_search(message: &str) -> String
```



## resq_tui::console::format_section_header

*Function*

Formats a section header with a rule line.

```rust
fn format_section_header(header: &str) -> String
```



## resq_tui::console::format_success

*Function*

Formats a success message: `✅ <message>`

```rust
fn format_success(message: &str) -> String
```



## resq_tui::console::format_verbose

*Function*

Formats a verbose/debug message (dim).

```rust
fn format_verbose(message: &str) -> String
```



## resq_tui::console::format_warning

*Function*

Formats a warning message: `⚠️  <message>`

```rust
fn format_warning(message: &str) -> String
```



## resq_tui::console::info

*Function*

Prints an info message to stderr.

```rust
fn info(message: &str)
```



## resq_tui::console::progress

*Function*

Prints a progress message to stderr.

```rust
fn progress(message: &str)
```



## resq_tui::console::section

*Function*

Prints a section header to stderr.

```rust
fn section(header: &str)
```



## resq_tui::console::success

*Function*

Prints a success message to stderr.

```rust
fn success(message: &str)
```



## resq_tui::console::verbose

*Function*

Prints a verbose/debug message to stderr.

```rust
fn verbose(message: &str)
```



## resq_tui::console::warning

*Function*

Prints a warning message to stderr.

```rust
fn warning(message: &str)
```



