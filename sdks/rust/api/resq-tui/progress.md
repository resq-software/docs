**resq_tui > progress**

# Module: progress

## Contents

**Structs**

- [`ProgressBar`](#progressbar) - Configuration for a progress bar.

---

## resq_tui::progress::ProgressBar

*Struct*

Configuration for a progress bar.

**Methods:**

- `fn new(message: &str, width: usize) -> Self` - Creates a new progress bar with the given width and message.
- `fn render(self: &Self, fraction: f64)` - Renders the progress bar at the given fraction (0.0 – 1.0) to stderr.
- `fn finish(self: &Self)` - Finishes the progress bar with a newline.
- `fn finish_with_message(self: &Self, message: &str)` - Finishes the progress bar and prints a final message.



