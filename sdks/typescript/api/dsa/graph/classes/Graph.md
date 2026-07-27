# Class: Graph\<T, M\>

Defined in: [graph.ts:150](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L150)

Weighted Graph with Adjacency List representation

Supports both directed and undirected graphs with weighted edges.
Implements common graph algorithms including BFS, DFS, Dijkstra's shortest
path, A* search, and topological sort.

Time Complexity:
- addVertex: O(1)
- addEdge: O(1)
- removeVertex: O(V + E)
- removeEdge: O(E)
- BFS/DFS: O(V + E)
- Dijkstra/A*: O((V + E) log V) with priority queue

Space Complexity: O(V + E)

## Example

```ts
const graph = new Graph<string>();
graph.addVertex('A').addVertex('B').addVertex('C');
graph.addEdge('A', 'B', 1);
graph.addEdge('A', 'C', 4);
const path = graph.findShortestPath('A', 'C');
```

## Type Parameters

### T

`T`

Type of vertex identifiers

### M

`M` = `Record`\<`string`, `unknown`\>

Shape of the optional structured metadata attached to
  vertices and edges. Defaults to `Record<string, unknown>` so existing
  `Graph<T>` usage keeps compiling; supply a concrete `M` (for example
  `Graph<string, { lastSeen: number }>`) to get typed reads from
  [Graph.getVertexMetadata](#getvertexmetadata) and [Graph.getNeighbors](#getneighbors).

## Constructors

### Constructor

&gt; **new Graph**\<`T`, `M`\>(`options?`): `Graph`\<`T`, `M`\>

Defined in: [graph.ts:160](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L160)

Creates a new graph.

#### Parameters

##### options?

[`GraphOptions`](../interfaces/GraphOptions) = `{}`

Configuration options.

#### Returns

`Graph`\<`T`, `M`\>

#### Throws

If options validation fails.

## Accessors

### edgeCount

#### Get Signature

&gt; **get** **edgeCount**(): `number`

Defined in: [graph.ts:180](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L180)

Returns the total number of edges in the graph.

##### Returns

`number`

***

### vertexCount

#### Get Signature

&gt; **get** **vertexCount**(): `number`

Defined in: [graph.ts:173](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L173)

Returns the number of vertices in the graph.

##### Returns

`number`

## Methods

### addEdge()

&gt; **addEdge**(`source`, `target`, `weight?`, `metadata?`): `this`

Defined in: [graph.ts:235](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L235)

Adds (or updates) a weighted edge between two vertices, creating either
endpoint if it is missing. For an undirected graph the reverse edge is
added too. Re-adding an existing edge overwrites its weight and metadata.

#### Parameters

##### source

`T`

##### target

`T`

##### weight?

`number` = `1`

##### metadata?

`M`

#### Returns

`this`

This graph, for chaining.

***

### addVertex()

&gt; **addVertex**(`vertex`, `metadata?`): `this`

Defined in: [graph.ts:209](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L209)

Adds a vertex to the graph. A no-op if the vertex already exists.

#### Parameters

##### vertex

`T`

##### metadata?

`M`

#### Returns

`this`

This graph, for chaining.

***

### addVertices()

&gt; **addVertices**(`vertices`): `this`

Defined in: [graph.ts:221](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L221)

Adds multiple vertices at once.

#### Parameters

##### vertices

`T`[]

#### Returns

`this`

This graph, for chaining.

***

### astar()

&gt; **astar**(`start`, `end`, `h`): \{ `cost`: `number`; `path`: `T`[]; \} \| `null`

Defined in: [graph.ts:481](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L481)

Finds the shortest path using A* search guided by a heuristic. Returns an
optimal path when `h` is admissible (never overestimates the true cost).

#### Parameters

##### start

`T`

Starting vertex.

##### end

`T`

Ending vertex.

##### h

(`a`, `b`) =&gt; `number`

Heuristic estimating the cost from a vertex to `end`.

#### Returns

\{ `cost`: `number`; `path`: `T`[]; \} \| `null`

The path and its cost, or `null` if no path exists.

***

### bfs()

&gt; **bfs**(`start`): [`TraversalResult`](../interfaces/TraversalResult)\<`T`\>

Defined in: [graph.ts:330](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L330)

Breadth-first traversal from `start`, visiting nearer vertices first.

#### Parameters

##### start

`T`

Starting vertex.

#### Returns

[`TraversalResult`](../interfaces/TraversalResult)\<`T`\>

Traversal result with vertices, parents, and hop distances. All
  three collections are empty when `start` is not in the graph.

***

### clear()

&gt; **clear**(): `void`

Defined in: [graph.ts:681](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L681)

Clears all vertices and edges.

#### Returns

`void`

***

### dfs()

&gt; **dfs**(`start`): [`TraversalResult`](../interfaces/TraversalResult)\<`T`\>

Defined in: [graph.ts:373](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L373)

Depth-first traversal from `start`, following each branch to its end
before backtracking.

#### Parameters

##### start

`T`

Starting vertex.

#### Returns

[`TraversalResult`](../interfaces/TraversalResult)\<`T`\>

Traversal result with vertices, parents, and depth per vertex.
  All three collections are empty when `start` is not in the graph.

***

### findAllPaths()

&gt; **findAllPaths**(`start`, `end`, `maxDepth?`): `T`[][]

Defined in: [graph.ts:528](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L528)

Finds every simple path between two vertices, bounded by `maxDepth` to
keep the search finite on large or cyclic graphs.

#### Parameters

##### start

`T`

Starting vertex.

##### end

`T`

Ending vertex.

##### maxDepth?

`number` = `10`

Maximum path length in edges. Defaults to `10`.

#### Returns

`T`[][]

All paths found, each an ordered list of vertices.

***

### findShortestPath()

&gt; **findShortestPath**(`start`, `end`): [`PathResult`](../interfaces/PathResult)\<`T`\>

Defined in: [graph.ts:411](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L411)

Finds the shortest path between two vertices with Dijkstra's algorithm.
Assumes non-negative edge weights.

#### Parameters

##### start

`T`

Starting vertex.

##### end

`T`

Ending vertex.

#### Returns

[`PathResult`](../interfaces/PathResult)\<`T`\>

A path result; `found` is `false` with an empty path and
  infinite distance when no route exists.

***

### getConnectedComponents()

&gt; **getConnectedComponents**(): `T`[][]

Defined in: [graph.ts:650](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L650)

Groups vertices into connected components. Intended for undirected
graphs; on a directed graph it treats edges as bidirectional and so
yields weakly-connected components.

#### Returns

`T`[][]

One array of vertices per component.

***

### getNeighbors()

&gt; **getNeighbors**(`vertex`): [`Edge`](../interfaces/Edge)\<`T`, `M`\>[]

Defined in: [graph.ts:305](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L305)

Gets the outgoing edges of a vertex, or an empty array if it is unknown.

#### Parameters

##### vertex

`T`

#### Returns

[`Edge`](../interfaces/Edge)\<`T`, `M`\>[]

***

### getVertexMetadata()

&gt; **getVertexMetadata**(`vertex`): `M` \| `undefined`

Defined in: [graph.ts:319](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L319)

Gets vertex metadata, typed as `M`.

#### Parameters

##### vertex

`T`

#### Returns

`M` \| `undefined`

***

### getVertices()

&gt; **getVertices**(): `T`[]

Defined in: [graph.ts:312](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L312)

Gets all vertices in the graph.

#### Returns

`T`[]

***

### hasCycle()

&gt; **hasCycle**(): `boolean`

Defined in: [graph.ts:613](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L613)

Detects whether the graph contains a cycle. Uses topological sorting for
directed graphs and a parent-aware DFS for undirected ones.

#### Returns

`boolean`

***

### hasEdge()

&gt; **hasEdge**(`source`, `target`): `boolean`

Defined in: [graph.ts:198](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L198)

Checks whether an edge exists from `source` to `target`.

#### Parameters

##### source

`T`

##### target

`T`

#### Returns

`boolean`

***

### hasVertex()

&gt; **hasVertex**(`vertex`): `boolean`

Defined in: [graph.ts:191](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L191)

Checks whether the graph contains a vertex.

#### Parameters

##### vertex

`T`

#### Returns

`boolean`

***

### removeEdge()

&gt; **removeEdge**(`source`, `target`): `boolean`

Defined in: [graph.ts:285](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L285)

Removes the edge from `source` to `target` (and its reverse in an
undirected graph).

#### Parameters

##### source

`T`

##### target

`T`

#### Returns

`boolean`

`true` if a matching edge existed and was removed.

***

### removeVertex()

&gt; **removeVertex**(`vertex`): `boolean`

Defined in: [graph.ts:268](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L268)

Removes a vertex and every edge that touches it.

#### Parameters

##### vertex

`T`

#### Returns

`boolean`

`true` if the vertex existed and was removed.

***

### toAdjacencyMatrix()

&gt; **toAdjacencyMatrix**(): `object`

Defined in: [graph.ts:691](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L691)

Converts the graph to a dense adjacency-matrix representation. Absent
edges are `Infinity` and the diagonal is `0`.

#### Returns

`object`

The vertex order and the corresponding weight matrix.

##### matrix

&gt; **matrix**: `number`[][]

##### vertices

&gt; **vertices**: `T`[]

***

### topologicalSort()

&gt; **topologicalSort**(): `T`[] \| `null`

Defined in: [graph.ts:568](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L568)

Performs a topological sort (Kahn's algorithm) of a directed acyclic
graph.

#### Returns

`T`[] \| `null`

The vertices in a valid topological order, or `null` if the
  graph contains a cycle.

#### Throws

If called on an undirected graph.
