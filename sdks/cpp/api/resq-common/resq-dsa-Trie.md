## Trie

```cpp
#include <trie.hpp>
```

[Trie](#trie) (prefix tree) for efficient string prefix operations.

Space-optimized prefix tree supporting insert, exact search, and prefix-based autocomplete operations.

:::note
Memory: O(total characters stored) - shared prefixes 

:::

:::note
Operations: O(length of string) for insert/search

:::

## Example:

```cpp
Trie t;
t.insert("api");
t.insert("app");
t.insert("apple");

t.search("api");              // true
t.search("ap");               // false
t.starts_with("ap");          // {"api", "app", "apple"}
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`insert`](#insert-1) | Insert a word into the trie. |
| `bool` | [`search`](#search) `const` | Search for exact word. |
| `std::vector< std::string >` | [`starts_with`](#starts_with-1) `const` | Find all words starting with prefix. |

---

#### insert

`inline`

```cpp
inline void insert(std::string_view w)
```

Insert a word into the trie.

#### Parameters
* `w` Word to insert (ASCII characters)

Word can be found via [search()](#search)

:::note
Duplicate inserts are idempotent 

:::

---

#### search

`const`

```cpp
inline bool search(std::string_view w) const
```

Search for exact word.

#### Parameters
* `w` Word to search for 

#### Returns
true if word exists in trie

---

#### starts_with

`const`

```cpp
inline std::vector< std::string > starts_with(std::string_view prefix) const
```

Find all words starting with prefix.

#### Parameters
* `prefix` Prefix to search for 

#### Returns
Vector of all words starting with prefix

Returns empty vector if prefix not found

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `Node` | [`root_`](#root_)  | Root node. |

---

#### root_

```cpp
Node root_
```

Root node.

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`collect`](#collect) `const` | Collect all words with given prefix. |

---

#### collect

`const`

```cpp
inline void collect(const Node & n, std::string & acc, std::vector< std::string > & out) const
```

Collect all words with given prefix.

