**resq_cli > utils**

# Module: utils

## Contents

**Functions**

- [`find_project_root`](#find_project_root) - Finds the project root by climbing up the directory tree from the CWD.

---

## resq_cli::utils::find_project_root

*Function*

Finds the project root by climbing up the directory tree from the CWD.
Returns the current directory if no root marker is found.

```rust
fn find_project_root() -> std::path::PathBuf
```



