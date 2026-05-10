**resq_ai > token**

# Module: token

## Contents

**Functions**

- [`estimate_tokens`](#estimate_tokens) - Estimate token count using the chars/4 heuristic.
- [`truncate_to_budget`](#truncate_to_budget) - Truncate text to fit within a token budget.

---

## resq_ai::token::estimate_tokens

*Function*

Estimate token count using the chars/4 heuristic.

```rust
fn estimate_tokens(text: &str) -> usize
```



## resq_ai::token::truncate_to_budget

*Function*

Truncate text to fit within a token budget.
Cuts at line boundaries to avoid broken diff hunks.

```rust
fn truncate_to_budget(text: &str, max_tokens: usize) -> &str
```



