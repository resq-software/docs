# Function: sanitizeRequestId()

&gt; **sanitizeRequestId**(`raw`): `Brand`

Defined in: [packages/http/src/security.ts:151](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/security.ts#L151)

Sanitize a raw, untrusted correlation ID into a [RequestId](../type-aliases/RequestId) — the ONLY
safe minting path for a caller-supplied value.

Strips every character outside `[A-Za-z0-9-_]` (defeating CRLF/log injection
and header smuggling) and truncates to MAX\_REQUEST\_ID\_LENGTH. When the
input contains no usable characters, a fresh UUID v4 is minted instead so the
result is always a non-empty, well-formed ID.

## Parameters

### raw

`string`

The untrusted inbound value (e.g. `x-request-id`).

## Returns

`Brand`

A branded, log-safe request ID.
