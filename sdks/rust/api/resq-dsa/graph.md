**resq_dsa > graph**

# Module: graph

## Contents

**Structs**

- [`Graph`](#graph) - Graph data structure with pathfinding algorithms.

---

## resq_dsa::graph::Graph

*Struct*

Graph data structure with pathfinding algorithms.

Provides BFS, Dijkstra's algorithm, and A* for finding shortest paths
in weighted directed graphs.

# Type Parameters

- `Id`: Node identifier (must be hashable, clonable, comparable)

# Use Cases

- Flight path planning
- Network routing
- Game pathfinding

# Examples

```
use resq_dsa::graph::Graph;

let mut g = Graph::<&str>::new();

// Add edges (from, to, weight)
g.add_edge("base", "waypoint-1", 100);
g.add_edge("waypoint-1", "waypoint-2", 50);
g.add_edge("base", "waypoint-2", 150);
g.add_edge("waypoint-2", "target", 25);

// BFS - visit all reachable nodes
let nodes = g.bfs(&"base");
assert!(nodes.contains(&"target"));

// Dijkstra - shortest path (175 via waypoint-2)
let (path, cost) = g.dijkstra(&"base", &"target").unwrap();
assert_eq!(cost, 175);
```

**Generic Parameters:**
- Id

**Methods:**

- `fn dijkstra(self: &Self, start: &Id, end: &Id) -> Option<(Vec<Id>, u64)>` - Finds the shortest path using Dijkstra's algorithm.
- `fn astar<H>(self: &Self, start: &Id, end: &Id, h: H) -> Option<(Vec<Id>, u64)>` - Finds the shortest path using A* algorithm.
- `fn new() -> Self` - Creates a new empty directed graph.
- `fn add_edge(self: & mut Self, from: Id, to: Id, weight: u64)` - Adds a directed edge from `from` to `to` with the given weight.
- `fn bfs(self: &Self, start: &Id) -> Vec<Id>` - Performs breadth-first search starting from `start`.

**Trait Implementations:**

- **Default**
  - `fn default() -> Self`



