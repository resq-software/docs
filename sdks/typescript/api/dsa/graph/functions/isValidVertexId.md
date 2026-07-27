# Function: isValidVertexId()

&gt; **isValidVertexId**(`id`): `id is string & Brand<"VertexId">`

Defined in: [graph.ts:759](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/graph.ts#L759)

Type guard that validates a vertex id with Effect Schema and narrows it to
the branded [VertexId](../../schemas/type-aliases/VertexId) type.

## Parameters

### id

`unknown`

The value to check.

## Returns

`id is string & Brand<"VertexId">`

`true` if `id` is a valid vertex id.
