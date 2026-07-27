# Interface: SendEmailOptions

Defined in: [packages/email-templates/src/send/send-email.ts:30](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/send-email.ts#L30)

Delivery options for [sendEmail](../functions/sendEmail) — everything the render step can't supply.

## Properties

### from

&gt; **from**: `string`

Defined in: [packages/email-templates/src/send/send-email.ts:32](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/send-email.ts#L32)

Verified sender address, e.g. "ResQ Systems &lt;updates@send.resq.software&gt;".

***

### headers?

&gt; `optional` **headers?**: `Record`\<`string`, `string`\>

Defined in: [packages/email-templates/src/send/send-email.ts:38](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/send-email.ts#L38)

Extra headers passed through to the sender.

***

### idempotencyKey?

&gt; `optional` **idempotencyKey?**: `string`

Defined in: [packages/email-templates/src/send/send-email.ts:36](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/send-email.ts#L36)

Stable key so Resend de-dupes identical sends for 24h.

***

### replyTo?

&gt; `optional` **replyTo?**: `string` \| `string`[]

Defined in: [packages/email-templates/src/send/send-email.ts:34](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/send-email.ts#L34)

Reply-To address(es); absent means the provider default applies.
