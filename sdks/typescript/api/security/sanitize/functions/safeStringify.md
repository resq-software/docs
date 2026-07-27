# Function: safeStringify()

&gt; **safeStringify**(`obj`, `sensitiveKeys?`, `indent?`): `string`

Defined in: [sanitize.ts:796](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L796)

Creates a safe string representation of an object for logging,
automatically redacting sensitive fields.

Never throws: any serialization failure — a circular reference, a `BigInt`
value, a throwing `toJSON` — is caught and returned as the sentinel string
`"[Unable to stringify object]"`. Key matching is case-insensitive and
compares the full key name (not substrings), so `apiKey` matches only the
literal `"apiKey"`, not `"apiKeyId"`.

## Parameters

### obj

`unknown`

The object to stringify.

### sensitiveKeys?

`string`[] = `...`

Key names to redact, compared case-insensitively.

### indent?

`number` = `2`

JSON indentation (default: 2).

## Returns

`string`

A JSON string with sensitive values redacted, or the sentinel
  `"[Unable to stringify object]"` when serialization fails.

## Compliance

NIST 800-53 AU-3 (Content of Audit Records)

## Example

```typescript
safeStringify({ user: 'john', password: 'secret123' }, ['password']);
// '{\n  "user": "john",\n  "password": "[REDACTED]"\n}'
```
