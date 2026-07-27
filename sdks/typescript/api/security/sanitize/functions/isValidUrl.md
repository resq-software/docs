# Function: isValidUrl()

&gt; **isValidUrl**(`url`): `url is Brand<string, "SafeUrl">`

Defined in: [sanitize.ts:875](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L875)

Validates if a string is a safe URL using Effect Schema.

Narrows the input to [SafeUrl](../type-aliases/SafeUrl) on success.

## Parameters

### url

`string`

The string to validate.

## Returns

`url is Brand<string, "SafeUrl">`

true if valid and safe URL, false otherwise.
