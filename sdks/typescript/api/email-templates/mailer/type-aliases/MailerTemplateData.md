# Type Alias: MailerTemplateData\<Defs, Name\>

&gt; **MailerTemplateData**\<`Defs`, `Name`\> = `Extract`\<[`MailerPayload`](./MailerPayload)\<`Defs`\>, \{ `name`: `Name`; \}\>\[`"data"`\]

Defined in: [packages/email-templates/src/mailer.tsx:137](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L137)

The `data` type for a given template name within a set of defs — the `data`
field of the [MailerPayload](./MailerPayload) variant whose discriminant equals `Name`.

## Type Parameters

### Defs

`Defs` *extends* readonly `AnyTemplateDef`[]

The tuple of template defs the payload union is built over.

### Name

`Name` *extends* [`MailerPayload`](./MailerPayload)\<`Defs`\>\[`"name"`\]

The literal `name` selecting a single variant's `data` shape.
