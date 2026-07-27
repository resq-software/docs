# Function: isValidEmail()

&gt; **isValidEmail**(`email`): `email is Brand<string, "Email">`

Defined in: [sanitize.ts:839](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L839)

Validates if a string is a valid email address using Effect Schema.

Narrows the input to [Email](../type-aliases/Email) on success, so validated call sites
carry the brand into downstream code.

## Parameters

### email

`string`

The string to validate.

## Returns

`email is Brand<string, "Email">`

true if valid email, false otherwise.
