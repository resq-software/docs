# Interface: TraversalResult\<T\>

Defined in: [graph.ts:69](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L69)

Graph traversal result

## Type Parameters

### T

`T`

## Properties

### distances

> **distances**: `Map`\<`T`, `number`\>

Defined in: [graph.ts:75](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L75)

Distance from source (for BFS)

***

### parents

> **parents**: `Map`\<`T`, `T` \| `null`\>

Defined in: [graph.ts:73](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L73)

Parent map for path reconstruction

***

### vertices

> **vertices**: `T`[]

Defined in: [graph.ts:71](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/graph.ts#L71)

Vertices in traversal order
