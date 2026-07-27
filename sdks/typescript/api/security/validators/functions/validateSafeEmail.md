# Function: validateSafeEmail()

&gt; **validateSafeEmail**(`input`): `boolean`

Defined in: [validators.ts:635](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L635)

Refinement for email fields. Combines:

1. RFC-style format check (length-bounded to ≤ 254 chars to
   prevent ReDoS).
2. XSS / SQL / NoSQL / homoglyph detectors — emails are extremely
   constrained and should never legitimately contain HTML or query
   operators.

## Parameters

### input

`string`

## Returns

`boolean`

`true` when both checks pass.
