# Variable: renderEmail

&gt; `const` **renderEmail**: (`input`, `options?`) =&gt; `Promise`\<[`RenderedEmail`](../../mailer/interfaces/RenderedEmail)\> = `resqMailer.renderEmail`

Defined in: [packages/email-templates/src/render.ts:43](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/render.ts#L43)

Validate an untrusted payload and render it to `{ to, subject, html, text }`.

Runs headlessly (no browser/DOM, no network, no clock) via
`@react-email/render`, so it is safe from queue workers, cron jobs, and other
pipeline contexts. Pure and stateless — concurrent calls are safe and there is
no ordering guarantee; it does not honour an `AbortSignal`. Pass `{ theme }` to
rebrand a single render.

Validate then render a payload to `{ to, subject, html, text }`.

Validates via [decode](../../mailer/interfaces/Mailer#decode) first, then renders headlessly through
`@react-email/render` — no browser, DOM, network, or clock — so it is safe in
queue workers and cron jobs. Pure and stateless: concurrent calls against one
mailer do not interfere, and there is no ordering guarantee between them. Does
not honour an `AbortSignal`.

## Parameters

### input

`unknown`

Untrusted payload to validate and render.

### options?

[`RenderEmailOptions`](../../mailer/interfaces/RenderEmailOptions)

Optional per-render theme override.

## Returns

`Promise`\<[`RenderedEmail`](../../mailer/interfaces/RenderedEmail)\>

A promise resolving to the rendered email.

## Throws

As a rejected promise, when `input` fails
  validation (surfaced from [decode](../../mailer/interfaces/Mailer#decode)).

## Param

**input**

Untrusted `{ name, to, data }` payload to validate and render.

## Param

**options**

Optional per-render theme override.

## Returns

A promise resolving to the rendered `{ to, subject, html, text }`.

## Throws

As a rejected promise, when `input` fails validation.
