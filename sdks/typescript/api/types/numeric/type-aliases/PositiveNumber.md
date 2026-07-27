# Type Alias: PositiveNumber

&gt; **PositiveNumber** = [`Brand`](../../brand/type-aliases/Brand)\<`number`, `"PositiveNumber"`\>

Defined in: [numeric.ts:64](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/numeric.ts#L64)

A finite real number strictly greater than zero — rates, weights, and scale
factors that may legitimately be fractional (e.g. `0.5` requests/second),
unlike [PositiveInt](./PositiveInt). Mint via [toPositiveNumber](../variables/toPositiveNumber),
[coercePositiveNumber](../variables/coercePositiveNumber), or [isPositiveNumber](../variables/isPositiveNumber).
