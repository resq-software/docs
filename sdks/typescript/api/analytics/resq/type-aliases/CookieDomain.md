# Type Alias: CookieDomain

&gt; **CookieDomain** = `Brand`\<`string`, `"CookieDomain"`\>

Defined in: [resq.ts:129](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/resq.ts#L129)

A normalized cross-subdomain cookie domain in leading-dot form
(e.g. `.resq.software`).

The leading dot is load-bearing: it tells the browser to scope the cookie to
a registrable root *and every subdomain under it* — the entire point of the
cross-subdomain analytics setup. A bare `resq.software` (no dot) is silently
rejected by the browser as a domain mismatch, breaking analytics with no
error.

Branding makes "this string has been normalized to a valid leading-dot
domain" a compile-time fact: only [toCookieDomain](../functions/toCookieDomain) (or the guard
[isCookieDomain](../variables/isCookieDomain)) can mint one, so an unnormalized host can never reach
the PostHog / GA4 cookie sink by accident.
