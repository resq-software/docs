**resq_tui > spinner**

# Module: spinner

## Contents

**Structs**

- [`Spinner`](#spinner) - A non-TUI stderr spinner.

**Constants**

- [`SPINNER_FRAMES`](#spinner_frames) - Braille spinner animation frames (for ratatui TUI rendering).

---

## resq_tui::spinner::SPINNER_FRAMES

*Constant*: `&[&str]`

Braille spinner animation frames (for ratatui TUI rendering).



## resq_tui::spinner::Spinner

*Struct*

A non-TUI stderr spinner.

Mirrors gh-aw's `pkg/console/spinner.go` with thread-safe lifecycle.

# Example
```no_run
use resq_tui::spinner::Spinner;

let spinner = Spinner::start("Loading data");
// ... do work ...
spinner.stop_with_message("✅ Loaded 42 items");
```

**Methods:**

- `fn start(message: &str) -> Self` - Starts a spinner on stderr with the given message.
- `fn stop_with_message(self: Self, message: &str)` - Stops the spinner and prints a final message.
- `fn stop(self: Self)` - Stops the spinner without printing a final message.

**Trait Implementations:**

- **Drop**
  - `fn drop(self: & mut Self)`



