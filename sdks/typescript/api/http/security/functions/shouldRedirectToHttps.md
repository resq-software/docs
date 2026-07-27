# Function: shouldRedirectToHttps()

&gt; **shouldRedirectToHttps**(`protocol`, `url`, `headers`, `nodeEnv?`): `string` \| `null`

Defined in: [packages/http/src/security.ts:68](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/security.ts#L68)

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

`LiteralUnion`\<`"http"` \| `"https"`\>

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

`LiteralUnion`\<`"development"` \| `"test"` \| `"production"`\> = `...`

Override for the environment guard. Defaults to
  `process.env.NODE_ENV` or `"development"`. Pass `"production"`
  explicitly when running outside Node (Bun, Deno, edge runtimes).

## Returns

`string` \| `null`

The redirect target (an `https://` URL) when a redirect is
  required, otherwise `null` (the request is already secure or in a
  non-prod environment).

## Throws

If a redirect is required (production/non-test and
  not already secure) and `url` is not a parseable absolute URL — it is
  passed to the `URL` constructor to derive the target. Not thrown on
  the `null` paths, which never parse `url`.

## Compliance

NIST 800-53 SC-8 (Transmission Confidentiality).

## Example

```ts
const target = shouldRedirectToHttps(req.protocol, req.url, req.headers);
if (target) return Response.redirect(target, 301);
```
