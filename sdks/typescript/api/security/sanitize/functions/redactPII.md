# Function: redactPII()

> **redactPII**(`text`, `options?`): `string`

Defined in: [sanitize.ts:533](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/sanitize.ts#L533)

Redacts common PII patterns in a string for safe logging.
Detects and masks SSNs, credit cards, emails, phone numbers, etc.

## Parameters

### text

`string`

The text to redact PII from.

### options?

Configuration options for redaction.

#### customPatterns?

`object`[]

#### redactCreditCards?

`boolean`

#### redactEmails?

`boolean`

#### redactIPs?

`boolean`

#### redactPhones?

`boolean`

#### redactSSN?

`boolean`

## Returns

`string`

The text with PII patterns replaced with redaction markers.

## Compliance

NIST 800-53 AU-3 (Content of Audit Records)

## Example

```typescript
redactPII('Contact john@example.com or call 555-123-4567');
// 'Contact [EMAIL] or call [PHONE]'

redactPII('SSN: 123-45-6789');
// 'SSN: [SSN]'
```
