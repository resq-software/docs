**resq_tui > theme**

# Module: theme

## Contents

**Structs**

- [`AdaptiveColor`](#adaptivecolor) - A color that adapts to the terminal background (light vs dark).
- [`Theme`](#theme) - Standard `ResQ` TUI Theme with adaptive color support.

**Constants**

- [`COLOR_ACCENT`](#color_accent) - Accent color for metadata (Magenta/Pink).
- [`COLOR_BG`](#color_bg) - Background.
- [`COLOR_ERROR`](#color_error) - Error/critical state (Red).
- [`COLOR_FG`](#color_fg) - Foreground text.
- [`COLOR_HIGHLIGHT`](#color_highlight) - Highlight / selection background.
- [`COLOR_INACTIVE`](#color_inactive) - Inactive / muted / comment.
- [`COLOR_PRIMARY`](#color_primary) - Primary brand color (Cyan).
- [`COLOR_PROGRESS_EMPTY`](#color_progress_empty) - Progress bar empty track.
- [`COLOR_PROGRESS_END`](#color_progress_end) - Progress bar gradient end.
- [`COLOR_PROGRESS_START`](#color_progress_start) - Progress bar gradient start.
- [`COLOR_SECONDARY`](#color_secondary) - Secondary supporting color (Blue/Purple).
- [`COLOR_SUCCESS`](#color_success) - Success state (Green).
- [`COLOR_WARNING`](#color_warning) - Warning/pending state (Yellow/Orange).

---

## resq_tui::theme::AdaptiveColor

*Struct*

A color that adapts to the terminal background (light vs dark).

Mirrors `lipgloss.AdaptiveColor` from the Charmbracelet ecosystem.

**Fields:**
- `light: ratatui::style::Color` - Color for light terminal backgrounds.
- `dark: ratatui::style::Color` - Color for dark terminal backgrounds.

**Methods:**

- `fn resolve(self: &Self) -> Color` - Resolves to the appropriate color variant based on the detected

**Traits:** Copy

**Trait Implementations:**

- **Clone**
  - `fn clone(self: &Self) -> AdaptiveColor`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`



## resq_tui::theme::COLOR_ACCENT

*Constant*: `AdaptiveColor`

Accent color for metadata (Magenta/Pink).



## resq_tui::theme::COLOR_BG

*Constant*: `AdaptiveColor`

Background.



## resq_tui::theme::COLOR_ERROR

*Constant*: `AdaptiveColor`

Error/critical state (Red).



## resq_tui::theme::COLOR_FG

*Constant*: `AdaptiveColor`

Foreground text.



## resq_tui::theme::COLOR_HIGHLIGHT

*Constant*: `AdaptiveColor`

Highlight / selection background.



## resq_tui::theme::COLOR_INACTIVE

*Constant*: `AdaptiveColor`

Inactive / muted / comment.



## resq_tui::theme::COLOR_PRIMARY

*Constant*: `AdaptiveColor`

Primary brand color (Cyan).



## resq_tui::theme::COLOR_PROGRESS_EMPTY

*Constant*: `AdaptiveColor`

Progress bar empty track.



## resq_tui::theme::COLOR_PROGRESS_END

*Constant*: `AdaptiveColor`

Progress bar gradient end.



## resq_tui::theme::COLOR_PROGRESS_START

*Constant*: `AdaptiveColor`

Progress bar gradient start.



## resq_tui::theme::COLOR_SECONDARY

*Constant*: `AdaptiveColor`

Secondary supporting color (Blue/Purple).



## resq_tui::theme::COLOR_SUCCESS

*Constant*: `AdaptiveColor`

Success state (Green).



## resq_tui::theme::COLOR_WARNING

*Constant*: `AdaptiveColor`

Warning/pending state (Yellow/Orange).



## resq_tui::theme::Theme

*Struct*

Standard `ResQ` TUI Theme with adaptive color support.

Consumers should call [`Theme::adaptive`] to get colors that match the
detected terminal background, or [`Theme::default`] for the classic
hardcoded dark palette (backward-compatible).

**Fields:**
- `primary: ratatui::style::Color` - Primary brand color (Cyan).
- `secondary: ratatui::style::Color` - Secondary supporting color (Blue/Purple).
- `accent: ratatui::style::Color` - Accent color for metadata (Magenta/Pink).
- `success: ratatui::style::Color` - Success state (Green).
- `warning: ratatui::style::Color` - Warning/pending state (Yellow/Orange).
- `error: ratatui::style::Color` - Error/critical state (Red).
- `bg: ratatui::style::Color` - Background color.
- `fg: ratatui::style::Color` - Foreground text color.
- `highlight: ratatui::style::Color` - Highlight/selection color.
- `inactive: ratatui::style::Color` - Inactive/muted/comment color.

**Methods:**

- `fn adaptive() -> Self` - Creates a theme that adapts to the detected terminal color mode.

**Trait Implementations:**

- **Default**
  - `fn default() -> Self` - Creates the classic hardcoded dark-theme palette.



