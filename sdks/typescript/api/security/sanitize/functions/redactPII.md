# Function: redactPII()

&gt; **redactPII**(`text`, `options?`): `string`

Defined in: [sanitize.ts:735](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L735)

Redacts common PII patterns in a string for safe logging.
Detects and masks SSNs, credit cards, emails, phone numbers, etc.

## Parameters

### text

`string`

The text to redact PII from. Non-string input yields `""`.

### options?

`object` & `object` = `{}`

Configuration options for redaction, plus optional
  `customPatterns` applied after the built-ins. Each `pattern` **must** be a
  global (`/g`) RegExp.

## Returns

`string`

The text with PII patterns replaced with redaction markers, or `""`
  for non-string input. If the built-in options fail schema validation the
  original `text` is returned unredacted rather than throwing.

## Throws

If any `customPatterns` entry uses a non-global RegExp —
  `String.prototype.replaceAll` rejects non-global patterns.

## Compliance

NIST 800-53 AU-3 (Content of Audit Records)

## Example

```typescript
redactPII('Contact john@example.com or call 555-123-4567');
// 'Contact [EMAIL] or call [PHONE]'

redactPII('SSN: 123-45-6789');
// 'SSN: [SSN]'
```
