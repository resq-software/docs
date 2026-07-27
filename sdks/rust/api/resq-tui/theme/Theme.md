**resq_tui > theme > Theme**

# Module: theme::Theme

## Contents

**Functions**

- [`adaptive`](#adaptive) - Creates a theme that adapts to the detected terminal color mode.

---

## resq_tui::theme::Theme::adaptive

*Function*

Creates a theme that adapts to the detected terminal color mode.

Uses [`AdaptiveColor::resolve`] for every field. This is the
recommended constructor for new code.

```rust
fn adaptive() -> Self
```



