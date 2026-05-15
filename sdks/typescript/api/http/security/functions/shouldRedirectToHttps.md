# Function: shouldRedirectToHttps()

> **shouldRedirectToHttps**(`protocol`, `url`, `headers`, `nodeEnv?`): `string` \| `null`

Defined in: [packages/http/src/security.ts:59](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/http/src/security.ts#L59)

Decide whether an inbound HTTP request must be redirected to HTTPS,
accounting for reverse-proxy and load-balancer hops that terminate
TLS upstream.

The check inspects (in order) `x-forwarded-proto`, `x-forwarded-ssl`,
the raw `protocol`, and the URL prefix. A request is treated as
already-secure if **any** of these signals indicate HTTPS.

In `development` and `test` environments the function always returns
`null` to avoid breaking local workflows that run plain HTTP.

## Parameters

### protocol

`string`

The protocol string from the request (e.g. `"http"`
  or `"https"`). Typically `req.protocol` or `req.url.protocol`.

### url

`string`

Full request URL. Used both as a fallback signal and as
  the basis for the redirect target.

### headers

`Record`\<`string`, `string` \| `undefined`\>

Request headers. Only the proxy-related ones
  (`x-forwarded-proto`, `x-forwarded-ssl`) are consulted.

### nodeEnv?

`string` = `...`

Override for the environment guard. Defaults to
  `process.env.NODE_ENV` or `"development"`. Pass `"production"`
  explicitly when running outside Node (Bun, Deno, edge runtimes).

## Returns

`string` \| `null`

The redirect target (an `https://` URL) when a redirect is
  required, otherwise `null` (the request is already secure or in a
  non-prod environment).

## Compliance

NIST 800-53 SC-8 (Transmission Confidentiality).

## Example

```ts
const target = shouldRedirectToHttps(req.protocol, req.url, req.headers);
if (target) return Response.redirect(target, 301);
```
