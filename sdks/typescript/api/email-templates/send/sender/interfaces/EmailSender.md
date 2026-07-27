# Interface: EmailSender

Defined in: [packages/email-templates/src/send/sender.ts:67](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L67)

Port for an email transport. Implement this to plug in any provider (Resend,
SES, Postmark, SMTP); the rest of the package depends only on this interface.

## Methods

### send()

&gt; **send**(`input`): `Promise`\<[`SendResult`](../type-aliases/SendResult)\>

Defined in: [packages/email-templates/src/send/sender.ts:74](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L74)

Send one email. Implementations SHOULD normalize transport/API failures into
a `{ ok: false, error }` result rather than throwing (the bundled Resend
adapter does). `sendEmail` still guards against a throwing sender, but
honoring this contract keeps the failure `name`/`message` provider-accurate.

#### Parameters

##### input

[`SendEmailInput`](./SendEmailInput)

#### Returns

`Promise`\<[`SendResult`](../type-aliases/SendResult)\>
