# Function: createResendSender()

&gt; **createResendSender**(`apiKey?`): [`EmailSender`](../../sender/interfaces/EmailSender)

Defined in: [packages/email-templates/src/send/resend-sender.ts:46](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/resend-sender.ts#L46)

Create an [EmailSender](../../sender/interfaces/EmailSender) backed by Resend.

Server-only — never import this into a browser bundle or the API key leaks.
The key is read from the explicit argument or the `RESEND_API_KEY` env var and
validated up front (fail fast). Resend returns `{ data, error }` for API-level
failures rather than throwing, so we branch on `error` instead of try/catch.

Reads `process.env.RESEND_API_KEY` when no key is passed, and constructs a
Resend HTTP client. The returned `send` upholds the never-throws contract of
[EmailSender.send](../../sender/interfaces/EmailSender#send): API errors, an empty response, and transport-level
throws (fetch rejection, DNS, aborted request) all become `{ ok: false, error }`
with a distinguishing `error.name` (the Resend error name, `"unknown_error"`,
or `"transport_error"`). It does not honour an `AbortSignal`.

## Parameters

### apiKey?

`string` \| `undefined`

Resend API key; defaults to `process.env.RESEND_API_KEY`.

## Returns

[`EmailSender`](../../sender/interfaces/EmailSender)

An [EmailSender](../../sender/interfaces/EmailSender) that delivers through Resend.

## Throws

If no API key is available from the argument or the environment.
