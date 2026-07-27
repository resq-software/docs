# Function: inferCookieDomain()

&gt; **inferCookieDomain**(`domains`): `any`

Defined in: [index.ts:521](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L521)

Derive the shared registrable-root cookie domain from a set of hosts. Returns
the longest common dot-suffix in normalized leading-dot [CookieDomain](../../resq/type-aliases/CookieDomain)
form (e.g. `["research.resq.software", "viz.resq.software"]` →
`".resq.software"`), or `undefined` when the hosts share no multi-label root.

Pure and total: never throws. An empty input list, or hosts whose only common
suffix is a single label, yields the `undefined` sentinel.

## Parameters

### domains

`string`[]

The hosts to reduce to their shared registrable root.

## Returns

`any`

The branded shared [CookieDomain](../../resq/type-aliases/CookieDomain), or the `undefined` sentinel
  when there is no shared multi-label root.

## Example

```ts
inferCookieDomain(["research.resq.software", "viz.resq.software"]);
// → branded ".resq.software"
inferCookieDomain(["a.example.com", "b.other.org"]); // → undefined
```
