# Function: safeStringify()

> **safeStringify**(`obj`, `sensitiveKeys?`, `indent?`): `string`

Defined in: [sanitize.ts:590](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/security/src/sanitize.ts#L590)

Creates a safe string representation of an object for logging,
automatically redacting sensitive fields.

## Parameters

### obj

`unknown`

The object to stringify.

### sensitiveKeys?

`string`[] = `...`

Array of key names to redact.

### indent?

`number` = `2`

JSON indentation (default: 2).

## Returns

`string`

A JSON string with sensitive values redacted.

## Compliance

NIST 800-53 AU-3 (Content of Audit Records)

## Example

```typescript
safeStringify({ user: 'john', password: 'secret123' }, ['password']);
// '{\n  "user": "john",\n  "password": "[REDACTED]"\n}'
```
