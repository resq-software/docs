**resq_tui > detect**

# Module: detect

## Contents

**Enums**

- [`ColorMode`](#colormode) - Detected terminal color capability.

**Functions**

- [`detect_color_mode`](#detect_color_mode) - Returns the detected color mode for adaptive color selection.
- [`is_accessible_mode`](#is_accessible_mode) - Returns `true` if the environment requests accessible / plain output.
- [`is_tty_stderr`](#is_tty_stderr) - Returns `true` if stderr is connected to a terminal.
- [`is_tty_stdout`](#is_tty_stdout) - Returns `true` if stdout is connected to a terminal.
- [`should_style`](#should_style) - Returns `true` if styled output should be emitted to stderr.

---

## resq_tui::detect::ColorMode

*Enum*

Detected terminal color capability.

**Variants:**
- `Dark` - Dark terminal background (default assumption).
- `Light` - Light terminal background.
- `None` - No color support — plain text only.

**Traits:** Eq, Copy

**Trait Implementations:**

- **PartialEq**
  - `fn eq(self: &Self, other: &ColorMode) -> bool`
- **Clone**
  - `fn clone(self: &Self) -> ColorMode`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`



## resq_tui::detect::detect_color_mode

*Function*

Returns the detected color mode for adaptive color selection.

```rust
fn detect_color_mode() -> ColorMode
```



## resq_tui::detect::is_accessible_mode

*Function*

Returns `true` if the environment requests accessible / plain output.

Checks: `NO_COLOR`, `TERM=dumb`, `ACCESSIBLE`.

```rust
fn is_accessible_mode() -> bool
```



## resq_tui::detect::is_tty_stderr

*Function*

Returns `true` if stderr is connected to a terminal.

```rust
fn is_tty_stderr() -> bool
```



## resq_tui::detect::is_tty_stdout

*Function*

Returns `true` if stdout is connected to a terminal.

```rust
fn is_tty_stdout() -> bool
```



## resq_tui::detect::should_style

*Function*

Returns `true` if styled output should be emitted to stderr.

This is the master gate — all console formatters check this before
applying any ANSI styling.

```rust
fn should_style() -> bool
```



