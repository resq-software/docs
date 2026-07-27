# Variable: PIIRedactionOptionsSchema

&gt; `const` **PIIRedactionOptionsSchema**: `Struct`\<\{ `redactCreditCards`: `optional`\<`Boolean`\>; `redactDates`: `optional`\<`Boolean`\>; `redactEmails`: `optional`\<`Boolean`\>; `redactIPs`: `optional`\<`Boolean`\>; `redactPhones`: `optional`\<`Boolean`\>; `redactSSN`: `optional`\<`Boolean`\>; \}\>

Defined in: [sanitize.ts:54](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L54)

Schema for the per-category toggles that drive [redactPII](../functions/redactPII).

## Compliance

NIST 800-53 AU-3 (Content of Audit Records)
