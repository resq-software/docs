# Function: isValidPhone()

&gt; **isValidPhone**(`phone`): `phone is Brand<string, "PhoneNumber">`

Defined in: [sanitize.ts:851](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L851)

Validates if a string is a valid phone number using Effect Schema.

Narrows the input to [PhoneNumber](../type-aliases/PhoneNumber) on success.

## Parameters

### phone

`string`

The string to validate.

## Returns

`phone is Brand<string, "PhoneNumber">`

true if valid phone number, false otherwise.
