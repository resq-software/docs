# Function: validateSafeText()

&gt; **validateSafeText**(`input`): `boolean`

Defined in: [validators.ts:594](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L594)

Boolean refinement helper for use with `zod.string().refine(...)`,
`effect/Schema.filter(...)`, or any predicate-based validator.

Equivalent to `isSafeInput(input)` with default config.

## Parameters

### input

`string`

## Returns

`boolean`
