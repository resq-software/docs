# Variable: THREAT\_DETECTED\_MESSAGE

&gt; `const` **THREAT\_DETECTED\_MESSAGE**: `"Input contains potentially unsafe content"` = `"Input contains potentially unsafe content"`

Defined in: [validators.ts:586](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L586)

Generic user-facing fallback message. Render this verbatim when a
detector fires but you don't want to expose which one. Prefer
[getThreatErrorMessage](../functions/getThreatErrorMessage) for category-specific messages.
