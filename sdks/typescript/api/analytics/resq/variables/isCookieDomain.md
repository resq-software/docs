# Variable: isCookieDomain

&gt; `const` **isCookieDomain**: (`value`) =&gt; `value is CookieDomain` = `cookieDomainRefiner.is`

Defined in: [resq.ts:151](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/resq.ts#L151)

Type guard: narrows a string to [CookieDomain](../type-aliases/CookieDomain) when it is *already* in
normalized leading-dot form. Does **not** normalize — reach for
[toCookieDomain](../functions/toCookieDomain) when the input may be a bare host.

## Parameters

### value

`string`

## Returns

`value is CookieDomain`
