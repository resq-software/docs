# Type Alias: NonNegativeInt

&gt; **NonNegativeInt** = [`Brand`](../../brand/type-aliases/Brand)\<`number`, `"NonNegativeInt"`\>

Defined in: [numeric.ts:47](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/numeric.ts#L47)

A finite integer greater than or equal to zero (`0, 1, 2, …`). Differs from
[PositiveInt](./PositiveInt) only in admitting `0`. Mint via [toNonNegativeInt](../variables/toNonNegativeInt),
[coerceNonNegativeInt](../variables/coerceNonNegativeInt), or [isNonNegativeInt](../variables/isNonNegativeInt).
