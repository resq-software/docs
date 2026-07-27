# Type Alias: CreditCard

&gt; **CreditCard** = `Brand`\<`string`, `"CreditCard"`\>

Defined in: [sanitize.ts:183](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L183)

A card number matching the [CreditCardSchema](../variables/CreditCardSchema) pattern (13–16 digits
with optional group separators). No exported type guard mints this brand;
decode [CreditCardSchema](../variables/CreditCardSchema) directly at the boundary. The pattern is a
shape check only — it performs **no** Luhn checksum and does not identify
the issuer. Treat any value as sensitive PII.
