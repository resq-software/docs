# Function: isValidSSN()

&gt; **isValidSSN**(`ssn`): `ssn is Brand<string, "SSN">`

Defined in: [sanitize.ts:863](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L863)

Validates if a string is a valid SSN using Effect Schema.

Narrows the input to [SSN](../type-aliases/SSN) on success.

## Parameters

### ssn

`string`

The string to validate.

## Returns

`ssn is Brand<string, "SSN">`

true if valid SSN, false otherwise.
