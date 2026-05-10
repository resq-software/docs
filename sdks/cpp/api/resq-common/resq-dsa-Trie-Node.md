## Node

Internal trie node.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `std::unordered_map< char, std::unique_ptr< Node > >` | [`ch`](#ch)  | Children nodes keyed by character. |
| `bool` | [`is_end`](#is_end)  | Whether this node marks end of a word. |

---

#### ch

```cpp
std::unordered_map< char, std::unique_ptr< Node > > ch
```

Children nodes keyed by character.

---

#### is_end

```cpp
bool is_end = false
```

Whether this node marks end of a word.

