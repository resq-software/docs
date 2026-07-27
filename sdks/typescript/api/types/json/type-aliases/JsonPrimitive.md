# Type Alias: JsonPrimitive

&gt; **JsonPrimitive** = `boolean` \| `null` \| `string` \| `number`

Defined in: [json.ts:33](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/json.ts#L33)

A JSON primitive value: `boolean`, `null`, `string`, or `number`. Note that
`undefined` is **not** a primitive here — it is not representable in JSON, and
`number` nominally excludes `NaN` / `±Infinity` (which `JSON.stringify` emits
as `null`), though the type cannot enforce that finiteness.
