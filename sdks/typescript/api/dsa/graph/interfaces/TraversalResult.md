# Interface: TraversalResult\<T\>

Defined in: [graph.ts:90](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L90)

Result of a graph traversal (BFS or DFS).

All three collections cover exactly the vertices reachable from the start,
and are empty when the start vertex is not in the graph.

## Type Parameters

### T

`T`

## Properties

### distances

&gt; **distances**: `Map`\<`T`, `number`\>

Defined in: [graph.ts:102](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L102)

Maps each visited vertex to its distance from the start: hop count for
[Graph.bfs](../classes/Graph#bfs), recursion depth for [Graph.dfs](../classes/Graph#dfs).

***

### parents

&gt; **parents**: `Map`\<`T`, `T` \| `null`\>

Defined in: [graph.ts:97](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L97)

Maps each visited vertex to the vertex it was reached from; the start
vertex maps to `null`. Follow it back to reconstruct a path.

***

### vertices

&gt; **vertices**: `T`[]

Defined in: [graph.ts:92](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L92)

Reachable vertices in the order they were visited.
