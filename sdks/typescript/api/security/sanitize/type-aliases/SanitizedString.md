# Type Alias: SanitizedString

&gt; **SanitizedString** = *typeof* `SanitizedStringSchema.Type`

Defined in: [sanitize.ts:120](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L120)

A string carrying the [SanitizedStringSchema](../variables/SanitizedStringSchema) contract. The schema is
`S.String` alone, so decoding asserts only that the value is a string —
the actual escaping is applied separately by the sanitization helpers
(e.g. [escapeHtml](../functions/escapeHtml)). The type name signals intent, not a proof of
escaping.
