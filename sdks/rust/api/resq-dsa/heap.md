**resq_dsa > heap**

# Module: heap

## Contents

**Structs**

- [`BoundedHeap`](#boundedheap) - A bounded max-heap that keeps the K entries with the smallest "distance"

---

## resq_dsa::heap::BoundedHeap

*Struct*

A bounded max-heap that keeps the K entries with the smallest "distance"
values.

This data structure is useful for tracking the K-nearest neighbors or
K-shortest paths. The root always contains the entry with the maximum
distance among the kept items. When the heap is full and a new entry has
a smaller distance than the root, the root is evicted and the new entry
takes its place.

# Algorithm

Uses a max-heap where:
- The root (index 0) always holds the entry with the *largest* distance
- When full, only entries with distance less than the current max can be inserted
- Insertion is O(log k) where k is the limit

# Use Cases

- K-nearest neighbor search in path planning
- Finding K shortest paths
- Maintaining top-K results in streaming scenarios

# Examples

```
use resq_dsa::heap::BoundedHeap;

#[derive(Debug)]
struct Waypoint { id: u32, distance: f64 }

let mut h = BoundedHeap::new(3, |w: &Waypoint| w.distance);

h.insert(Waypoint { id: 1, distance: 10.0 });
h.insert(Waypoint { id: 2, distance: 2.0 });
h.insert(Waypoint { id: 3, distance: 7.0 });
h.insert(Waypoint { id: 4, distance: 1.0 }); // evicts id=1 (dist 10)
h.insert(Waypoint { id: 5, distance: 50.0 }); // rejected (too large)

// Returns the 3 nearest waypoints sorted by distance
let sorted: Vec<u32> = h.to_sorted().iter().map(|w| w.id).collect();
assert_eq!(sorted, vec![4, 2, 3]); // nearest first
```

**Generic Parameters:**
- T
- D

**Methods:**

- `fn new(limit: usize, dist: D) -> Self` - Creates a new bounded heap with the given limit and distance function.
- `fn insert(self: & mut Self, entry: T)` - Inserts an entry into the heap.
- `fn peek(self: &Self) -> Option<&T>` - Returns a reference to the entry with the maximum distance (the root).
- `fn to_sorted(self: &Self) -> Vec<&T>` - Returns all entries sorted by distance (ascending, nearest first).
- `fn len(self: &Self) -> usize` - Returns the current number of entries in the heap.
- `fn is_empty(self: &Self) -> bool` - Returns `true` if the heap contains no entries.



