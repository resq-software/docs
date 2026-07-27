# Type Alias: EmailTemplateData\<N\>

&gt; **EmailTemplateData**\<`N`\> = `Extract`\<[`EmailPayload`](./EmailPayload), \{ `name`: `N`; \}\>\[`"data"`\]

Defined in: [packages/email-templates/src/contract.ts:48](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/contract.ts#L48)

The `data` shape for a given built-in template name — the `data` field of the
[EmailPayload](../variables/EmailPayload) variant whose discriminant equals `N`.

## Type Parameters

### N

`N` *extends* [`EmailName`](./EmailName)

The template name selecting a single variant's `data` shape.
