## Graph

```cpp
#include <graph.hpp>
```

Generic directed weighted graph.

Implements an adjacency list graph with support for:

* Breadth-first search (unweighted shortest path)

* Dijkstra's algorithm (weighted shortest path)

* A* search (heuristic-guided pathfinding)

#### Parameters
* `Id` Vertex identifier type (must be hashable) 

* `IdHash` Hash function for Id type (default: std::hash&lt;Id>)

:::note
Edge weights must be non-negative for Dijkstra and A* 

:::

:::note
Self-loops and duplicate edges are supported 

:::

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`add_edge`](#add_edge) | Add a directed edge to the graph. |
| `std::vector< Id >` | [`bfs`](#bfs) `const` | Breadth-first search from a start vertex. |
| `std::optional< PathResult >` | [`dijkstra`](#dijkstra) `const` | Dijkstra's algorithm for shortest path. |
| `std::optional< PathResult >` | [`astar`](#astar) `const` | A* pathfinding algorithm. |

---

#### add_edge

`inline`

```cpp
inline void add_edge(const Id & from, const Id & to, double w)
```

Add a directed edge to the graph.

#### Parameters
* `from` Source vertex 

* `to` Destination vertex 

* `w` Edge weight (default: 1.0)

Edge from->to exists with weight w 

:::note
If edge already exists, adds additional parallel edge

:::

## Example:

```cpp
Graph<int> g;
g.add_edge(1, 2, 5.0);   // Weighted edge
g.add_edge(2, 3);        // Unweighted edge (weight=1)
```

---

#### bfs

`const`

```cpp
inline std::vector< Id > bfs(const Id & start) const
```

Breadth-first search from a start vertex.

Returns all vertices reachable from start in BFS order. Uses O(V + E) time where V = vertices, E = edges.

#### Parameters
* `start` Starting vertex 

#### Returns
Vector of visited vertices in BFS order

Returns empty vector if start not in graph 

:::note
Does not consider edge weights (treats all as weight 1) 

:::

---

#### dijkstra

`const`

```cpp
inline std::optional< PathResult > dijkstra(const Id & start, const Id & end) const
```

Dijkstra's algorithm for shortest path.

Finds the shortest path between two vertices using Dijkstra's algorithm with a binary heap priority queue.

#### Parameters
* `start` Starting vertex 

* `end` Destination vertex 

#### Returns
[PathResult](./resq-dsa-Graph-PathResult.md#pathresult) if path exists, std::nullopt otherwise

On success, path contains vertices from start to end 

cost equals sum of edge weights along path

:::note
Time complexity: O((V + E) log V) 

:::

:::note
Edge weights must be non-negative

:::

## Example:

```cpp
Graph<std::string> g;
g.add_edge("home", "store", 5.0);
g.add_edge("store", "work", 3.0);

auto result = g.dijkstra("home", "work");
if (result) {
    // result->path = ["home", "store", "work"]
    // result->cost = 8.0
}
```

---

#### astar

`const`

```cpp
inline std::optional< PathResult > astar(const Id & start, const Id & end, std::function< double(const Id &, const Id &)> h) const
```

A* pathfinding algorithm.

Finds shortest path using heuristic-guided search. More efficient than Dijkstra when a good heuristic is available.

#### Parameters
* `start` Starting vertex 

* `end` Destination vertex 

* `h` Heuristic function: estimated cost from node to goal Must be admissible (never overestimate)

#### Returns
[PathResult](./resq-dsa-Graph-PathResult.md#pathresult) if path exists, std::nullopt otherwise

On success, path contains vertices from start to end 

cost equals g-score (actual cost, not f-score)

:::note
Time complexity: O(E log V) in best case with good heuristic 

:::

:::note
Heuristic must be admissible for optimal results 

:::

:::note
Edge weights must be non-negative

:::

## Example:

```cpp
Graph<int> g;
// Add edges representing a grid...

// Manhattan distance heuristic for grid
auto h = [&](int from, int to) {
    return std::abs(from - to);  // Simplified
};

auto result = g.astar(0, 100, h);
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `std::unordered_map< Id, std::vector< std::pair< Id, double > >, IdHash >` | [`adj_`](#adj_)  | Adjacency list: vertex -> list of (neighbor, weight) pairs. |

---

#### adj_

```cpp
std::unordered_map< Id, std::vector< std::pair< Id, double > >, IdHash > adj_
```

Adjacency list: vertex -> list of (neighbor, weight) pairs.

