# Type Alias: Headers

&gt; **Headers** = `Schema.Schema.Type`\<*typeof* `Headers`\>

Defined in: [packages/http/src/fetcher.ts:185](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L185)

HTTP headers as a flat map of string names to single string values. Multi-value
headers are not modelled here — pass a pre-joined string. Header-name case is
preserved as given; no normalisation is applied at this layer.
