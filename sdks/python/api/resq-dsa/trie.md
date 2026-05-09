<a id="resq_dsa.trie"></a>

# resq\_dsa.trie

Trie data structure and string matching algorithms.

This module provides a prefix tree (Trie) implementation for efficient
string storage and retrieval, along with the Rabin-Karp string matching
algorithm for pattern search.

Classes:
    Trie: Prefix tree for word storage and prefix-based retrieval.

Functions:
    rabin_karp: Find all occurrences of a pattern in text using rolling hash.

<a id="resq_dsa.trie.Trie"></a>

## Trie Objects

```python
class Trie()
```

Prefix tree for efficient string storage and retrieval.

A Trie organizes strings by common prefixes, enabling fast lookup
for word existence and autocomplete-style prefix searches.

**Attributes**:

- `_root` - The root node of the Trie.
  

**Example**:

  >>> trie = Trie()
  >>> trie.insert("hello")
  >>> trie.insert("help")
  >>> trie.search("hello")
  True
  >>> trie.starts_with("hel")
  ['hello', 'help']

<a id="resq_dsa.trie.Trie.__init__"></a>

#### Trie.\_\_init\_\_

```python
def __init__() -> None
```

Initialize an empty Trie.

<a id="resq_dsa.trie.Trie.insert"></a>

#### Trie.insert

```python
def insert(word: str) -> None
```

Insert a word into the Trie.

**Arguments**:

- `word` - The word to insert.
  

**Example**:

  >>> trie = Trie()
  >>> trie.insert("python")

<a id="resq_dsa.trie.Trie.search"></a>

#### Trie.search

```python
def search(word: str) -> bool
```

Check if a word exists in the Trie.

**Arguments**:

- `word` - The word to search for.
  

**Returns**:

  True if the word exists, False otherwise.
  

**Example**:

  >>> trie = Trie()
  >>> trie.insert("test")
  >>> trie.search("test")
  True
  >>> trie.search("tes")
  False

<a id="resq_dsa.trie.Trie.starts_with"></a>

#### Trie.starts\_with

```python
def starts_with(prefix: str) -> list[str]
```

Find all words in the Trie that start with a given prefix.

**Arguments**:

- `prefix` - The prefix to search for.
  

**Returns**:

  List of all words that have the given prefix.
  

**Example**:

  >>> trie = Trie()
  >>> trie.insert("hello")
  >>> trie.insert("help")
  >>> trie.insert("hero")
  >>> trie.starts_with("he")
  ['hello', 'help', 'hero']

<a id="resq_dsa.trie.rabin_karp"></a>

#### rabin\_karp

```python
def rabin_karp(text: str, pattern: str) -> list[int]
```

Find all starting positions where pattern occurs in text.

Uses the Rabin-Karp algorithm with rolling hash for efficient string
matching. Returns all positions where the pattern matches.

**Arguments**:

- `text` - The text to search in.
- `pattern` - The pattern to search for.
  

**Returns**:

  List of starting indices where pattern occurs in text.
  

**Example**:

  >>> rabin_karp("ABABDABACDABABCABAB", "ABABCABAB")
  [10]
  >>> rabin_karp("hello world", "wor")
  [6]
  >>> rabin_karp("test", "xyz")
  []
