# Function: sanitizeUrl()

> **sanitizeUrl**(`url`, `allowedProtocols?`): `string`

Defined in: [sanitize.ts:235](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/security/src/sanitize.ts#L235)

Validates and sanitizes a user-supplied URL, ensuring it conforms to allowed protocols
and is not a vector for injection attacks like `javascript:` or `data:`.

## Parameters

### url

`string`

The URL to be validated and sanitized.

### allowedProtocols?

readonly `string`[] = `...`

Array of allowed URL protocols.

## Returns

`string`

The sanitized URL if valid, or an empty string if unsafe.

## Compliance

NIST 800-53 SI-10 (Information Input Validation)

## Example

```typescript
sanitizeUrl('https://example.com'); // 'https://example.com'
sanitizeUrl('javascript:alert(1)'); // ''
```
