# Function: escapeHtml()

> **escapeHtml**(`text`): `string`

Defined in: [sanitize.ts:157](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/sanitize.ts#L157)

Escapes special HTML characters in a string to their corresponding HTML entities,
preventing direct injection of HTML and JavaScript when rendering untrusted content.

## Parameters

### text

`string`

The plain text to escape.

## Returns

`string`

The escaped string safe for HTML rendering.

## Compliance

NIST 800-53 SI-10 (Information Input Validation)

## Example

```typescript
escapeHtml('<script>alert("xss")</script>');
// "&lt;script&gt;alert(&quot;xss&quot;)&lt;/script&gt;"
```
