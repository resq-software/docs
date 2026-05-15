# Function: validateSafeEmail()

> **validateSafeEmail**(`input`): `boolean`

Defined in: [validators.ts:626](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L626)

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
