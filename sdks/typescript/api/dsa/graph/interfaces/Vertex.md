# Interface: Vertex\<T, M\>

Defined in: [graph.ts:58](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L58)

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

Defined in: [graph.ts:62](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L62)

Outgoing edges

***

### metadata?

&gt; `optional` **metadata?**: `M`

Defined in: [graph.ts:64](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L64)

Optional vertex metadata, typed as `M`.

***

### value

&gt; **value**: `T`

Defined in: [graph.ts:60](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L60)

Vertex value/id
