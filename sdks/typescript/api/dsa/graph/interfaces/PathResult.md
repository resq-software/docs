# Interface: PathResult\<T\>

Defined in: [graph.ts:75](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L75)

Result of a shortest-path search.

The fields move together: when [found](#found) is `false` (no route exists),
`path` is empty and `distance` is `Number.POSITIVE_INFINITY`. When `found`
is `true`, `path` runs from source to target inclusive and `distance` is its
summed edge weight (`0` for a source-equals-target path).

## Type Parameters

### T

`T`

## Properties

### distance

&gt; **distance**: `number`

Defined in: [graph.ts:79](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L79)

Total summed edge weight; `Infinity` when `found` is `false`.

***

### found

&gt; **found**: `boolean`

Defined in: [graph.ts:81](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L81)

Whether a path from source to target was found.

***

### path

&gt; **path**: `T`[]

Defined in: [graph.ts:77](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L77)

Vertices from source to target inclusive; empty when `found` is `false`.
