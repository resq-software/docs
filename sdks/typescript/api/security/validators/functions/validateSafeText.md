# Function: validateSafeText()

> **validateSafeText**(`input`): `boolean`

Defined in: [validators.ts:585](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L585)

Boolean refinement helper for use with `zod.string().refine(...)`,
`effect/Schema.filter(...)`, or any predicate-based validator.

Equivalent to `isSafeInput(input)` with default config.

## Parameters

### input

`string`

## Returns

`boolean`
