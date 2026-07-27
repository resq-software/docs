# Function: escapeHtml()

&gt; **escapeHtml**(`text`): `string`

Defined in: [sanitize.ts:214](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L214)

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
