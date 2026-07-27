# Type Alias: EmailPayload

&gt; **EmailPayload** = `ReturnType`\<*typeof* `resqMailer.decode`\>

Defined in: [packages/email-templates/src/contract.ts:30](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/contract.ts#L30)

The validated payload type for the built-in ResQ Systems templates — the
discriminated `{ name, to, data, category?, unsubscribeUrl? }` union, keyed by
[EmailName](./EmailName). Narrow on `name` to recover the matching `data` shape.
