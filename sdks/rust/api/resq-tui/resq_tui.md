**resq_tui**

# Module: resq_tui

## Contents

**Modules**

- [`terminal`](#terminal) - Terminal lifecycle helpers — init, restore, and event-loop runner.

**Structs**

- [`Theme`](#theme) - Standard `ResQ` TUI Theme.

**Functions**

- [`centered_rect`](#centered_rect) - Helper to create a centered rectangle for popups.
- [`draw_footer`](#draw_footer) - Renders a standardized footer with keyboard shortcuts.
- [`draw_header`](#draw_header) - Renders a standardized header with service metadata and PID.
- [`draw_popup`](#draw_popup) - Renders a centered popup for help or errors.
- [`draw_tabs`](#draw_tabs) - Renders a standardized tab bar.
- [`format_bytes`](#format_bytes) - Formats bytes into human-readable units.
- [`format_duration`](#format_duration) - Formats seconds into human-readable duration.

**Constants**

- [`SPINNER_FRAMES`](#spinner_frames) - Spinner animation frames for loading indicators.

---

## resq_tui::SPINNER_FRAMES

*Constant*: `&[&str]`

Spinner animation frames for loading indicators.



## resq_tui::Theme

*Struct*

Standard `ResQ` TUI Theme.

**Fields:**
- `primary: ratatui::style::Color` - Primary brand color (Cyan)
- `secondary: ratatui::style::Color` - Secondary supporting color (Blue)
- `accent: ratatui::style::Color` - Accent color for PID/Metadata (Magenta)
- `success: ratatui::style::Color` - Success state (Green)
- `warning: ratatui::style::Color` - Warning/Pending state (Yellow)
- `error: ratatui::style::Color` - Error/Critical state (Red)
- `bg: ratatui::style::Color` - Background color
- `fg: ratatui::style::Color` - Foreground text color
- `highlight: ratatui::style::Color` - Highlight/Selection color
- `inactive: ratatui::style::Color` - Inactive/Muted color (`DarkGray`)

**Trait Implementations:**

- **Default**
  - `fn default() -> Self`



## resq_tui::centered_rect

*Function*

Helper to create a centered rectangle for popups.

```rust
fn centered_rect(percent_x: u16, percent_y: u16, r: ratatui::layout::Rect) -> ratatui::layout::Rect
```



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



## Module: terminal

Terminal lifecycle helpers — init, restore, and event-loop runner.



