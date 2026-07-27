# Function: withEmailMessage()

&gt; **withEmailMessage**(`element`, `message?`): `ReactElement`

Defined in: [packages/email-templates/src/emails/theme.tsx:229](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L229)

Wrap an element so it renders against a message policy (used by `renderEmail`).
Returns the element unchanged when no message is given, so the default
transactional policy flows through context.

Pure — builds a new provider element and does not mutate `element`.

## Parameters

### element

`ReactElement`

The email element tree to wrap.

### message?

[`EmailMessage`](../interfaces/EmailMessage)

The per-send policy; when omitted, `element` is returned unchanged.

## Returns

`ReactElement`

`element`, wrapped in an [EmailMessageContext](../variables/EmailMessageContext) provider when a message is given.
