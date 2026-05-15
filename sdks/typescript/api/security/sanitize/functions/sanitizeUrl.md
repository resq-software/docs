# Function: sanitizeUrl()

> **sanitizeUrl**(`url`, `allowedProtocols?`): `string`

Defined in: [sanitize.ts:235](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/sanitize.ts#L235)

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
