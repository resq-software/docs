# Interface: Vertex\<T, M\>

Defined in: [graph.ts:58](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L58)

Vertex with adjacency list.

## Type Parameters

### T

`T`

Type of vertex identifiers.

### M

`M` = `Record`\<`string`, `unknown`\>

Shape of the optional structured metadata (see [Edge](./Edge)).

## Properties

### edges

&gt; **edges**: [`Edge`](./Edge)\<`T`, `M`\>[]

Defined in: [graph.ts:62](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L62)

Outgoing edges

***

### metadata?

&gt; `optional` **metadata?**: `M`

Defined in: [graph.ts:64](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L64)

Optional vertex metadata, typed as `M`.

***

### value

&gt; **value**: `T`

Defined in: [graph.ts:60](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L60)

Vertex value/id
