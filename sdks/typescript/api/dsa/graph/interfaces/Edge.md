# Interface: Edge\<T, M\>

Defined in: [graph.ts:43](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L43)

Edge in the graph.

## Type Parameters

### T

`T`

Type of vertex identifiers.

### M

`M` = `Record`\<`string`, `unknown`\>

Shape of the optional structured metadata. Defaults to
  `Record<string, unknown>` so unparameterised `Edge<T>` keeps the previous
  loosely-typed metadata; supply a concrete `M` for typed reads.

## Properties

### metadata?

&gt; `optional` **metadata?**: `M`

Defined in: [graph.ts:49](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L49)

Optional metadata, typed as `M`.

***

### target

&gt; **target**: `T`

Defined in: [graph.ts:45](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L45)

Target vertex

***

### weight

&gt; **weight**: `number`

Defined in: [graph.ts:47](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L47)

Edge weight (default: 1)
