# Variable: HttpUrl

&gt; `const` **HttpUrl**: `String`

Defined in: [packages/email-templates/src/schemas.ts:34](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/schemas.ts#L34)

A non-empty, absolute http(s) URL. Validated with a pattern check (blocks
`javascript:`/relative hrefs) but decoded as a plain `string`, so template
props stay ergonomic. Exported for consumers building their own templates.
