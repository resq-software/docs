# Type Alias: JsonValue

&gt; **JsonValue** = `string` \| `number` \| `boolean` \| `null` \| \{\[`key`: `string`\]: `JsonValue`; \} \| readonly `JsonValue`[]

Defined in: [packages/http/src/fetcher.ts:163](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L163)

A JSON-serialisable value: the recursive shape `bodyType: "json"` (the
default) accepts and `HttpClientRequest.bodyJson` can encode.
