# Function: validate()

&gt; **validate**\<`T`\>(`schema`, `input`): `T`\[`"Type"`\]

Defined in: [schemas.ts:176](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/schemas.ts#L176)

Decode `input` against `schema` synchronously, throwing on failure.

Use when the input is already trusted and you'd rather propagate
the error than handle it locally — typically inside a wrapping
try/catch or further up the call stack. For caller-friendly
handling use [validateSafe](./validateSafe) instead.

## Type Parameters

### T

`T` *extends* `AnySchema`

## Parameters

### schema

`T`

### input

`unknown`

## Returns

`T`\[`"Type"`\]

## Throws

The Effect parse error from `decodeUnknownSync`.
