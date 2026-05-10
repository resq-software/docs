## BloomFilter

```cpp
#include <bloom.hpp>
```

Bloom filter for probabilistic set membership.

Implements a space-efficient probabilistic set data structure. Supports insert and membership test operations.

#### Parameters
* `N/A` Uses internal bit array (not template parameter)

Filter capacity must be >= 1 

False positive rate must be in (0, 1)

:::note
Memory usage: approximately 1.2 bytes per expected element at 1% FPR 

:::

:::note
Uses FNV-1a hash with double hashing for k independent hash functions 

:::

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`BloomFilter`](#bloomfilter-1) `inline` | Construct a Bloom filter with specified capacity and false positive rate. |
| `void` | [`add`](#add) `inline` | Insert an element into the filter. |
| `bool` | [`has`](#has) `const` `inline` | Check if element may be in the set. |
| `void` | [`clear`](#clear) `inline` | Reset all bits to zero. |

---

#### BloomFilter

`inline`

```cpp
inline BloomFilter(std::size_t cap, double err)
```

Construct a Bloom filter with specified capacity and false positive rate.

#### Parameters
* `expected_elements` Maximum number of elements expected to be inserted 

* `false_positive_rate` Desired false positive rate (0.0 to 1.0)

#### Exceptions
* `std::invalid_argument` If capacity &lt; 1 

* `std::invalid_argument` If false_positive_rate &lt;= 0.0 or >= 1.0

Filter is initialized with all bits set to 0

## Example:

```cpp
// Create filter for 10000 elements with 1% false positive rate
[BloomFilter](#bloomfilter-1) filter(10000, 0.01);
```

---

#### add

`inline`

```cpp
inline void add(std::string_view item)
```

Insert an element into the filter.

#### Parameters
* `item` String to insert

Element will return true for subsequent [has()](#has) calls 

:::note
May set additional bits (affects other elements' FPR)

:::

:::note
Thread-safe: caller must ensure no concurrent access 

:::

---

#### has

`const` `inline`

```cpp
inline bool has(std::string_view item) const
```

Check if element may be in the set.

#### Parameters
* `item` String to check 

#### Returns
true if element possibly exists, false if definitely not exists

#### Parameters
* `true` Element may be in set (or false positive) 

* `false` Element is definitely not in set

:::note
False positives are possible (returns true when element wasn't added) 

:::

:::note
False negatives are impossible (returns false only for non-members)

:::

## Example:

```cpp
if (filter.has("drone_001")) {
    // High confidence element was added
    // But could be false positive
} else {
    // Definitely not in set
}
```

---

#### clear

`inline`

```cpp
inline void clear()
```

Reset all bits to zero.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `std::vector< uint8_t >` | [`bits_`](#bits_)  | Bit array storage. |
| `std::size_t` | [`k_`](#k_)  | Number of hash functions. |
| `std::size_t` | [`m_`](#m_)  | Number of bits in filter. |

---

#### bits_

```cpp
std::vector< uint8_t > bits_
```

Bit array storage.

---

#### k_

```cpp
std::size_t k_
```

Number of hash functions.

---

#### m_

```cpp
std::size_t m_
```

Number of bits in filter.

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `std::size_t` | [`hash_fn`](#hash_fn) `const` `inline` | Compute hash at index i using double hashing technique. |

---

#### hash_fn

`const` `inline`

```cpp
inline std::size_t hash_fn(std::string_view s, uint32_t seed) const
```

Compute hash at index i using double hashing technique.

Uses FNV-1a as base hash, then applies secondary hash for generating k independent hash functions via h(i) = h1 + i*h2

#### Parameters
* `s` String to hash 

* `seed` Secondary hash seed 

#### Returns
Hash value modulo m_

