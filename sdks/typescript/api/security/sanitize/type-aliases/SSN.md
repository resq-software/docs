# Type Alias: SSN

&gt; **SSN** = `Brand`\<`string`, `"SSN"`\>

Defined in: [sanitize.ts:167](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L167)

A US Social Security Number matching [SSNSchema](../variables/SSNSchema). Mint one by
narrowing through the [isValidSSN](../functions/isValidSSN) type guard. The brand asserts
the `NNN-NN-NNNN` shape only — it does not validate area/group ranges or
confirm the number was ever issued. Treat any value as sensitive PII.
