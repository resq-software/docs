## CountMinSketch

```cpp
#include <count_min.hpp>
```

Count-Min sketch for frequency estimation.

Probabilistic counter that over-estimates frequencies. Uses d hash functions and w counters per row to provide (epsilon, delta) guarantees.

eps in (0, 1) - error parameter 

delta in (0, 1) - confidence parameter

:::note
Memory: O(1/eps * log(1/delta)) counters 

:::

:::note
Update: O(log(1/delta)) operations 

:::

:::note
Query: O(log(1/delta)) operations

:::

:::warning
Returned estimate is always >= true count (upper bound) 

:::

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`CountMinSketch`](#countminsketch-1) | Construct a Count-Min sketch. |
| `void` | [`increment`](#increment) | Increment count for a key. |
| `uint64_t` | [`estimate`](#estimate) `const` | Estimate frequency of a key. |
| `void` | [`clear`](#clear-1) | Reset all counters to zero. |

---

#### CountMinSketch

`inline`

```cpp
inline CountMinSketch(double eps, double delta)
```

Construct a Count-Min sketch.

#### Parameters
* `eps` Error parameter (epsilon). Error &lt;= eps * N with probability delta Smaller eps = more memory, more accuracy 

* `delta` Confidence parameter. Error guarantee holds with probability (1 - delta) Smaller delta = more memory, higher confidence

#### Exceptions
* `std::invalid_argument` If eps &lt;= 0 or eps >= 1 

* `std::invalid_argument` If delta &lt;= 0 or delta >= 1

## Example:

```cpp
// 1% error, 99% confidence
[CountMinSketch](#countminsketch-1) cms(0.01, 0.01);

// 5% error, 95% confidence (smaller)
[CountMinSketch](#countminsketch-1) cms_small(0.05, 0.05);
```

---

#### increment

`inline`

```cpp
inline void increment(std::string_view key, uint64_t count)
```

Increment count for a key.

#### Parameters
* `key` String identifier to count 

* `count` Amount to add (default: 1)

Count for key is incremented by count 

:::note
Updates all d hash function buckets 

:::

---

#### estimate

`const`

```cpp
inline uint64_t estimate(std::string_view key) const
```

Estimate frequency of a key.

#### Parameters
* `key` Key to estimate count for 

#### Returns
Estimated count (guaranteed >= true count)

#### Parameters
* `>=` Actual frequency (upper bound) 

* `<=` eps * N (theoretical upper bound)

:::note
Returns minimum across all hash function buckets 

:::

:::note
Always returns estimate >= true count 

:::

---

#### clear

`inline`

```cpp
inline void clear()
```

Reset all counters to zero.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `std::vector< std::vector< uint64_t > >` | [`table_`](#table_)  | Table of counters [hash_function][bucket]. |
| `std::size_t` | [`w_`](#w_)  | Number of buckets (w) |
| `std::size_t` | [`d_`](#d_)  | Number of hash functions (d) |

---

#### table_

```cpp
std::vector< std::vector< uint64_t > > table_
```

Table of counters [hash_function][bucket].

---

#### w_

```cpp
std::size_t w_
```

Number of buckets (w)

---

#### d_

```cpp
std::size_t d_
```

Number of hash functions (d)

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `std::size_t` | [`hash_fn`](#hash_fn-1) `const` | Compute hash using double hashing technique. |

---

#### hash_fn

`const`

```cpp
inline std::size_t hash_fn(std::string_view key, uint32_t seed) const
```

Compute hash using double hashing technique.

