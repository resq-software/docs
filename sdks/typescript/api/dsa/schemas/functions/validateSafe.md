# Function: validateSafe()

> **validateSafe**\<`T`\>(`schema`, `input`): `ValidationResult`\<`Type`\<`T`\>\>

Defined in: [schemas.ts:187](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/schemas.ts#L187)

Decode `input` against `schema` and return a discriminated result
instead of throwing. Mirrors the `Result<T, E>` shape used
elsewhere in `@resq-sw/helpers`.

## Type Parameters

### T

`T` *extends* `AnySchema`

## Parameters

### schema

`T`

### input

`unknown`

## Returns

`ValidationResult`\<`Type`\<`T`\>\>

`{ success: true, data }` on success; `{ success: false,
  error &#125;` (with the parse-error message) on failure.

## Example

```ts
const r = validateSafe(GraphEdgeSchema, body);
if (!r.success) return new Response(r.error, { status: 400 });
graph.addEdge(r.data.source, r.data.target, r.data.weight);
```
