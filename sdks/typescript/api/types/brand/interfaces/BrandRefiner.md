# Interface: BrandRefiner\<T, B\>

Defined in: [brand.ts:131](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/brand.ts#L131)

A smart-constructor bundle for a single brand, built from one runtime
predicate. Returned by [brandRefiner](../functions/brandRefiner).

## Type Parameters

### T

`T`

The carrier type.

### B

`B` *extends* `PropertyKey`

The brand name.

## Properties

### coerce

&gt; `readonly` **coerce**: (`value`) =&gt; [`Brand`](../type-aliases/Brand)\<`T`, `B`\> \| `null`

Defined in: [brand.ts:146](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/brand.ts#L146)

Return the branded value if valid, or `null` — the total, throw-free
counterpart of [from](#from). Compose with `?.` / `??`.

#### Parameters

##### value

`T`

#### Returns

[`Brand`](../type-aliases/Brand)\<`T`, `B`\> \| `null`

***

### from

&gt; `readonly` **from**: (`value`) =&gt; [`Brand`](../type-aliases/Brand)\<`T`, `B`\>

Defined in: [brand.ts:141](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/brand.ts#L141)

Assert the value is valid and return it branded, throwing a `TypeError`
otherwise. Use at trust boundaries where an invalid value is a bug.

#### Parameters

##### value

`T`

#### Returns

[`Brand`](../type-aliases/Brand)\<`T`, `B`\>

***

### is

&gt; `readonly` **is**: (`value`) =&gt; `value is Brand<T, B>`

Defined in: [brand.ts:136](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/brand.ts#L136)

Type guard: narrows `value` to the branded type when the predicate holds.
Use in `if`/`filter` so downstream code sees the brand.

#### Parameters

##### value

`T`

#### Returns

`value is Brand<T, B>`

***

### unsafe

&gt; `readonly` **unsafe**: (`value`) =&gt; [`Brand`](../type-aliases/Brand)\<`T`, `B`\>

Defined in: [brand.ts:151](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/brand.ts#L151)

Brand without checking. Identical to [unsafeBrand](../functions/unsafeBrand) but pinned to this
refiner's `T` and `B`, so it reads as an intentional, named bypass.

#### Parameters

##### value

`T`

#### Returns

[`Brand`](../type-aliases/Brand)\<`T`, `B`\>
