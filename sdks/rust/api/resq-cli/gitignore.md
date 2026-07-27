**resq_cli > gitignore**

# Module: gitignore

## Contents

**Structs**

- [`Matcher`](#matcher) - A compiled gitignore matcher rooted at a project directory.

**Functions**

- [`load`](#load) - Build a [`Matcher`] for `root`.

---

## resq_cli::gitignore::Matcher

*Struct*

A compiled gitignore matcher rooted at a project directory.

**Methods:**

- `fn is_ignored(self: &Self, path: &Path, is_dir: bool) -> bool` - Returns `true` if `path` is ignored, checking the path itself and every



## resq_cli::gitignore::load

*Function*

Build a [`Matcher`] for `root`.

Loads `root/.gitignore` when present; otherwise seeds the matcher with
[`FALLBACK_EXCLUDES`]. `.git/` and `node_modules/` are always added as
safety nets so they are skipped even if a `.gitignore` omits them.

```rust
fn load(root: &std::path::Path) -> Matcher
```



