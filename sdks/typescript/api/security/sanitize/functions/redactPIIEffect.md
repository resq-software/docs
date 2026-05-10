# Function: redactPIIEffect()

> **redactPIIEffect**(`text`, `options?`): `Exit`\<`string`, `unknown`\>

Defined in: [sanitize.ts:465](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/security/src/sanitize.ts#L465)

Redacts PII from text using Effect Schema validated options.

## Parameters

### text

`string`

The text to redact PII from.

### options?

Configuration options for redaction.

#### redactCreditCards?

`boolean`

#### redactDates?

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

`Exit`\<`string`, `unknown`\>

Exit containing redacted text or error.

## Compliance

NIST 800-53 AU-3 (Content of Audit Records)
