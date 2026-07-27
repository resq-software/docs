# Type Alias: HostPattern

&gt; **HostPattern** = `Lowercase`\<`string`\> \| `` `*.${string}` ``

Defined in: [packages/http/src/fetcher.ts:63](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/fetcher.ts#L63)

A host-matching pattern for the SSRF allow/block lists
([FetcherOptions.allowedHosts](../interfaces/FetcherOptions#allowedhosts), [FetcherOptions.blockedHosts](../interfaces/FetcherOptions#blockedhosts)).

Either an exact hostname (`"api.example.com"`) or a wildcard-subdomain
pattern (`` `*.example.com` ``).

The two members document the supported shapes, but this is **not** a
compile-time SSRF guarantee: `Lowercase<string>` evaluates to `string`, so
the union widens to `string` and does not reject uppercase or otherwise
malformed literals at the type level. Case-insensitive matching and host
normalization are enforced at **runtime** by `matchHost` (which lowercases
both the pattern and the request host before comparing), so an entry like
`"API.example.com"` still matches correctly.
