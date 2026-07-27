# Function: sanitizeUrl()

&gt; **sanitizeUrl**(`url`, `allowedProtocols?`): `string`

Defined in: [sanitize.ts:297](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L297)

Validates and sanitizes a user-supplied URL, ensuring it conforms to allowed protocols
and is not a vector for injection attacks like `javascript:` or `data:`.

## Parameters

### url

`string`

The URL to be validated and sanitized.

### allowedProtocols?

readonly (`"http:"` \| `"https:"` \| `"mailto:"` \| `"tel:"` \| `"ftp:"`)[] = `...`

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
