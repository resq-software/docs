# Type Alias: PhoneNumber

&gt; **PhoneNumber** = `Brand`\<`string`, `"PhoneNumber"`\>

Defined in: [sanitize.ts:154](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L154)

A US-format phone number matching [PhoneNumberSchema](../variables/PhoneNumberSchema). Mint one by
narrowing through the [isValidPhone](../functions/isValidPhone) type guard. The brand asserts
the digit/separator shape only; it neither normalizes formatting nor
confirms the number is assigned.
