# Type Alias: SafeUrl

&gt; **SafeUrl** = `Brand`\<`string`, `"SafeUrl"`\>

Defined in: [sanitize.ts:105](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L105)

A URL string vouched safe against scheme-based injection. Mint one by
narrowing through the [isValidUrl](../functions/isValidUrl) type guard (backed by
[SafeUrlSchema](../variables/SafeUrlSchema)); the brand guarantees the value is either a
root-relative path or an absolute URL restricted to `http:`/`https:`/
`mailto:`. It does **not** guarantee the host is reachable or trusted.
