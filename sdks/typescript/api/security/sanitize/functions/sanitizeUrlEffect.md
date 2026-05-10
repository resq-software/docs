# Function: sanitizeUrlEffect()

> **sanitizeUrlEffect**(`url`, `allowedProtocols?`): `Exit`\<`string`, `unknown`\>

Defined in: [sanitize.ts:188](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/security/src/sanitize.ts#L188)

Validates and sanitizes a user-supplied URL using Effect Schema.
Returns an Exit with the sanitized URL or an error.

## Parameters

### url

`string`

The URL to be validated and sanitized.

### allowedProtocols?

readonly `string`[] = `...`

Array of allowed URL protocols.

## Returns

`Exit`\<`string`, `unknown`\>

Exit containing the sanitized URL or an error.

## Compliance

NIST 800-53 SI-10 (Information Input Validation)

## Example

```typescript
const result = sanitizeUrlEffect('https://example.com');
// Exit.succeed('https://example.com')

const invalid = sanitizeUrlEffect('javascript:alert(1)');
// Exit.fail(...)
```
