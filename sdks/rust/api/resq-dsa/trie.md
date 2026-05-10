**resq_dsa > trie**

# Module: trie

## Contents

**Structs**

- [`Trie`](#trie) - A prefix tree (trie) for efficient string storage and retrieval.

**Functions**

- [`rabin_karp`](#rabin_karp) - Rabin-Karp string pattern matching using rolling hash.

---

## resq_dsa::trie::Trie

*Struct*

A prefix tree (trie) for efficient string storage and retrieval.

Supports insertion, exact search, and prefix-based autocomplete.
All operations are O(m) where m is the length of the string.

# Use Cases

- Autocomplete suggestions
- IP address routing tables
- Spell checking
- Word frequency tracking

# Examples

```
use resq_dsa::trie::Trie;

let mut t = Trie::new();
t.insert("drone");
t.insert("drone-001");
t.insert("drone-002");

assert!(t.search("drone"));
assert!(!t.search("dro"));

let suggestions = t.starts_with("drone-");
assert!(suggestions.contains(&"drone-001".to_string()));
```

**Methods:**

- `fn new() -> Self` - Creates a new empty Trie.
- `fn insert(self: & mut Self, word: &str)` - Inserts a word into the trie.
- `fn search(self: &Self, word: &str) -> bool` - Returns `true` if the exact word exists in the trie.
- `fn starts_with(self: &Self, prefix: &str) -> Vec<String>` - Returns all words in the trie that start with the given prefix.

**Trait Implementations:**

- **Default**
  - `fn default() -> Self`



## resq_dsa::trie::rabin_karp

*Function*

Rabin-Karp string pattern matching using rolling hash.

Finds all occurrences of `pattern` in `text` using a polynomial
rolling hash with modular arithmetic. Average case O(n + m).

The algorithm operates on `char` boundaries, so it is
Unicode-aware (multi-byte characters are handled correctly).

# Arguments

* `text` - The text to search in
* `pattern` - The pattern to search for

# Returns

A vector of starting indices (in chars, not bytes) where the pattern matches.

# Examples

```
use resq_dsa::trie::rabin_karp;

let matches = rabin_karp("ababab", "ab");
assert_eq!(matches, vec![0, 2, 4]);

let single = rabin_karp("hello world", "world");
assert_eq!(single, vec![6]);

let none = rabin_karp("hello", "xyz");
assert!(none.is_empty());
```

```rust
fn rabin_karp(text: &str, pattern: &str) -> Vec<usize>
```



