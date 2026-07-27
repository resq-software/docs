# Function: resolveResqCookieDomain()

&gt; **resolveResqCookieDomain**(`host?`): `any`

Defined in: [resq.ts:224](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/resq.ts#L224)

Resolve the production ResQ cookie domain only when the current host
actually lives under `resq.software`.

Cloudflare/Vercel preview URLs and `localhost` would otherwise have
their cookie rejected by the browser with a domain mismatch, silently
breaking analytics in every non-prod environment. This guards that
path so the package can ship safe defaults.

Hostnames are case-insensitive per RFC 3986 §3.2.2. Browsers normalize
`window.location.hostname` to lowercase, but server-side reads of the
`Host` header can carry whatever casing the client sent — normalize
here so a stray `RESQ.SOFTWARE` from a Workers `request.headers` read
still returns the cookie domain.

Pure and total: never throws. A host outside the `resq.software` root, an
empty string, or a nullish argument yields the `undefined` sentinel.

## Parameters

### host?

`string` \| `null`

The current hostname. In a browser, pass
  `window.location.hostname`. On the server pass the `Host` header
  value, or `null` / `undefined` (or call without an argument) to
  short-circuit cleanly.

## Returns

`any`

the branded `".resq.software"` [CookieDomain](../type-aliases/CookieDomain) when `host`
  belongs to that registrable root, otherwise the `undefined` sentinel —
  assign the result directly to `AnalyticsConfig.cookieDomain`.

## Example

```ts
resolveResqCookieDomain("viz.resq.software"); // → branded ".resq.software"
resolveResqCookieDomain("preview-abc.vercel.app"); // → undefined
resolveResqCookieDomain("localhost"); // → undefined
```
