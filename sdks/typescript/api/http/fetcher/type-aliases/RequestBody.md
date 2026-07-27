# Type Alias: RequestBody

&gt; **RequestBody** = [`JsonValue`](./JsonValue) \| `FormData`

Defined in: [packages/http/src/fetcher.ts:179](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L179)

Represents a type-safe request body for HTTP methods that support a body.

Either a JSON-serialisable value (encoded via `bodyType: "json"`/`"text"`) or
a FormData instance (encoded via `bodyType: "form"`). These are the
two shapes the request builder actually supports; other transport payloads
are intentionally excluded so the type never lies about what will be sent.
