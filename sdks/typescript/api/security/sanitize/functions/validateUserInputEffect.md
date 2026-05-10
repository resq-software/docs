# Function: validateUserInputEffect()

> **validateUserInputEffect**(`input`, `options?`): `Exit`\<`string`, `unknown`\>

Defined in: [sanitize.ts:251](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/security/src/sanitize.ts#L251)

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
