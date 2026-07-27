# Function: sanitizeUrlEffect()

&gt; **sanitizeUrlEffect**(`url`, `allowedProtocols?`): `Exit`\<`string`, `SchemaError`\>

Defined in: [sanitize.ts:250](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L250)

Validates and sanitizes a user-supplied URL using Effect Schema.
Returns an Exit with the sanitized URL or an error.

Pure and total — failure is encoded as a resolved Exit.Exit failure
(an `Exit.fail` carrying a S.SchemaError), never a thrown exception.

## Parameters

### url

`string`

The URL to be validated and sanitized.

### allowedProtocols?

readonly (`"http:"` \| `"https:"` \| `"mailto:"` \| `"tel:"` \| `"ftp:"`)[] = `...`

Allowed URL protocols; a root-relative path
  (`/foo`, not `//foo`) is always accepted regardless of this list.

## Returns

`Exit`\<`string`, `SchemaError`\>

An Exit.Exit: success carries the accepted URL string,
  failure carries a S.SchemaError.

## Compliance

NIST 800-53 SI-10 (Information Input Validation)

## Example

```typescript
const result = sanitizeUrlEffect('https://example.com');
// Exit.succeed('https://example.com')

const invalid = sanitizeUrlEffect('javascript:alert(1)');
// Exit.fail(...)
```
