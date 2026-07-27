**resq_dsa > count_min > CountMinSketch**

# Module: count_min::CountMinSketch

## Contents

**Functions**

- [`estimate`](#estimate) - Estimates the count for a key.
- [`from_raw_params`](#from_raw_params) - Creates a new Count-Min sketch from pre-computed dimensions.
- [`new`](#new) - Creates a new Count-Min sketch with the given error parameters.

---

## resq_dsa::count_min::CountMinSketch::estimate

*Function*

Estimates the count for a key.

Accepts any type that can be converted to a byte slice.

Returns the minimum value across all hash table rows.
The estimate is guaranteed to be at least the true count,
but may be higher due to hash collisions from other keys.

# Examples

```
use resq_dsa::count_min::CountMinSketch;

let mut cms = CountMinSketch::new(0.01, 0.01);
cms.increment("drone-001", 10);
cms.increment("drone-001", 5);

let estimate = cms.estimate("drone-001");
assert!(estimate >= 15); // never undercounts
```

```rust
fn estimate<impl AsRef<[u8]>>(self: &Self, key: impl Trait) -> u64
```



## resq_dsa::count_min::CountMinSketch::from_raw_params

*Function*

Creates a new Count-Min sketch from pre-computed dimensions.

Use this in `no_std` environments where you pre-compute `width`
and `depth` externally. With `std`, prefer [`new`][Self::new].

# Arguments

* `width` - Number of columns (derived from epsilon: `ceil(e / epsilon)`)
* `depth` - Number of rows / hash functions (derived from delta: `ceil(ln(1 / delta))`)

# Panics

Panics if `width` or `depth` is zero.

```rust
fn from_raw_params(width: usize, depth: usize) -> Self
```



## resq_dsa::count_min::CountMinSketch::new

*Function*

Creates a new Count-Min sketch with the given error parameters.

# Arguments

* `epsilon` - Error parameter (estimates are within epsilon * N with high probability)
* `delta` - Failure probability (1 - delta is the success probability)

# Panics

Panics if epsilon or delta are not in `(0, 1)`.

# Examples

```
use resq_dsa::count_min::CountMinSketch;

// Creates a sketch where estimates are within 1% of true count
// with 99% probability
let cms = CountMinSketch::new(0.01, 0.01);
```
Creates a new Count-Min sketch with the given error bounds.

Requires the `std` feature for floating-point math. In `no_std`
environments, use [`from_raw_params`][Self::from_raw_params].

```rust
fn new(epsilon: f64, delta: f64) -> Self
```



