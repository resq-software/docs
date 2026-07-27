# Interface: Mailer\<Payload\>

Defined in: [packages/email-templates/src/mailer.tsx:193](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L193)

A composed set of templates: contract schema, decoder, registry, and renderer.

## Type Parameters

### Payload

`Payload` *extends* `object`

## Properties

### names

&gt; `readonly` **names**: readonly `Payload`\[`"name"`\][]

Defined in: [packages/email-templates/src/mailer.tsx:201](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L201)

Every registered template name, in def order.

***

### registry

&gt; `readonly` **registry**: `Record`\<`Payload`\[`"name"`\], [`EmailRegistryEntry`](./EmailRegistryEntry)\>

Defined in: [packages/email-templates/src/mailer.tsx:199](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L199)

name → &#123; subject, render &#125; for every template.

***

### schema

&gt; `readonly` **schema**: `Top`

Defined in: [packages/email-templates/src/mailer.tsx:197](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L197)

The Effect Schema union describing every `{ name, to, data }` payload.

## Methods

### decode()

&gt; **decode**(`input`): `Payload`

Defined in: [packages/email-templates/src/mailer.tsx:211](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L211)

Validate an untrusted payload against the contract union and return the
narrowed [Payload](#payload).

#### Parameters

##### input

`unknown`

Untrusted `{ name, to, data }` value from the boundary.

#### Returns

`Payload`

The validated, branded payload.

#### Throws

If `input` matches no template variant — bad
  `name`, a malformed/header-injecting `to`, or `data` failing its schema.

***

### renderEmail()

&gt; **renderEmail**(`input`, `options?`): `Promise`\<[`RenderedEmail`](./RenderedEmail)\>

Defined in: [packages/email-templates/src/mailer.tsx:227](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L227)

Validate then render a payload to `{ to, subject, html, text }`.

Validates via [decode](#decode) first, then renders headlessly through
`@react-email/render` — no browser, DOM, network, or clock — so it is safe in
queue workers and cron jobs. Pure and stateless: concurrent calls against one
mailer do not interfere, and there is no ordering guarantee between them. Does
not honour an `AbortSignal`.

#### Parameters

##### input

`unknown`

Untrusted payload to validate and render.

##### options?

[`RenderEmailOptions`](./RenderEmailOptions)

Optional per-render theme override.

#### Returns

`Promise`\<[`RenderedEmail`](./RenderedEmail)\>

A promise resolving to the rendered email.

#### Throws

As a rejected promise, when `input` fails
  validation (surfaced from [decode](#decode)).
