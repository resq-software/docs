# Interface: Tag\<B\>

Defined in: [brand.ts:60](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/brand.ts#L60)

The phantom tag carrier. Brands compose: intersecting `Tag<"A">` with
`Tag<"B">` yields a carrier for both tags rather than collapsing to `never`,
so [Brand](../type-aliases/Brand)&lt;[Brand](../type-aliases/Brand)&lt;T, "A"&gt;, "B"&gt; is a value that is *both* an `A`
and a `B`.

## Type Parameters

### B

`B` *extends* `PropertyKey`

The brand name(s) held by this carrier.

## Properties

### \[BRAND\]

&gt; `readonly` **\[BRAND\]**: `{ readonly [K in PropertyKey]: true }`

Defined in: [brand.ts:61](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/brand.ts#L61)
