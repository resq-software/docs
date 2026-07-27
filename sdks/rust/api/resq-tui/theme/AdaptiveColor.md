**resq_tui > theme > AdaptiveColor**

# Module: theme::AdaptiveColor

## Contents

**Functions**

- [`resolve`](#resolve) - Resolves to the appropriate color variant based on the detected

---

## resq_tui::theme::AdaptiveColor::resolve

*Function*

Resolves to the appropriate color variant based on the detected
terminal color mode. Returns [`Color::Reset`] when color is disabled.

```rust
fn resolve(self: &Self) -> Color
```



