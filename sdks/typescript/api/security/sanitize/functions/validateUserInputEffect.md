# Function: validateUserInputEffect()

> **validateUserInputEffect**(`input`, `options?`): `Exit`\<`string`, `unknown`\>

Defined in: [sanitize.ts:251](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/sanitize.ts#L251)

Validates user input using Effect Schema and returns an Exit.

## Parameters

### input

`string`

User input to validate and sanitize.

### options?

Validation options.

#### allowHtml?

`boolean`

#### allowNewlines?

`boolean`

#### maxLength?

`number`

#### trimWhitespace?

`boolean`

## Returns

`Exit`\<`string`, `unknown`\>

Exit containing sanitized input or error.

## Compliance

NIST 800-53 SI-10 (Information Input Validation)
