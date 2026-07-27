# Interface: JsonObject

Defined in: [json.ts:51](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/json.ts#L51)

A JSON object keyed by strings, with JSON values.

The `| undefined` in the value type models keys that may be **absent** from
the serialized form: `JSON.stringify` drops a property whose value is
`undefined` entirely rather than emitting `"key": undefined`. So a member
typed `undefined` means "may be omitted", not "serializes to a literal
undefined" — round-tripping such a key through `stringify`/`parse` yields an
object without it.

## Indexable

&gt; \[`key`: `string`\]: [`JsonValue`](../type-aliases/JsonValue) \| `undefined`
