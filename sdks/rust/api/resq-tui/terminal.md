**resq_tui > terminal**

# Module: terminal

## Contents

**Structs**

- [`TerminalGuard`](#terminalguard) - RAII guard that owns a [`Term`] and automatically calls [`restore`] on drop.

**Functions**

- [`init`](#init) - Initialise raw mode and enter the alternate screen.
- [`restore`](#restore) - Leave the alternate screen and disable raw mode.
- [`run_loop`](#run_loop) - Run a standard TUI event loop with the given app.

**Traits**

- [`TuiApp`](#tuiapp) - Implement this trait on your app state to use [`run_loop`].

**Type Aliases**

- [`Term`](#term) - A `ratatui` terminal backed by Crossterm.

---

## resq_tui::terminal::Term

*Type Alias*: `ratatui::Terminal<ratatui::backend::CrosstermBackend<io::Stdout>>`

A `ratatui` terminal backed by Crossterm.



## resq_tui::terminal::TerminalGuard

*Struct*

RAII guard that owns a [`Term`] and automatically calls [`restore`] on drop.

This ensures the terminal is cleaned up even on panic or early `?` returns.
Use [`Deref`] / [`DerefMut`] to access the underlying [`Term`] transparently
(e.g. `guard.draw(|f| ...)` works).

**Trait Implementations:**

- **Drop**
  - `fn drop(self: & mut Self)`
- **DerefMut**
  - `fn deref_mut(self: & mut Self) -> & mut <Self as >::Target`
- **Deref**
  - `fn deref(self: &Self) -> &<Self as >::Target`



## resq_tui::terminal::TuiApp

*Trait*

Implement this trait on your app state to use [`run_loop`].

**Methods:**

- `draw`: Draw the current frame.
- `handle_key`: Handle a key event. Return `false` to exit the loop.



## resq_tui::terminal::init

*Function*

Initialise raw mode and enter the alternate screen.

Returns a [`TerminalGuard`] that will call [`restore`] automatically when
dropped, ensuring cleanup even on panic or early `?` returns.

# Errors
Propagates any I/O error from Crossterm or Ratatui.

```rust
fn init() -> anyhow::Result<TerminalGuard>
```



## resq_tui::terminal::restore

*Function*

Leave the alternate screen and disable raw mode.

Safe to call even if the terminal is in a partially-initialised state.

```rust
fn restore()
```



## resq_tui::terminal::run_loop

*Function*

Run a standard TUI event loop with the given app.

`poll_ms` controls how frequently the loop polls for keyboard input.
Ctrl+C always exits. The terminal is **not** automatically initialised
or restored — wrap the call site with [`init`] / [`restore`].

# Errors
Propagates draw or event errors, and errors from the app's `handle_key`.

```rust
fn run_loop(terminal: & mut Term, poll_ms: u64, app: & mut dyn TuiApp) -> anyhow::Result<()>
```



