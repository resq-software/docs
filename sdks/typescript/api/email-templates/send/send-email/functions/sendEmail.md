# Function: sendEmail()

&gt; **sendEmail**(`sender`, `payload`, `options`): `Promise`\<[`SendResult`](../../sender/type-aliases/SendResult)\>

Defined in: [packages/email-templates/src/send/send-email.ts:64](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/send-email.ts#L64)

Render a validated payload and hand it to a sender in one call. Convenience
wiring for the common pipeline case: `sendEmail(sender, payload, { from })`.

Never throws or rejects: every failure — an invalid payload, a render error, or
a throwing/failing sender — is normalized into a `{ ok: false, error }`
[SendResult](../../sender/type-aliases/SendResult). Distinguish failures by `error.name`: `"EmailValidationError"`
(payload failed schema validation), `"render_error"` (any other render failure),
`"sender_error"` (the sender threw instead of returning a result), or whatever
`name` the sender itself reports on a normal `{ ok: false }` return. The
`idempotencyKey` is passed through to the sender and only takes effect insofar
as the sender honours it.

## Parameters

### sender

[`EmailSender`](../../sender/interfaces/EmailSender)

The transport port that performs delivery.

### payload

`unknown`

Untrusted `{ name, to, data }` payload to validate and render.

### options

[`SendEmailOptions`](../interfaces/SendEmailOptions)

Delivery options; `from` is required.

## Returns

`Promise`\<[`SendResult`](../../sender/type-aliases/SendResult)\>

A promise resolving to the send outcome — never a rejection.

## Example

```ts
const result = await sendEmail(sender, badPayload, { from: "ResQ <ops@resq.software>" });
result.ok; // → false
```
