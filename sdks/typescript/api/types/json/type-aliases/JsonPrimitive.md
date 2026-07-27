# Type Alias: JsonPrimitive

&gt; **JsonPrimitive** = `boolean` \| `null` \| `string` \| `number`

Defined in: [json.ts:33](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/json.ts#L33)

A JSON primitive value: `boolean`, `null`, `string`, or `number`. Note that
`undefined` is **not** a primitive here — it is not representable in JSON, and
`number` nominally excludes `NaN` / `±Infinity` (which `JSON.stringify` emits
as `null`), though the type cannot enforce that finiteness.
