# Type Alias: IPv4

&gt; **IPv4** = `Brand`\<`string`, `"IPv4"`\>

Defined in: [sanitize.ts:195](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L195)

A dotted-quad string matching [IPv4Schema](../variables/IPv4Schema). No exported type guard
mints this brand; decode [IPv4Schema](../variables/IPv4Schema) directly. The pattern checks
four dot-separated groups of 1–3 digits only — it does **not** bound each
octet to `0–255`, so `999.0.0.1` still matches.
