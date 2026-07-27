# Type Alias: HttpMethod

&gt; **HttpMethod** = `Schema.Schema.Type`\<*typeof* `HttpMethod`\>

Defined in: [packages/http/src/fetcher.ts:148](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L148)

The HTTP verbs [fetcher](../functions/fetcher) can issue: `GET`, `POST`, `PUT`, `PATCH`,
`DELETE`, `OPTIONS`, `HEAD`. Always upper-case — buildRequest matches
these literals exactly and has no case-folding fallback.
