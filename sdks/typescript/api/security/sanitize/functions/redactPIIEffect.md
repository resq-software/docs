# Function: redactPIIEffect()

&gt; **redactPIIEffect**(`text`, `options?`): `Exit`\<`string`, `SchemaError`\>

Defined in: [sanitize.ts:661](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L661)

Redacts PII from text using Effect Schema validated options.

Total — never throws. Failure to decode `options` is returned as a resolved
Exit.Exit failure carrying the S.SchemaError. By default
dates are **not** redacted (`redactDates` defaults to `false`); every other
category defaults to `true`.

## Parameters

### text

`string`

The text to redact PII from.

### options?

Configuration options for redaction.

#### redactCreditCards?

`boolean` = `...`

#### redactDates?

`boolean` = `...`

#### redactEmails?

`boolean` = `...`

#### redactIPs?

`boolean` = `...`

#### redactPhones?

`boolean` = `...`

#### redactSSN?

`boolean` = `...`

## Returns

`Exit`\<`string`, `SchemaError`\>

An Exit.Exit: success carries the redacted text, failure
  carries a S.SchemaError from invalid `options`.

## Compliance

NIST 800-53 AU-3 (Content of Audit Records)
