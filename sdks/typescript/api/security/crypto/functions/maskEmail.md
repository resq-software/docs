# Function: maskEmail()

> **maskEmail**(`email`): `string`

Defined in: [crypto.ts:221](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/crypto.ts#L221)

Mask an email address while preserving the domain — useful for
deduplication and support workflows where the domain is non-PII but
the local part identifies the user.

## Parameters

### email

`string`

Full email. Falls back to [maskPII](./maskPII) if the input
  does not contain a valid `local@domain` shape.

## Returns

`string`

Masked email; e.g. `"j*****e@example.com"`.

## Example

```ts
maskEmail("jane@example.com"); // → "j**e@example.com"
maskEmail("ab@example.com");   // → "**@example.com"
maskEmail("not-an-email");     // → "no********il" (maskPII fallback)
```
