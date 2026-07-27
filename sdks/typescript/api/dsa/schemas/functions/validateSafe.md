# Function: validateSafe()

&gt; **validateSafe**\<`T`\>(`schema`, `input`): `ValidationResult`\<`T`\[`"Type"`\]\>

Defined in: [schemas.ts:199](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/schemas.ts#L199)

Decode `input` against `schema` and return a discriminated result
instead of throwing. Mirrors the `Result<T, E>` shape used
elsewhere in `@resq-systems/helpers`.

## Type Parameters

### T

`T` *extends* `AnySchema`

## Parameters

### schema

`T`

### input

`unknown`

## Returns

`ValidationResult`\<`T`\[`"Type"`\]\>

`{ success: true, data }` on success; `{ success: false,
  error &#125;` (with the parse-error message) on failure.

## Example

```ts
const r = validateSafe(GraphEdgeSchema, body);
if (!r.success) return new Response(r.error, { status: 400 });
graph.addEdge(r.data.source, r.data.target, r.data.weight);
```
