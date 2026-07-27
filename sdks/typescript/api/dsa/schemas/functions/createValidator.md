# Function: createValidator()

&gt; **createValidator**\<`T`\>(`schema`): (`input`) =&gt; `T`\[`"Type"`\]

Defined in: [schemas.ts:228](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/schemas.ts#L228)

Build a reusable, throwing decoder bound to one schema. Equivalent
to currying [validate](./validate).

The returned function decodes its input synchronously and **throws** the
Effect parse error on invalid input, exactly like [validate](./validate). Reach for
[validateSafe](./validateSafe) when you want a non-throwing result instead.

## Type Parameters

### T

`T` *extends* `AnySchema`

## Parameters

### schema

`T`

## Returns

A decoder that maps trusted input to `T["Type"]`, throwing on a
  parse failure.

(`input`) =&gt; `T`\[`"Type"`\]

## Example

```ts
const parseEdge = createValidator(GraphEdgeSchema);
const edge = parseEdge(rawJson);
```
