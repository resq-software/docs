# Table of Contents

* [resq\_dsa](#resq_dsa)
  * [BloomFilter](#resq_dsa.BloomFilter)
  * [CountMinSketch](#resq_dsa.CountMinSketch)
  * [Graph](#resq_dsa.Graph)
  * [BoundedHeap](#resq_dsa.BoundedHeap)
  * [Trie](#resq_dsa.Trie)
  * [rabin\_karp](#resq_dsa.rabin_karp)
* [resq\_dsa.bloom](#resq_dsa.bloom)
  * [hashlib](#resq_dsa.bloom.hashlib)
  * [math](#resq_dsa.bloom.math)
  * [BloomFilter](#resq_dsa.bloom.BloomFilter)
    * [\_\_init\_\_](#resq_dsa.bloom.BloomFilter.__init__)
    * [add](#resq_dsa.bloom.BloomFilter.add)
    * [has](#resq_dsa.bloom.BloomFilter.has)
* [resq\_dsa.count\_min](#resq_dsa.count_min)
  * [math](#resq_dsa.count_min.math)
  * [CountMinSketch](#resq_dsa.count_min.CountMinSketch)
    * [\_\_init\_\_](#resq_dsa.count_min.CountMinSketch.__init__)
    * [increment](#resq_dsa.count_min.CountMinSketch.increment)
    * [estimate](#resq_dsa.count_min.CountMinSketch.estimate)
* [resq\_dsa.graph](#resq_dsa.graph)
  * [heapq](#resq_dsa.graph.heapq)
  * [deque](#resq_dsa.graph.deque)
  * [Callable](#resq_dsa.graph.Callable)
  * [Graph](#resq_dsa.graph.Graph)
    * [\_\_init\_\_](#resq_dsa.graph.Graph.__init__)
    * [add\_edge](#resq_dsa.graph.Graph.add_edge)
    * [bfs](#resq_dsa.graph.Graph.bfs)
    * [dijkstra](#resq_dsa.graph.Graph.dijkstra)
    * [astar](#resq_dsa.graph.Graph.astar)
* [resq\_dsa.heap](#resq_dsa.heap)
  * [Callable](#resq_dsa.heap.Callable)
  * [Generic](#resq_dsa.heap.Generic)
  * [TypeVar](#resq_dsa.heap.TypeVar)
  * [T](#resq_dsa.heap.T)
  * [BoundedHeap](#resq_dsa.heap.BoundedHeap)
    * [\_\_init\_\_](#resq_dsa.heap.BoundedHeap.__init__)
    * [insert](#resq_dsa.heap.BoundedHeap.insert)
    * [peek](#resq_dsa.heap.BoundedHeap.peek)
    * [to\_sorted](#resq_dsa.heap.BoundedHeap.to_sorted)
    * [size](#resq_dsa.heap.BoundedHeap.size)
* [resq\_dsa.trie](#resq_dsa.trie)
  * [Trie](#resq_dsa.trie.Trie)
    * [\_\_init\_\_](#resq_dsa.trie.Trie.__init__)
    * [insert](#resq_dsa.trie.Trie.insert)
    * [search](#resq_dsa.trie.Trie.search)
    * [starts\_with](#resq_dsa.trie.Trie.starts_with)
  * [rabin\_karp](#resq_dsa.trie.rabin_karp)

<a id="resq_dsa"></a>

# resq\_dsa

ResQ Data Structures and Algorithms Library.

This package provides performant data structures and algorithms
commonly used in the ResQ disaster response system.

Classes:
BoundedHeap: Bounded min-heap for top-k queries.
Graph: Directed weighted graph with pathfinding algorithms.
Trie: Prefix tree for efficient string operations.
BloomFilter: Probabilistic set membership structure.
CountMinSketch: Probabilistic frequency estimation.

Functions:
rabin_karp: Rabin-Karp string pattern matching algorithm.

**Example**:

  >>> from resq_dsa import BoundedHeap, Trie, BloomFilter
  >>> trie = Trie()
  >>> trie.insert("disaster")
  >>> bloom = BloomFilter(capacity=1000)
  >>> bloom.add("emergency")
  >>> bloom.has("emergency")
  True

<a id="resq_dsa.BloomFilter"></a>

## BloomFilter

<a id="resq_dsa.CountMinSketch"></a>

## CountMinSketch

<a id="resq_dsa.Graph"></a>

## Graph

<a id="resq_dsa.BoundedHeap"></a>

## BoundedHeap

<a id="resq_dsa.Trie"></a>

## Trie

<a id="resq_dsa.rabin_karp"></a>

## rabin\_karp

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

<a id="resq_dsa.count_min"></a>

# resq\_dsa.count\_min

Count-Min Sketch probabilistic data structure.

This module provides a Count-Min Sketch implementation for frequency
estimation of elements in a data stream. Useful for top-k queries and
heavy hitter detection with sub-linear space.

<a id="resq_dsa.count_min.math"></a>

## math

<a id="resq_dsa.count_min.CountMinSketch"></a>

## CountMinSketch Objects

```python
class CountMinSketch()
```

Probabilistic data structure for frequency estimation.

The Count-Min Sketch uses multiple hash tables to estimate the count
of elements in a stream with guaranteed error bounds. It provides
an upper bound on frequencies (never underestimates, but may overestimate).

**Attributes**:

- `_w` - Number of columns in the sketch (width).
- `_d` - Number of rows in the sketch (depth).
- `_table` - The hash table storage.
  

**Example**:

  >>> sketch = CountMinSketch(epsilon=0.1, delta=0.01)
  >>> sketch.increment("item1")
  >>> sketch.increment("item1")
  >>> sketch.increment("item2")
  >>> sketch.estimate("item1")  # Returns at least 2
  2
  >>> sketch.estimate("item2")  # Returns at least 1
  1

<a id="resq_dsa.count_min.CountMinSketch.__init__"></a>

#### CountMinSketch.\_\_init\_\_

```python
def __init__(epsilon: float, delta: float) -> None
```

Initialize the Count-Min Sketch.

**Arguments**:

- `epsilon` - Error parameter. The error in estimation is at most epsilon
  with probability delta. Must be in (0, 1).
- `delta` - Confidence parameter. Must be in (0, 1).
  

**Raises**:

- `ValueError` - If epsilon or delta are not in (0, 1).
  

**Example**:

  >>> sketch = CountMinSketch(epsilon=0.1, delta=0.01)

<a id="resq_dsa.count_min.CountMinSketch.increment"></a>

#### CountMinSketch.increment

```python
def increment(key: str, count: int = 1) -> None
```

Increment the count for a key.

**Arguments**:

- `key` - The key to increment.
- `count` - Amount to increment by (default: 1).
  

**Example**:

  >>> sketch = CountMinSketch(epsilon=0.1, delta=0.01)
  >>> sketch.increment("error")
  >>> sketch.increment("error", 5)

<a id="resq_dsa.count_min.CountMinSketch.estimate"></a>

#### CountMinSketch.estimate

```python
def estimate(key: str) -> int
```

Estimate the count for a key.

Returns the minimum across all hash table rows, providing an
upper bound on the true count.

**Arguments**:

- `key` - The key to estimate.
  

**Returns**:

  Estimated count (upper bound).
  

**Example**:

  >>> sketch = CountMinSketch(epsilon=0.1, delta=0.01)
  >>> sketch.increment("event")
  >>> sketch.estimate("event")
  1

<a id="resq_dsa.graph"></a>

# resq\_dsa.graph

Graph data structures and shortest path algorithms.

This module provides a graph representation with implementations of
Breadth-First Search, Dijkstra's algorithm, and A* pathfinding.

<a id="resq_dsa.graph.heapq"></a>

## heapq

<a id="resq_dsa.graph.deque"></a>

## deque

<a id="resq_dsa.graph.Callable"></a>

## Callable

<a id="resq_dsa.graph.Graph"></a>

## Graph Objects

```python
class Graph()
```

Directed weighted graph for pathfinding and traversal.

Supports adding edges and computing shortest paths using BFS,
Dijkstra's algorithm, and A* search.

**Attributes**:

- `_adj` - Adjacency list representation.
- `_counter` - Counter for tiebreaking in priority queue.
  

**Example**:

  >>> g = Graph()
  >>> g.add_edge("A", "B", 1.0)
  >>> g.add_edge("B", "C", 2.0)
  >>> g.bfs("A")
  ['A', 'B', 'C']
  >>> g.dijkstra("A", "C")
- `{'path'` - ['A', 'B', 'C'], 'cost': 3.0&#125;

<a id="resq_dsa.graph.Graph.__init__"></a>

#### Graph.\_\_init\_\_

```python
def __init__() -> None
```

Initialize an empty graph.

<a id="resq_dsa.graph.Graph.add_edge"></a>

#### Graph.add\_edge

```python
def add_edge(from_: object, to: object, weight: float = 1.0) -> None
```

Add a directed edge to the graph.

**Arguments**:

- `from_` - Source node.
- `to` - Destination node.
- `weight` - Edge weight (default: 1.0).
  

**Example**:

  >>> g = Graph()
  >>> g.add_edge("start", "end", 5.0)

<a id="resq_dsa.graph.Graph.bfs"></a>

#### Graph.bfs

```python
def bfs(start: object) -> list[object]
```

Perform Breadth-First Search from start node.

Returns nodes in order of distance from start (unweighted).

**Arguments**:

- `start` - Starting node.
  

**Returns**:

  List of nodes visited in BFS order.
  

**Example**:

  >>> g = Graph()
  >>> g.add_edge("A", "B")
  >>> g.add_edge("A", "C")
  >>> g.bfs("A")
  ['A', 'B', 'C']

<a id="resq_dsa.graph.Graph.dijkstra"></a>

#### Graph.dijkstra

```python
def dijkstra(start: object, end: object) -> dict[str, object] | None
```

Find shortest path using Dijkstra's algorithm.

Computes the minimum cost path between start and end nodes.

**Arguments**:

- `start` - Starting node.
- `end` - Target node.
  

**Returns**:

  Dictionary with 'path' (list of nodes) and 'cost' (float),
  or None if no path exists.
  

**Example**:

  >>> g = Graph()
  >>> g.add_edge("A", "B", 1.0)
  >>> g.add_edge("B", "C", 2.0)
  >>> g.dijkstra("A", "C")
- `{'path'` - ['A', 'B', 'C'], 'cost': 3.0&#125;

<a id="resq_dsa.graph.Graph.astar"></a>

#### Graph.astar

```python
def astar(start: object, end: object,
          h: Callable[[object, object], float]) -> dict[str, object] | None
```

Find shortest path using A* algorithm.

Uses a heuristic function to guide the search toward the goal.

**Arguments**:

- `start` - Starting node.
- `end` - Target node.
- `h` - Heuristic function estimating cost from node to goal.
  

**Returns**:

  Dictionary with 'path' (list of nodes) and 'cost' (float),
  or None if no path exists.
  

**Example**:

  >>> g = Graph()
  >>> g.add_edge("A", "B", 1.0)
  >>> g.add_edge("B", "C", 2.0)
  >>> h = lambda n, goal: abs(ord(goal) - ord(n))  # Simple heuristic
  >>> g.astar("A", "C", h)
- `{'path'` - ['A', 'B', 'C'], 'cost': 3.0&#125;

<a id="resq_dsa.heap"></a>

# resq\_dsa.heap

Bounded heap data structure for top-k queries.

This module provides a bounded min-heap implementation for maintaining
the k smallest (or largest) elements from a stream of data.

<a id="resq_dsa.heap.Callable"></a>

## Callable

<a id="resq_dsa.heap.Generic"></a>

## Generic

<a id="resq_dsa.heap.TypeVar"></a>

## TypeVar

<a id="resq_dsa.heap.T"></a>

#### T

<a id="resq_dsa.heap.BoundedHeap"></a>

## BoundedHeap Objects

```python
class BoundedHeap(Generic[T])
```

Bounded min-heap for tracking top-k elements by distance.

Maintains a fixed-size heap that keeps only the k smallest elements
according to a provided distance/cost function. Useful for k-nearest
neighbors, top-k queries, and streaming data processing.

**Attributes**:

- `_limit` - Maximum number of elements to maintain.
- `_dist` - Function to compute distance/score for elements.
- `_data` - Internal heap storage.
  

**Example**:

  >>> heap = BoundedHeap(limit=3, dist=lambda x: x)
  >>> for i in [5, 2, 8, 1, 9]:
  ...     heap.insert(i)
  >>> heap.to_sorted()
  [1, 2, 5]

<a id="resq_dsa.heap.BoundedHeap.__init__"></a>

#### BoundedHeap.\_\_init\_\_

```python
def __init__(limit: int, dist: Callable[[T], float]) -> None
```

Initialize the bounded heap.

**Arguments**:

- `limit` - Maximum number of elements to maintain.
- `dist` - Function to compute the distance/score for ranking.
  

**Raises**:

- `ValueError` - If limit is less than 1.
  

**Example**:

  >>> heap = BoundedHeap(limit=5, dist=lambda x: abs(x - 10))

<a id="resq_dsa.heap.BoundedHeap.insert"></a>

#### BoundedHeap.insert

```python
def insert(entry: T) -> None
```

Insert an element into the heap.

If the heap is not full, the element is added. If the heap is full
and the new element has a lower distance than the current maximum,
the maximum is replaced with the new element.

**Arguments**:

- `entry` - The element to insert.
  

**Example**:

  >>> heap = BoundedHeap(limit=3, dist=lambda x: x)
  >>> heap.insert(5)
  >>> heap.insert(2)

<a id="resq_dsa.heap.BoundedHeap.peek"></a>

#### BoundedHeap.peek

```python
def peek() -> T | None
```

Return the element with minimum distance without removing it.

**Returns**:

  The element with lowest distance, or None if heap is empty.
  

**Example**:

  >>> heap = BoundedHeap(limit=3, dist=lambda x: x)
  >>> heap.insert(5)
  >>> heap.peek()
  5

<a id="resq_dsa.heap.BoundedHeap.to_sorted"></a>

#### BoundedHeap.to\_sorted

```python
def to_sorted() -> list[T]
```

Return the heap contents sorted by distance.

**Returns**:

  List of elements sorted by distance (ascending).
  

**Example**:

  >>> heap = BoundedHeap(limit=3, dist=lambda x: x)
  >>> heap.insert(5)
  >>> heap.insert(2)
  >>> heap.to_sorted()
  [2, 5]

<a id="resq_dsa.heap.BoundedHeap.size"></a>

#### BoundedHeap.size

```python
@property
def size() -> int
```

Return the current number of elements in the heap.

**Returns**:

  Number of elements currently stored.
  

**Example**:

  >>> heap = BoundedHeap(limit=3, dist=lambda x: x)
  >>> heap.insert(1)
  >>> heap.insert(2)
  >>> heap.size
  2

<a id="resq_dsa.trie"></a>

# resq\_dsa.trie

Trie data structure and string matching algorithms.

This module provides a prefix tree (Trie) implementation for efficient
string storage and retrieval, along with the Rabin-Karp string matching
algorithm for pattern search.

Classes:
    Trie: Prefix tree for word storage and prefix-based retrieval.

Functions:
    rabin_karp: Find all occurrences of a pattern in text using rolling hash.

<a id="resq_dsa.trie.Trie"></a>

## Trie Objects

```python
class Trie()
```

Prefix tree for efficient string storage and retrieval.

A Trie organizes strings by common prefixes, enabling fast lookup
for word existence and autocomplete-style prefix searches.

**Attributes**:

- `_root` - The root node of the Trie.
  

**Example**:

  >>> trie = Trie()
  >>> trie.insert("hello")
  >>> trie.insert("help")
  >>> trie.search("hello")
  True
  >>> trie.starts_with("hel")
  ['hello', 'help']

<a id="resq_dsa.trie.Trie.__init__"></a>

#### Trie.\_\_init\_\_

```python
def __init__() -> None
```

Initialize an empty Trie.

<a id="resq_dsa.trie.Trie.insert"></a>

#### Trie.insert

```python
def insert(word: str) -> None
```

Insert a word into the Trie.

**Arguments**:

- `word` - The word to insert.
  

**Example**:

  >>> trie = Trie()
  >>> trie.insert("python")

<a id="resq_dsa.trie.Trie.search"></a>

#### Trie.search

```python
def search(word: str) -> bool
```

Check if a word exists in the Trie.

**Arguments**:

- `word` - The word to search for.
  

**Returns**:

  True if the word exists, False otherwise.
  

**Example**:

  >>> trie = Trie()
  >>> trie.insert("test")
  >>> trie.search("test")
  True
  >>> trie.search("tes")
  False

<a id="resq_dsa.trie.Trie.starts_with"></a>

#### Trie.starts\_with

```python
def starts_with(prefix: str) -> list[str]
```

Find all words in the Trie that start with a given prefix.

**Arguments**:

- `prefix` - The prefix to search for.
  

**Returns**:

  List of all words that have the given prefix.
  

**Example**:

  >>> trie = Trie()
  >>> trie.insert("hello")
  >>> trie.insert("help")
  >>> trie.insert("hero")
  >>> trie.starts_with("he")
  ['hello', 'help', 'hero']

<a id="resq_dsa.trie.rabin_karp"></a>

#### rabin\_karp

```python
def rabin_karp(text: str, pattern: str) -> list[int]
```

Find all starting positions where pattern occurs in text.

Uses the Rabin-Karp algorithm with rolling hash for efficient string
matching. Returns all positions where the pattern matches.

**Arguments**:

- `text` - The text to search in.
- `pattern` - The pattern to search for.
  

**Returns**:

  List of starting indices where pattern occurs in text.
  

**Example**:

  >>> rabin_karp("ABABDABACDABABCABAB", "ABABCABAB")
  [10]
  >>> rabin_karp("hello world", "wor")
  [6]
  >>> rabin_karp("test", "xyz")
  []

