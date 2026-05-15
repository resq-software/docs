# Function: getRequestId()

> **getRequestId**(`existingId?`): `string`

Defined in: [packages/http/src/security.ts:114](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/security.ts#L114)

Resolve the request ID for an inbound request — passing through any
caller-supplied value verbatim, otherwise minting a fresh UUID v4 via
`crypto.randomUUID()`.

Use as the source of truth for the per-request correlation ID written
into log lines, response headers (`x-request-id`), and downstream
service hops. Trusting an upstream-supplied ID lets distributed
traces follow the request across service boundaries without
regeneration.

## Parameters

### existingId?

`string`

Inbound `x-request-id` (or equivalent), if any.
  Returned unchanged when truthy; no validation is applied, so do not
  echo untrusted values into log structures without your own
  sanitization.

## Returns

`string`

The supplied ID, or a freshly generated UUID v4.

## Example

```ts
const requestId = getRequestId(req.headers["x-request-id"]);
res.headers.set("x-request-id", requestId);
logger.info("incoming request", { requestId, path: req.url });
```
