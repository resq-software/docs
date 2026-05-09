<a id="resq_dsa.bloom"></a>

# resq\_dsa.bloom

Bloom Filter probabilistic data structure.

This module provides a Bloom Filter implementation for set membership
testing with configurable false positive rate and space efficiency.

<a id="resq_dsa.bloom.hashlib"></a>

## hashlib

<a id="resq_dsa.bloom.math"></a>

## math

<a id="resq_dsa.bloom.BloomFilter"></a>

## BloomFilter Objects

```python
class BloomFilter()
```

Space-efficient probabilistic set membership data structure.

A Bloom Filter can test whether an element is possibly in a set
or definitely not in the set. It may return false positives but
never false negatives.

**Attributes**:

- `_m` - Number of bits        _k: in the filter.
  Number of hash functions.
- `_bits` - Bit array storage.
  

**Example**:

  >>> bf = BloomFilter(capacity=1000)
  >>> bf.add("hello")
  >>> bf.add("world")
  >>> bf.has("hello")
  True
  >>> bf.has("missing")
  False

<a id="resq_dsa.bloom.BloomFilter.__init__"></a>

#### BloomFilter.\_\_init\_\_

```python
def __init__(capacity: int, error_rate: float = 0.01) -> None
```

Initialize the Bloom Filter.

**Arguments**:

- `capacity` - Expected number of elements to be added.
- `error_rate` - Desired false positive rate (default: 0.01 = 1%).
  

**Raises**:

- `ValueError` - If error_rate is not in (0, 1) or capacity &lt; 1.
  

**Example**:

  >>> bf = BloomFilter(capacity=1000, error_rate=0.05)

<a id="resq_dsa.bloom.BloomFilter.add"></a>

#### BloomFilter.add

```python
def add(item: str) -> None
```

Add an item to the Bloom Filter.

**Arguments**:

- `item` - The string item to add.
  

**Example**:

  >>> bf = BloomFilter(capacity=100)
  >>> bf.add("new_item")

<a id="resq_dsa.bloom.BloomFilter.has"></a>

#### BloomFilter.has

```python
def has(item: str) -> bool
```

Check if an item might be in the set.

Returns True if the item may have been added (possibly a false
positive), False if definitely not in the set.

**Arguments**:

- `item` - The item to check.
  

**Returns**:

  True if possibly in set, False if definitely not.
  

**Example**:

  >>> bf = BloomFilter(capacity=100)
  >>> bf.add("present")
  >>> bf.has("present")
  True
  >>> bf.has("absent")
  False
