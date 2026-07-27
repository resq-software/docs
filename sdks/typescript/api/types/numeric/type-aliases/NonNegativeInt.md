# Type Alias: NonNegativeInt

&gt; **NonNegativeInt** = [`Brand`](../../brand/type-aliases/Brand)\<`number`, `"NonNegativeInt"`\>

Defined in: [numeric.ts:47](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/numeric.ts#L47)

A finite integer greater than or equal to zero (`0, 1, 2, …`). Differs from
[PositiveInt](./PositiveInt) only in admitting `0`. Mint via [toNonNegativeInt](../variables/toNonNegativeInt),
[coerceNonNegativeInt](../variables/coerceNonNegativeInt), or [isNonNegativeInt](../variables/isNonNegativeInt).
