# Function: createValidator()

> **createValidator**\<`T`\>(`schema`): (`input`) => `Type`\<`T`\>

Defined in: [schemas.ts:211](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/schemas.ts#L211)

Build a reusable, throwing decoder bound to one schema. Equivalent
to currying [validate](./validate).

## Type Parameters

### T

`T` *extends* `AnySchema`

## Parameters

### schema

`T`

## Returns

(`input`) => `Type`\<`T`\>

## Example

```ts
const parseEdge = createValidator(GraphEdgeSchema);
const edge = parseEdge(rawJson);
```
