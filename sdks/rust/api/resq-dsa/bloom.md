**resq_dsa > bloom**

# Module: bloom

## Contents

**Structs**

- [`BloomFilter`](#bloomfilter) - A space-efficient probabilistic set membership data structure.

---

## resq_dsa::bloom::BloomFilter

*Struct*

A space-efficient probabilistic set membership data structure.

A Bloom filter can tell you if an element is *possibly* in the set
or *definitely* not in the set. False positives are possible (it may
say an element is present when it's not), but false negatives are not.

# Algorithm

Uses `k` independent FNV-1a hash functions (seeded variants) to set bits
in an `m`-bit array. The optimal number of hash functions and bit array
size are calculated from the desired capacity and false positive rate.

# Use Cases

- Deduplication of IDs, sensor readings, or events
- Caching layer to avoid expensive lookups
- Quick membership checks before database queries

# Examples

```
use resq_dsa::bloom::BloomFilter;

let mut bf = BloomFilter::new(1000, 0.01); // 1% false positive rate
bf.add("drone-001");
bf.add("drone-002");

assert!(bf.has("drone-001")); // definitely present
assert!(!bf.has("drone-999")); // definitely not present
```

**Methods:**

- `fn new(capacity: usize, error_rate: f64) -> Self` - Creates a new Bloom filter with the given capacity and error rate.
- `fn from_raw_params(bit_count: usize, hash_count: usize) -> Self` - Creates a new Bloom filter from pre-computed parameters.
- `fn add<impl AsRef<[u8]>>(self: & mut Self, item: impl Trait)` - Adds an element to the filter.
- `fn has<impl AsRef<[u8]>>(self: &Self, item: impl Trait) -> bool` - Checks if an element might be in the set.
- `fn len(self: &Self) -> usize` - Returns the number of elements that have been added to the filter.
- `fn is_empty(self: &Self) -> bool` - Returns `true` if no elements have been added.
- `fn clear(self: & mut Self)` - Resets the filter, removing all elements.



