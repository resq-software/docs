# Function: addValidatedEdge()

&gt; **addValidatedEdge**(`graph`, `source`, `target`, `weight?`): `boolean`

Defined in: [graph.ts:740](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L740)

Validates an edge with Effect Schema before adding it to a string-keyed
graph, so malformed input is rejected instead of silently corrupting it.

## Parameters

### graph

[`Graph`](../classes/Graph)\<`string`\>

The target graph.

### source

`string`

Source vertex id.

### target

`string`

Target vertex id.

### weight?

`number` = `1`

Edge weight. Defaults to `1`.

## Returns

`boolean`

`true` if the edge passed validation and was added.
