# Type Alias: SendResult

&gt; **SendResult** = \{ `id`: `string`; `ok`: `true`; \} \| \{ `error`: \{ `message`: `string`; `name`: `string`; \}; `ok`: `false`; \}

Defined in: [packages/email-templates/src/send/sender.ts:59](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/send/sender.ts#L59)

Normalized send result — a discriminated union keyed by the `ok` boolean.
Providers map their responses onto this shape so callers branch on `ok` rather
than on provider specifics.

When `ok` is `true`, `id` is the provider's message id. When `ok` is `false`,
`error.name` is a stable, machine-branchable tag and `error.message` is a
human-readable detail.
