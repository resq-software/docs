# Class: Graph\<T\>

Defined in: [graph.ts:118](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L118)

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

```typescript
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

## Constructors

### Constructor

> **new Graph**\<`T`\>(`options?`): `Graph`\<`T`\>

Defined in: [graph.ts:127](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L127)

Creates a new Graph

#### Parameters

##### options?

[`GraphOptions`](../interfaces/GraphOptions.md) = `{}`

Configuration options

#### Returns

`Graph`\<`T`\>

#### Throws

Error if options validation fails

## Accessors

### edgeCount

#### Get Signature

> **get** **edgeCount**(): `number`

Defined in: [graph.ts:147](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L147)

Returns the total number of edges in the graph

##### Returns

`number`

***

### vertexCount

#### Get Signature

> **get** **vertexCount**(): `number`

Defined in: [graph.ts:140](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L140)

Returns the number of vertices in the graph

##### Returns

`number`

## Methods

### addEdge()

> **addEdge**(`source`, `target`, `weight?`, `metadata?`): `this`

Defined in: [graph.ts:197](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L197)

Adds an edge between two vertices

#### Parameters

##### source

`T`

##### target

`T`

##### weight?

`number` = `1`

##### metadata?

`Record`\<`string`, `unknown`\>

#### Returns

`this`

This graph for chaining

***

### addVertex()

> **addVertex**(`vertex`, `metadata?`): `this`

Defined in: [graph.ts:175](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L175)

Adds a vertex to the graph

#### Parameters

##### vertex

`T`

##### metadata?

`Record`\<`string`, `unknown`\>

#### Returns

`this`

This graph for chaining

***

### addVertices()

> **addVertices**(`vertices`): `this`

Defined in: [graph.ts:186](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L186)

Adds multiple vertices at once

#### Parameters

##### vertices

`T`[]

#### Returns

`this`

This graph for chaining

***

### astar()

> **astar**(`start`, `end`, `h`): \&#123; `cost`: `number`; `path`: `T`[]; \&#125; \| `null`

Defined in: [graph.ts:434](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L434)

Finds the shortest path using A* search with a heuristic function

#### Parameters

##### start

`T`

Starting vertex

##### end

`T`

Ending vertex

##### h

(`a`, `b`) => `number`

Heuristic function estimating cost from a vertex to end

#### Returns

\&#123; `cost`: `number`; `path`: `T`[]; \&#125; \| `null`

Path and cost, or null if no path exists

***

### bfs()

> **bfs**(`start`): [`TraversalResult`](../interfaces/TraversalResult.md)\<`T`\>

Defined in: [graph.ts:288](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L288)

Breadth-First Search traversal

#### Parameters

##### start

`T`

Starting vertex

#### Returns

[`TraversalResult`](../interfaces/TraversalResult.md)\<`T`\>

Traversal result with vertices, parents, and distances

***

### clear()

> **clear**(): `void`

Defined in: [graph.ts:625](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L625)

Clears all vertices and edges

#### Returns

`void`

***

### dfs()

> **dfs**(`start`): [`TraversalResult`](../interfaces/TraversalResult.md)\<`T`\>

Defined in: [graph.ts:329](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L329)

Depth-First Search traversal

#### Parameters

##### start

`T`

Starting vertex

#### Returns

[`TraversalResult`](../interfaces/TraversalResult.md)\<`T`\>

Traversal result with vertices and parents

***

### findAllPaths()

> **findAllPaths**(`start`, `end`, `maxDepth?`): `T`[][]

Defined in: [graph.ts:478](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L478)

Finds all paths between two vertices (limited by max depth)

#### Parameters

##### start

`T`

Starting vertex

##### end

`T`

Ending vertex

##### maxDepth?

`number` = `10`

Maximum path depth (default: 10)

#### Returns

`T`[][]

Array of all paths found

***

### findShortestPath()

> **findShortestPath**(`start`, `end`): [`PathResult`](../interfaces/PathResult.md)\<`T`\>

Defined in: [graph.ts:365](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L365)

Finds the shortest path between two vertices using Dijkstra's algorithm

#### Parameters

##### start

`T`

Starting vertex

##### end

`T`

Ending vertex

#### Returns

[`PathResult`](../interfaces/PathResult.md)\<`T`\>

Path result with vertices and total distance

***

### getConnectedComponents()

> **getConnectedComponents**(): `T`[][]

Defined in: [graph.ts:594](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L594)

Gets connected components in an undirected graph

#### Returns

`T`[][]

Array of connected components (each component is an array of vertices)

***

### getNeighbors()

> **getNeighbors**(`vertex`): [`Edge`](../interfaces/Edge.md)\<`T`\>[]

Defined in: [graph.ts:264](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L264)

Gets all neighbors of a vertex

#### Parameters

##### vertex

`T`

#### Returns

[`Edge`](../interfaces/Edge.md)\<`T`\>[]

***

### getVertexMetadata()

> **getVertexMetadata**(`vertex`): `Record`\<`string`, `unknown`\> \| `undefined`

Defined in: [graph.ts:278](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L278)

Gets vertex metadata

#### Parameters

##### vertex

`T`

#### Returns

`Record`\<`string`, `unknown`\> \| `undefined`

***

### getVertices()

> **getVertices**(): `T`[]

Defined in: [graph.ts:271](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L271)

Gets all vertices in the graph

#### Returns

`T`[]

***

### hasCycle()

> **hasCycle**(): `boolean`

Defined in: [graph.ts:560](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L560)

Detects if the graph contains a cycle

#### Returns

`boolean`

***

### hasEdge()

> **hasEdge**(`source`, `target`): `boolean`

Defined in: [graph.ts:165](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L165)

Checks if an edge exists between two vertices

#### Parameters

##### source

`T`

##### target

`T`

#### Returns

`boolean`

***

### hasVertex()

> **hasVertex**(`vertex`): `boolean`

Defined in: [graph.ts:158](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L158)

Checks if the graph has a vertex

#### Parameters

##### vertex

`T`

#### Returns

`boolean`

***

### removeEdge()

> **removeEdge**(`source`, `target`): `boolean`

Defined in: [graph.ts:244](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L244)

Removes an edge between two vertices

#### Parameters

##### source

`T`

##### target

`T`

#### Returns

`boolean`

True if edge was removed

***

### removeVertex()

> **removeVertex**(`vertex`): `boolean`

Defined in: [graph.ts:229](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L229)

Removes a vertex and all its edges

#### Parameters

##### vertex

`T`

#### Returns

`boolean`

True if vertex was removed

***

### toAdjacencyMatrix()

> **toAdjacencyMatrix**(): `object`

Defined in: [graph.ts:632](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L632)

Converts graph to adjacency matrix representation

#### Returns

`object`

##### matrix

> **matrix**: `number`[][]

##### vertices

> **vertices**: `T`[]

***

### topologicalSort()

> **topologicalSort**(): `T`[] \| `null`

Defined in: [graph.ts:516](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L516)

Performs topological sort on a directed acyclic graph (DAG)

#### Returns

`T`[] \| `null`

Topologically sorted vertices or null if cycle detected

#### Throws

Error if called on an undirected graph
