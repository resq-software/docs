# Function: validateSafeName()

> **validateSafeName**(`input`): `boolean`

Defined in: [validators.ts:600](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L600)

Refinement for human name fields. More permissive than
[validateSafeText](./validateSafeText) — allows international letters,
combining marks, hyphens, apostrophes, and spaces — but still
rejects HTML/SQL/NoSQL injection patterns and homoglyph forgeries.

Suitable for first/last/full-name inputs in registration forms.

## Parameters

### input

`string`

## Returns

`boolean`

`true` when the name passes both the threat detectors and
  the name-shape regex.
