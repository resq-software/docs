**resq_dsa > count_min**

# Module: count_min

## Contents

**Structs**

- [`CountMinSketch`](#countminsketch) - A space-efficient probabilistic data structure for frequency estimation.

---

## resq_dsa::count_min::CountMinSketch

*Struct*

A space-efficient probabilistic data structure for frequency estimation.

The Count-Min sketch can estimate the frequency of events with guaranteed
error bounds. It may overcount but never undercounts (like Bloom filters,
this is a property of the algorithm).

# Algorithm

Uses `depth` independent FNV-1a hash functions (seeded variants) to map
elements to positions in `width` columns. The estimated count is the
minimum across all hash table rows.

# Error Bounds

- Error is at most `epsilon * total_count` with probability `1 - delta`
- Smaller epsilon/delta values require more memory

# Use Cases

- Tracking event frequencies
- Network traffic analysis
- Distributed counting without central aggregation

# Examples

```
use resq_dsa::count_min::CountMinSketch;

let mut cms = CountMinSketch::new(0.01, 0.01);
cms.increment("sensor-temp-high", 5);
cms.increment("sensor-temp-high", 3);
cms.increment("sensor-humidity", 1);

let temp_estimate = cms.estimate("sensor-temp-high");
assert!(temp_estimate >= 8); // never undercounts
```

**Methods:**

- `fn new(epsilon: f64, delta: f64) -> Self` - Creates a new Count-Min sketch with the given error parameters.
- `fn from_raw_params(width: usize, depth: usize) -> Self` - Creates a new Count-Min sketch from pre-computed dimensions.
- `fn increment<impl AsRef<[u8]>>(self: & mut Self, key: impl Trait, count: u64)` - Increments the count for a key by the given amount.
- `fn estimate<impl AsRef<[u8]>>(self: &Self, key: impl Trait) -> u64` - Estimates the count for a key.



