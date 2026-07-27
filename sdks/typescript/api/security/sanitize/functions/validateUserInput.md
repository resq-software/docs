# Function: validateUserInput()

&gt; **validateUserInput**(`input`, `maxLength?`, `allowHtml?`): `string`

Defined in: [sanitize.ts:459](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L459)

Validates and sanitizes generic user input by trimming, removing HTML tags (unless allowed),
normalizing whitespace, and removing dangerous patterns to prevent XSS and basic injection flaws.

## Parameters

### input

`string`

User input to validate and sanitize.

### maxLength?

`number` = `500`

Maximum allowed input length. Excess will be truncated.

### allowHtml?

`boolean` = `false`

If true, HTML tags are preserved; otherwise, all tags are stripped.

## Returns

`string`

Sanitized input string with length at most `maxLength`.

## Compliance

NIST 800-53 SI-10 (Information Input Validation)

## Example

```typescript
validateUserInput('<p>Hello!</p>', 50); // "Hello!"
validateUserInput('<script>alert(1)</script>test', 100); // "test"
```
