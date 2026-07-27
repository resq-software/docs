# Interface: RenderedEmail

Defined in: [packages/email-templates/src/mailer.tsx:147](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L147)

The rendered, provider-ready email — the resolved output of
[Mailer.renderEmail](./Mailer#renderemail). `html` and `text` are two renderings of the *same*
message, so a provider may attach both as a multipart alternative.

## Properties

### html

&gt; **html**: `string`

Defined in: [packages/email-templates/src/mailer.tsx:153](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L153)

The complete standalone HTML document for the email body.

***

### subject

&gt; **subject**: `string`

Defined in: [packages/email-templates/src/mailer.tsx:151](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L151)

The subject line produced by the template's `subject` builder.

***

### text

&gt; **text**: `string`

Defined in: [packages/email-templates/src/mailer.tsx:155](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L155)

The plain-text alternative rendering of the same body, for text-only clients.

***

### to

&gt; **to**: `string` & `Brand`\<`"EmailAddress"`\>

Defined in: [packages/email-templates/src/mailer.tsx:149](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L149)

Validated recipient (branded [EmailAddress](../../schemas/variables/EmailAddress)), carried through from decode.
