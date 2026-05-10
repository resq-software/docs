# Function: resolveResqCookieDomain()

> **resolveResqCookieDomain**(`host?`): `string` \| `undefined`

Defined in: [resq.ts:97](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/resq.ts#L97)

Resolve the production ResQ cookie domain only when the current host
actually lives under `resq.software`.

Cloudflare/Vercel preview URLs and `localhost` would otherwise have
their cookie rejected by the browser with a domain mismatch, silently
breaking analytics in every non-prod environment. This guards that
path so the package can ship safe defaults.

Hostnames are case-insensitive per RFC 3986 §3.2.2. Browsers normalise
`window.location.hostname` to lowercase, but server-side reads of the
`Host` header can carry whatever casing the client sent — normalise
here so a stray `RESQ.SOFTWARE` from a Workers `request.headers` read
still returns the cookie domain.

## Parameters

### host?

`string` \| `null`

The current hostname. In a browser, pass
  `window.location.hostname`. On the server pass the `Host` header
  value, or `null` / `undefined` (or call without an argument) to
  short-circuit cleanly.

## Returns

`string` \| `undefined`

`".resq.software"` when `host` belongs to that registrable
  root, otherwise `undefined` — assign the result directly to
  `AnalyticsConfig.cookieDomain`.
