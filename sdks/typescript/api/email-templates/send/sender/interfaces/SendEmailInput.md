# Interface: SendEmailInput

Defined in: [packages/email-templates/src/send/sender.ts:31](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L31)

Provider-agnostic input for sending a single email.

At least one of [SendEmailInput.html](#html) or [SendEmailInput.text](#text) should
be present, or the message has no body — the pipeline (`renderEmail`) always
supplies both. `to`, `cc`, and `bcc` accept one address or a list.

## Properties

### bcc?

&gt; `optional` **bcc?**: `string` \| `string`[]

Defined in: [packages/email-templates/src/send/sender.ts:43](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L43)

***

### cc?

&gt; `optional` **cc?**: `string` \| `string`[]

Defined in: [packages/email-templates/src/send/sender.ts:42](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L42)

***

### from

&gt; **from**: `string`

Defined in: [packages/email-templates/src/send/sender.ts:33](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L33)

Verified sender address, e.g. "ResQ Systems &lt;ops@send.resq.software&gt;".

***

### headers?

&gt; `optional` **headers?**: `Record`\<`string`, `string`\>

Defined in: [packages/email-templates/src/send/sender.ts:47](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L47)

Extra headers, e.g. RFC 8058 `List-Unsubscribe` for marketing mail.

***

### html?

&gt; `optional` **html?**: `string`

Defined in: [packages/email-templates/src/send/sender.ts:38](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L38)

HTML body; omit only if `text` is provided.

***

### idempotencyKey?

&gt; `optional` **idempotencyKey?**: `string`

Defined in: [packages/email-templates/src/send/sender.ts:45](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L45)

Stable key so Resend de-dupes identical sends for 24h.

***

### replyTo?

&gt; `optional` **replyTo?**: `string` \| `string`[]

Defined in: [packages/email-templates/src/send/sender.ts:41](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L41)

***

### subject

&gt; **subject**: `string`

Defined in: [packages/email-templates/src/send/sender.ts:36](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L36)

***

### text?

&gt; `optional` **text?**: `string`

Defined in: [packages/email-templates/src/send/sender.ts:40](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L40)

Plain-text body; omit only if `html` is provided.

***

### to

&gt; **to**: `string` \| `string`[]

Defined in: [packages/email-templates/src/send/sender.ts:35](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L35)

Primary recipient(s); at least one address.
