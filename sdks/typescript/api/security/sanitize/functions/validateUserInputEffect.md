# Function: validateUserInputEffect()

&gt; **validateUserInputEffect**(`input`, `options?`): `Exit`\<`string`, `SchemaError`\>

Defined in: [sanitize.ts:393](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L393)

Validates user input using Effect Schema and returns an Exit.

Strips HTML (unless `allowHtml`), collapses whitespace, and repeatedly
removes dangerous URI schemes and inline handlers until the string
stabilizes — the fixed-point loop defeats nested-payload bypasses such as
`javascrjavascript:ipt:`. Failure is a resolved Exit.Exit failure,
never a throw; the only failure path is a non-string reaching `S.String`.

## Parameters

### input

`string`

User input to validate and sanitize.

### options?

Validation options. Defaults: `maxLength` 500, `allowHtml`
  false, `allowNewlines` false, `trimWhitespace` true.

#### allowHtml?

`boolean` = `...`

#### allowNewlines?

`boolean` = `...`

#### maxLength?

`number` = `...`

#### trimWhitespace?

`boolean` = `...`

## Returns

`Exit`\<`string`, `SchemaError`\>

An Exit.Exit: success carries the sanitized string truncated
  to `maxLength`; failure carries a S.SchemaError.

## Compliance

NIST 800-53 SI-10 (Information Input Validation)
