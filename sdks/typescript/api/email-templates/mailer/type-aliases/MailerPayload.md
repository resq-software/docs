# Type Alias: MailerPayload\<Defs\>

&gt; **MailerPayload**\<`Defs`\> = `PayloadFor`\<`Defs`\[`number`\]\>

Defined in: [packages/email-templates/src/mailer.tsx:128](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/mailer.tsx#L128)

The discriminated payload union for a tuple of template defs — one
`{ name, to, data, category?, unsubscribeUrl? }` variant per def, discriminated
by the literal `name` field. Narrow a value with `payload.name` to recover the
matching `data` type.

## Type Parameters

### Defs

`Defs` *extends* readonly `AnyTemplateDef`[]

The `as const` tuple of template defs the union is built over.
