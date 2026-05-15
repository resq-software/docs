# Function: validate()

> **validate**\<`T`\>(`schema`, `input`): `Type`\<`T`\>

Defined in: [schemas.ts:163](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/schemas.ts#L163)

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

`Type`\<`T`\>

## Throws

The Effect parse error from `decodeUnknownSync`.
