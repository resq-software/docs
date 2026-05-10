**resq_cli > gitignore**

# Module: gitignore

## Contents

**Functions**

- [`parse_gitignore`](#parse_gitignore) - Parse `.gitignore` from `root` and return a list of simple directory/file
- [`should_skip_path`](#should_skip_path) - Check whether `path` should be skipped based on its directory components

---

## resq_cli::gitignore::parse_gitignore

*Function*

Parse `.gitignore` from `root` and return a list of simple directory/file
names to exclude during traversal.

Strategy (matches the TS `parseGitignore` in `sync-turbo-env.ts`):
- Read `.gitignore`, split into lines
- Strip comments (`#`) and blank lines
- Normalize: remove leading `/` and trailing `/`
- Drop negations (`!`) and wildcard patterns (`*`) — too complex for
  simple component-based matching; these are already handled by git itself
- Always include `.git` and `node_modules` as safety nets

```rust
fn parse_gitignore(root: &std::path::Path) -> Vec<String>
```



## resq_cli::gitignore::should_skip_path

*Function*

Check whether `path` should be skipped based on its directory components
matching any entry in `excludes`.

```rust
fn should_skip_path(path: &std::path::Path, excludes: &[String]) -> bool
```



