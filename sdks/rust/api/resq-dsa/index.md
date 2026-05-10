# resq_dsa

> **Version:** `v0.1.3` · **License:** `Apache-2.0` · **Crate:** [crates.io](https://crates.io/crates/resq-dsa) · **API docs:** [docs.rs](https://docs.rs/resq-dsa/0.1.3)

Production-grade data structures and algorithms — zero external dependencies.

A collection of space-efficient probabilistic data structures and
graph algorithms for general-purpose use.

# Modules

- [`bloom`] - Bloom filter for approximate set membership
- [`count_min`] - Count-Min sketch for frequency estimation
- [`graph`] - Graph algorithms (BFS, Dijkstra, A*)
- [`heap`] - Bounded heap for K-nearest neighbor tracking
- [`trie`] - Trie prefix tree and Rabin-Karp string matching

# Usage

```
use resq_dsa::bloom::BloomFilter;
use resq_dsa::count_min::CountMinSketch;
use resq_dsa::graph::Graph;

// Bloom filter for deduplication
let mut bf = BloomFilter::new(1000, 0.01);
bf.add("drone-001");
assert!(bf.has("drone-001"));

// Count-Min for frequency tracking
let mut cms = CountMinSketch::new(0.01, 0.01);
cms.increment("sensor-reading", 5);

// Graph for pathfinding
let mut g = Graph::<&str>::new();
g.add_edge("base", "waypoint-1", 100);
g.add_edge("waypoint-1", "target", 50);
let (path, cost) = g.dijkstra(&"base", &"target").unwrap();
assert_eq!(path, vec!["base", "waypoint-1", "target"]);
```

## Modules

### [`resq_dsa`](resq_dsa.md)

*5 modules*

### [`bloom`](bloom.md)

*1 struct*

### [`count_min`](count_min.md)

*1 struct*

### [`graph`](graph.md)

*1 struct*

### [`heap`](heap.md)

*1 struct*

### [`trie`](trie.md)

*1 function, 1 struct*

