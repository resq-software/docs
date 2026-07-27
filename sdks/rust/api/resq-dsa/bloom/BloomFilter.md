**resq_dsa > bloom > BloomFilter**

# Module: bloom::BloomFilter

## Contents

**Functions**

- [`new`](#new) - Creates a new Bloom filter with the given capacity and error rate.

---

## resq_dsa::bloom::BloomFilter::new

*Function*

Creates a new Bloom filter with the given capacity and error rate.

# Arguments

* `capacity` - Expected maximum number of elements to be added
* `error_rate` - Desired false positive probability (must be in (0, 1))

# Panics

Panics if `error_rate` is not in `(0, 1)` or `capacity` is zero.

# Examples

```
use resq_dsa::bloom::BloomFilter;

// Create a filter for 10000 items with 1% false positive rate
let bf = BloomFilter::new(10000, 0.01);
```

```rust
fn new(capacity: usize, error_rate: f64) -> Self
```



