# Function: sanitizeForLogging()

&gt; **sanitizeForLogging**(`obj`, `sensitiveFields?`): `Record`\<`string`, `unknown`\>

Defined in: [crypto.ts:370](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/crypto.ts#L370)

Recursively shallow-copy an object, replacing any field whose key
contains a sensitive substring (case-insensitive) with `[REDACTED]`,
and masking string fields whose key contains `"email"` via
[maskEmail](./maskEmail).

Designed for log structures — preserves shape so log queries continue
to work, but ensures secrets and identifiers don't leak. Use as a
defensive layer **before** writing structured log lines.

## Parameters

### obj

`Record`\<`string`, `unknown`\>

Object to sanitize. Original is not mutated.

### sensitiveFields?

`string`[] = `...`

Substring allow-list. Defaults to
  `["password", "passwordHash", "token", "secret",
  "twoFactorSecret", "apiKey"]`. Substrings match anywhere in the
  key, e.g. `"token"` matches `"refreshToken"` and `"id_token"`.

## Returns

`Record`\<`string`, `unknown`\>

A new object with sensitive fields redacted and emails
  masked. Any non-null object value is recursed and comes back as a
  plain object keyed by its enumerable own properties — so arrays
  return as index-keyed objects (`["a"]` → `{ "0": "a" }`) and class
  instances / `Date`s lose their prototype. Only primitives, `null`,
  and `undefined` pass through unchanged.

## Throws

On a circular reference — recursion has no cycle
  guard, so a self-referential object overflows the call stack.

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
