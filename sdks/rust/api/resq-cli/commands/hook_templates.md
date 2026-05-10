**resq_cli > commands > hook_templates**

# Module: commands::hook_templates

## Contents

**Functions**

- [`hook_content`](#hook_content) - Returns the canonical content for a given hook name, or `None` if the

**Constants**

- [`HOOK_TEMPLATES`](#hook_templates) - Canonical hook templates: `(hook_name, file_content)` tuples.

---

## resq_cli::commands::hook_templates::HOOK_TEMPLATES

*Constant*: `&[(&str, &str)]`

Canonical hook templates: `(hook_name, file_content)` tuples.
The hook names correspond to git hook trigger names.



## resq_cli::commands::hook_templates::hook_content

*Function*

Returns the canonical content for a given hook name, or `None` if the
hook is not one of the known canonical hooks.

```rust
fn hook_content(name: &str) -> Option<&'static str>
```



