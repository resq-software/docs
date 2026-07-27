# Function: validateSafeName()

&gt; **validateSafeName**(`input`): `boolean`

Defined in: [validators.ts:609](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L609)

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
