# Function: getRequestId()

&gt; **getRequestId**(`existingId?`): `Brand`

Defined in: [packages/http/src/security.ts:184](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/security.ts#L184)

Resolve the request ID for an inbound request — sanitizing any caller-supplied
value via [sanitizeRequestId](./sanitizeRequestId), otherwise minting a fresh UUID v4 via
`crypto.randomUUID()`.

Use as the source of truth for the per-request correlation ID written into log
lines, response headers (`x-request-id`), and downstream service hops.
Trusting an upstream-supplied ID lets distributed traces follow the request
across service boundaries — but the raw value is untrusted, so it is passed
through [sanitizeRequestId](./sanitizeRequestId) (safe charset + length bound) before use.

## Parameters

### existingId?

`string`

Inbound `x-request-id` (or equivalent), if any. Sanitized
  (not echoed verbatim) when truthy; unsafe characters are stripped so the
  value cannot inject CRLF into logs or smuggle response headers.

## Returns

`Brand`

A branded [RequestId](../type-aliases/RequestId): the sanitized inbound value, or a freshly
  generated UUID v4.

## Example

```ts
const requestId = getRequestId(req.headers["x-request-id"]);
res.headers.set("x-request-id", requestId);
logger.info("incoming request", { requestId, path: req.url });
```
