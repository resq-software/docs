# dsa

Copyright 2026 ResQ Software.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 
```
http://www.apache.org/licenses/LICENSE-2.0
```
 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Probabilistic set membership data structure

Space-efficient probabilistic data structure that tests whether an element is a member of a set. May produce false positives but never false negatives.

Use cases:

* Quick membership checks for large sets

* Spam filtering

* Distributed cache lookup

* Network packet deduplication

:::note
False positive rate is configurable at construction 

:::

:::warning
Not suitable for security-critical membership tests 

:::

:::warning
Cannot remove elements (use CountingBloomFilter instead)

:::

## Example:

```cpp
[BloomFilter](./resq-dsa-BloomFilter.md#bloomfilter) filter(10000, 0.01); // 10k elements, 1% false positive rate
filter.add("drone_001");
filter.add("drone_002");

if (filter.has("drone_001")) {
    // Likely in set (may be false positive)
}
```

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 
```
http://www.apache.org/licenses/LICENSE-2.0
```
 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Count-Min sketch for frequency estimation

Probabilistic data structure for estimating frequencies of events. Provides space-efficient counting with guaranteed error bounds.

Use cases:

* Network traffic analysis

* Heavy hitter detection

* Approximate frequency queries

:::note
Guarantees estimate >= true count (upper bound) 

:::

:::note
Actual error is at most eps * N with probability delta 

:::

:::warning
Not suitable for exact counting

:::

## Example:

```cpp
// Create sketch with 1% error bound, 99% confidence
[CountMinSketch](./resq-dsa-CountMinSketch.md#countminsketch) sketch(0.01, 0.01);

for (const auto& req : requests) {
    sketch.increment(req.ip_address);
}

// Estimate frequency (may be overestimate)
uint64_t freq = sketch.estimate("192.168.1.1");
```

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 
```
http://www.apache.org/licenses/LICENSE-2.0
```
 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

[Graph](./resq-dsa-Graph.md#graph) data structures and pathfinding algorithms

Provides generic graph representation with common pathfinding algorithms. Supports both unweighted and weighted edges with Dijkstra and A* search.

:::note
Uses adjacency list representation for memory efficiency 

:::

:::note
Id type must be hashable and equality-comparable

:::

## Example:

```cpp
[Graph<std::string>](./resq-dsa-Graph.md#graph) g;
g.[add_edge](./resq-dsa-Graph.md#add_edge)("A", "B", 1.0);
g.[add_edge](./resq-dsa-Graph.md#add_edge)("B", "C", 2.0);

auto result = g.[dijkstra](./resq-dsa-Graph.md#dijkstra)("A", "C");
if (result) {
    std::cout << "Path: ";
    for (const auto& node : result->path) {
        std::cout << node << " ";
    }
}
```

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 
```
http://www.apache.org/licenses/LICENSE-2.0
```
 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Fixed-size priority queue with bounded capacity

A bounded min-heap that maintains at most N elements, automatically evicting the element with the highest distance value when full. Useful for K-nearest-neighbors, top-K selection, and beam search.

:::note
Uses max-heap internally (highest distance at root), but exposes the element with minimum distance value as the "best" 

:::

:::warning
The comparison function must be consistent - if f(a) &lt; f(b) and f(b) &lt; f(c), then f(a) &lt; f(c)

:::

## Example:

```cpp
// Keep top 5 closest drones to target
[BoundedHeap<Drone>](./resq-dsa-BoundedHeap.md#boundedheap) closest(5, [](const Drone& d) {
    return distance(d.position, target);
});

for (const auto& drone : all_drones) {
    closest.[insert](./resq-dsa-BoundedHeap.md#insert)(drone);
}

// Get sorted results
auto results = closest.to_sorted();
```

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 
```
http://www.apache.org/licenses/LICENSE-2.0
```
 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

[Trie](./resq-dsa-Trie.md#trie) (prefix tree) and string matching algorithms

Provides efficient string data structures for:

* Prefix-based autocomplete

* String storage and lookup

* Pattern matching

:::note
Uses case-sensitive ASCII character comparison 

:::

:::warning
Not suitable for Unicode strings without modification

:::

## Example:

```cpp
[Trie](./resq-dsa-Trie.md#trie) trie;
trie.[insert](./resq-dsa-Trie.md#insert-1)("drone");
trie.[insert](./resq-dsa-Trie.md#insert-1)("drone_001");
trie.[insert](./resq-dsa-Trie.md#insert-1)("drone_002");

auto suggestions = trie.[starts_with](./resq-dsa-Trie.md#starts_with-1)("drone_");
// suggestions = {"drone_001", "drone_002"}
```

### Classes

| Name | Description |
|------|-------------|
| [`BloomFilter`](./resq-dsa-BloomFilter.md#bloomfilter) | Bloom filter for probabilistic set membership. |
| [`BoundedHeap`](./resq-dsa-BoundedHeap.md#boundedheap) | Bounded heap for top-K element selection. |
| [`CountMinSketch`](./resq-dsa-CountMinSketch.md#countminsketch) | Count-Min sketch for frequency estimation. |
| [`Graph`](./resq-dsa-Graph.md#graph) | Generic directed weighted graph. |
| [`Trie`](./resq-dsa-Trie.md#trie) | [Trie](./resq-dsa-Trie.md#trie) (prefix tree) for efficient string prefix operations. |

### Functions

| Return | Name | Description |
|--------|------|-------------|
| `std::vector< std::size_t >` | [`rabin_karp`](#rabin_karp) | Rabin-Karp string matching algorithm. |

---

#### rabin_karp

`inline`

```cpp
inline std::vector< std::size_t > rabin_karp(const std::string & text, const std::string & pat)
```

Rabin-Karp string matching algorithm.

Uses rolling hash for O(n + m) average-case string matching. Useful for finding all occurrences of a pattern in text.

#### Parameters
* `text` Text to search in 

* `pat` Pattern to search for 

#### Returns
Vector of starting positions where pattern matches

:::note
Uses base 31 with modulo 1,000,000,007 

:::

:::note
False matches are possible due to hash collisions

:::

## Example:

```cpp
auto matches = [rabin_karp](#rabin_karp)("ABABDABACDABABCABAB", "ABABCABAB");
// matches = {10}
```

