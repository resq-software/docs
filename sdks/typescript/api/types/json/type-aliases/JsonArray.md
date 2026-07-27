# Type Alias: JsonArray

&gt; **JsonArray** = [`JsonValue`](./JsonValue)[]

Defined in: [json.ts:39](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/json.ts#L39)

A JSON array holding any valid JSON values. Elements are always present (no
holes); a sparse slot serializes as `null`, so treat the type as dense.
