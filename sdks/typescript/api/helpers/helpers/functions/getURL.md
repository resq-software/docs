# Function: getURL()

&gt; **getURL**(`path?`): `string`

Defined in: [packages/helpers/src/helpers.ts:72](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L72)

Build an absolute URL from the current origin plus an optional path.

Uses `globalThis.location.origin` in the browser, falling back to the
`VITE_BASE_URL` / `NEXT_PUBLIC_BASE_URL` / `BASE_URL` env vars on the server,
and returns `""` when no origin can be resolved. Intended for same-origin
client-side use, not as a fixed cross-environment API base.

Reads global/environment state only; the sole side effect is a `warn` log
(via `@resq-systems/logger`) emitted on the empty-string fallback path when
neither an origin nor an env base URL is available.

## Parameters

### path?

`string` = `""`

Path to append to the origin; leading slashes are trimmed.

## Returns

`string`

The combined URL, or `""` (the sentinel for "no origin resolvable")
  — check for it rather than assuming a usable absolute URL.

## Example

```ts
// On "http://localhost:5173/dashboard":
getURL("api/users"); // → "http://localhost:5173/api/users"
getURL();            // → "http://localhost:5173"
```
