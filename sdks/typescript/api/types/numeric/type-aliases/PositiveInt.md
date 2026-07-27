# Type Alias: PositiveInt

&gt; **PositiveInt** = [`Brand`](../../brand/type-aliases/Brand)\<`number`, `"PositiveInt"`\>

Defined in: [numeric.ts:40](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/numeric.ts#L40)

A finite integer strictly greater than zero (`1, 2, 3, …`). Excludes `0`,
negatives, non-integers, `NaN`, and `±Infinity`. Mint via [toPositiveInt](../variables/toPositiveInt)
(throws on violation), [coercePositiveInt](../variables/coercePositiveInt) (returns `null`), or narrow an
existing `number` with [isPositiveInt](../variables/isPositiveInt).
