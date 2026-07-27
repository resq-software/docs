# Type Alias: Email

&gt; **Email** = `Brand`\<`string`, `"Email"`\>

Defined in: [sanitize.ts:139](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L139)

An email address that matches [EmailSchema](../variables/EmailSchema). Mint one by narrowing
through the [isValidEmail](../functions/isValidEmail) type guard. The brand guarantees only
syntactic well-formedness (including IDN/Punycode TLDs) — not that the
mailbox exists or is deliverable.
