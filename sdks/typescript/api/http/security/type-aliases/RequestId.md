# Type Alias: RequestId

&gt; **RequestId** = `Brand`\<`string`, `"RequestId"`\>

Defined in: [packages/http/src/security.ts:112](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/security.ts#L112)

A correlation ID that is safe to write into log lines, response headers, and
downstream service hops.

The brand is nominal: a plain `string` is **not** assignable to `RequestId`.
The only way to obtain one is [sanitizeRequestId](../functions/sanitizeRequestId) (which strips a raw,
possibly-untrusted value down to a safe charset) or [getRequestId](../functions/getRequestId).
This makes it a type error to log an unsanitized header value as a request ID.
