# Function: sanitizeForLogging()

> **sanitizeForLogging**\<`T`\>(`obj`, `sensitiveFields?`): `Partial`\<`T`\>

Defined in: [crypto.ts:264](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/crypto.ts#L264)

Recursively shallow-copy an object, replacing any field whose key
contains a sensitive substring (case-insensitive) with `[REDACTED]`,
and masking string fields whose key contains `"email"` via
[maskEmail](./maskEmail).

Designed for log structures — preserves shape so log queries continue
to work, but ensures secrets and identifiers don't leak. Use as a
defensive layer **before** writing structured log lines.

## Type Parameters

### T

`T` *extends* `Record`\<`string`, `unknown`\>

## Parameters

### obj

`T`

Object to sanitize. Original is not mutated.

### sensitiveFields?

`string`[] = `...`

Substring allow-list. Defaults to
  `["password", "passwordHash", "token", "secret",
  "twoFactorSecret", "apiKey"]`. Substrings match anywhere in the
  key, e.g. `"token"` matches `"refreshToken"` and `"id_token"`.

## Returns

`Partial`\<`T`\>

A new object with sensitive fields redacted and emails
  masked. Nested objects are recursed; arrays and primitives pass
  through unchanged.

## Example

```ts
sanitizeForLogging({
  id: 1,
  email: "u@x.com",
  apiKey: "sk-...",
  nested: { token: "..." },
});
// → { id: 1, email: "u@x.com" (masked), apiKey: "[REDACTED]", nested: { token: "[REDACTED]" } }
```
