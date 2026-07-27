# Type Alias: JsonValue

&gt; **JsonValue** = [`JsonPrimitive`](./JsonPrimitive) \| [`JsonArray`](./JsonArray) \| [`JsonObject`](../interfaces/JsonObject)

Defined in: [json.ts:61](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/json.ts#L61)

Any valid JSON value: a primitive, an array, or an object. This is the closed
set that survives a `JSON.parse(JSON.stringify(x))` round-trip — it excludes
`undefined`, functions, `symbol`, `bigint`, and class instances, none of which
JSON can represent. Use it in place of `any` for anything that must serialize.
