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
