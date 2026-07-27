# Type Alias: JsonArray

&gt; **JsonArray** = [`JsonValue`](./JsonValue)[]

Defined in: [json.ts:39](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/json.ts#L39)

A JSON array holding any valid JSON values. Elements are always present (no
holes); a sparse slot serializes as `null`, so treat the type as dense.
