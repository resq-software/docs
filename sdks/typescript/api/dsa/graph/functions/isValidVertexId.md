# Function: isValidVertexId()

&gt; **isValidVertexId**(`id`): `id is string & Brand<"VertexId">`

Defined in: [graph.ts:759](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/graph.ts#L759)

Type guard that validates a vertex id with Effect Schema and narrows it to
the branded [VertexId](../../schemas/type-aliases/VertexId) type.

## Parameters

### id

`unknown`

The value to check.

## Returns

`id is string & Brand<"VertexId">`

`true` if `id` is a valid vertex id.
