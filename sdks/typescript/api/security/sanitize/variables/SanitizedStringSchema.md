# Variable: SanitizedStringSchema

&gt; `const` **SanitizedStringSchema**: `String` = `S.String`

Defined in: [sanitize.ts:112](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L112)

Schema for a sanitized HTML-safe string — validates the value is a string; the
actual escaping is applied at runtime by the sanitization helpers.

## Compliance

NIST 800-53 SI-10 (Information Input Validation)
