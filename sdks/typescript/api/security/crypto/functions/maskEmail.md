# Function: maskEmail()

&gt; **maskEmail**(`email`): `Brand`

Defined in: [crypto.ts:321](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/crypto.ts#L321)

Mask an email address while preserving the domain — useful for
deduplication and support workflows where the domain is non-PII but
the local part identifies the user.

## Parameters

### email

`string`

Full email. Falls back to [maskPII](./maskPII) if the input
  does not contain a valid `local@domain` shape.

## Returns

`Brand`

Masked email; e.g. `"j*****e@example.com"`.

## Example

```ts
maskEmail("jane@example.com"); // → "j**e@example.com"
maskEmail("ab@example.com");   // → "**@example.com"
maskEmail("not-an-email");     // → "no********il" (maskPII fallback)
```
