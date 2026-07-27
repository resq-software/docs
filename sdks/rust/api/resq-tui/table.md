**resq_tui > table**

# Module: table

## Contents

**Structs**

- [`Column`](#column) - A column definition.

**Enums**

- [`Align`](#align) - Column alignment.

**Functions**

- [`render_table`](#render_table) - Renders a table to stderr with optional zebra striping and header styling.

---

## resq_tui::table::Align

*Enum*

Column alignment.

**Variants:**
- `Left` - Left-aligned (default).
- `Right` - Right-aligned.

**Traits:** Eq, Copy

**Trait Implementations:**

- **PartialEq**
  - `fn eq(self: &Self, other: &Align) -> bool`
- **Clone**
  - `fn clone(self: &Self) -> Align`
- **Debug**
  - `fn fmt(self: &Self, f: & mut $crate::fmt::Formatter) -> $crate::fmt::Result`



## resq_tui::table::Column

*Struct*

A column definition.

**Fields:**
- `header: String` - Column header text.
- `align: Align` - Alignment.
- `min_width: usize` - Minimum width (0 = auto).

**Methods:**

- `fn new(header: &str) -> Self` - Creates a left-aligned column.
- `fn right(header: &str) -> Self` - Creates a right-aligned column.
- `fn width(self: Self, w: usize) -> Self` - Sets minimum column width.



## resq_tui::table::render_table

*Function*

Renders a table to stderr with optional zebra striping and header styling.

Each row is a `Vec<String>`. Columns define headers and alignment.

# Example
```no_run
use resq_tui::table::{Column, render_table};

let columns = vec![
    Column::new("Name"),
    Column::right("Size"),
    Column::new("Status"),
];
let rows = vec![
    vec!["api".into(), "12 MB".into(), "healthy".into()],
    vec!["worker".into(), "8 MB".into(), "degraded".into()],
];
render_table(&columns, &rows);
```

```rust
fn render_table(columns: &[Column], rows: &[Vec<String>])
```



