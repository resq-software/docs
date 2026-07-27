# Type Alias: IndexKey

&gt; **IndexKey** = `string` & `object`

Defined in: [reordering.ts:51](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/reordering.ts#L51)

An order key: an integer part followed by an optional fraction part, whose
lexicographic (byte-wise) order *is* the intended list order — so two items
can be reordered by minting a key between their neighbours, never by
renumbering the rest.

The `__brand` tag is nominal: a plain `string` is not assignable to
`IndexKey`. Mint a valid value through [ZERO\_INDEX\_KEY](../variables/ZERO_INDEX_KEY), any of the
`getIndex*`/`getIndices*` generators (which return already-branded keys), or
by asserting an externally-sourced string with [validateIndexKey](../functions/validateIndexKey). The
brand asserts canonical form (no reserved smallest-integer key, no trailing
zero); it is a convention, not a runtime-enforced guarantee, since the
generators cast their output rather than re-validate it.

## Type Declaration

### \_\_brand

&gt; **\_\_brand**: `"indexKey"`
