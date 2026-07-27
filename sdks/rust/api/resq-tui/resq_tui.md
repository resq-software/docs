**resq_tui**

# Module: resq_tui

## Contents

**Modules**

- [`console`](#console) - TTY-gated console message formatters for non-TUI CLI output.
- [`detect`](#detect) - Terminal environment detection.
- [`progress`](#progress) - Non-TUI progress bar for CLI output.
- [`spinner`](#spinner) - Spinner frames and non-TUI spinner for CLI output.
- [`table`](#table) - Styled table renderer for non-TUI CLI output.
- [`terminal`](#terminal) - Terminal lifecycle helpers — init, restore, and event-loop runner.
- [`theme`](#theme) - Centralized theme and adaptive colors for `ResQ` TUI and CLI output.

**Functions**

- [`centered_rect`](#centered_rect) - Helper to create a centered rectangle for popups.
- [`draw_footer`](#draw_footer) - Renders a standardized footer with keyboard shortcuts.
- [`draw_header`](#draw_header) - Renders a standardized header with service metadata and PID.
- [`draw_popup`](#draw_popup) - Renders a centered popup for help or errors.
- [`draw_tabs`](#draw_tabs) - Renders a standardized tab bar.
- [`format_bytes`](#format_bytes) - Formats bytes into human-readable units.
- [`format_duration`](#format_duration) - Formats seconds into human-readable duration.

---

## resq_tui::centered_rect

*Function*

Helper to create a centered rectangle for popups.

```rust
fn centered_rect(percent_x: u16, percent_y: u16, r: ratatui::layout::Rect) -> ratatui::layout::Rect
```



## Module: console

TTY-gated console message formatters for non-TUI CLI output.

Mirrors the gh-aw `pkg/console/console.go` pattern:
- 14+ named message formatters (success, error, warning, info, …)
- All styling gated through [`crate::detect::should_style`]
- Output routing: diagnostics → stderr, structured data → stdout
- In non-TTY / accessible mode, emoji prefixes still appear but ANSI
  color codes are stripped.



## Module: detect

Terminal environment detection.

Mirrors the gh-aw pattern of gating all styling through environment checks:
- TTY detection via `crossterm::tty::IsTty`
- `NO_COLOR` standard (&lt;https://no-color.org/>)
- `TERM=dumb` detection
- `ACCESSIBLE` env var for screen-reader mode

All console output formatting in [`crate::console`] is gated through
[`should_style`] so no ANSI codes bleed into pipes or redirects.



## resq_tui::draw_footer

*Function*

Renders a standardized footer with keyboard shortcuts.

```rust
fn draw_footer(frame: & mut ratatui::Frame, area: ratatui::layout::Rect, keys: &[(&str, &str)], theme: &Theme)
```



## resq_tui::draw_header

*Function*

Renders a standardized header with service metadata and PID.

```rust
fn draw_header(frame: & mut ratatui::Frame, area: ratatui::layout::Rect, title: &str, status: &str, status_color: ratatui::style::Color, pid: Option<i32>, url: &str, theme: &Theme)
```



## resq_tui::draw_popup

*Function*

Renders a centered popup for help or errors.

```rust
fn draw_popup(frame: & mut ratatui::Frame, area: ratatui::layout::Rect, title: &str, lines: &[ratatui::text::Line], percent_x: u16, percent_y: u16, theme: &Theme)
```



## resq_tui::draw_tabs

*Function*

Renders a standardized tab bar.

```rust
fn draw_tabs(frame: & mut ratatui::Frame, area: ratatui::layout::Rect, titles: Vec<&str>, selected: usize)
```



## resq_tui::format_bytes

*Function*

Formats bytes into human-readable units.

```rust
fn format_bytes(bytes: u64) -> String
```



## resq_tui::format_duration

*Function*

Formats seconds into human-readable duration.

```rust
fn format_duration(seconds: u64) -> String
```



## Module: progress

Non-TUI progress bar for CLI output.

Renders a styled progress bar to stderr using adaptive colors.
Falls back to a plain ASCII bar in accessible/non-TTY mode.

Mirrors gh-aw's `pkg/console/progress.go` pattern with adaptive colors
instead of hardcoded hex strings.



## Module: spinner

Spinner frames and non-TUI spinner for CLI output.

Provides:
- [`SPINNER_FRAMES`] — Braille animation frames for TUI usage.
- [`Spinner`] — A thread-safe stderr spinner that respects
  [`crate::detect::should_style`] and falls back to plain dots in
  accessible mode.



## Module: table

Styled table renderer for non-TUI CLI output.

Mirrors gh-aw's `RenderTable` with zebra-striped rows and
adaptive colors. Falls back to plain aligned text when styling
is disabled.



## Module: terminal

Terminal lifecycle helpers — init, restore, and event-loop runner.



## Module: theme

Centralized theme and adaptive colors for `ResQ` TUI and CLI output.

Mirrors the gh-aw `pkg/styles/theme.go` pattern:
- All colors defined as [`AdaptiveColor`] with explicit light and dark
  variants (Dracula-inspired dark palette).
- No direct color usage outside this module and [`crate::console`].
- Resolution is gated through [`crate::detect::detect_color_mode`].



