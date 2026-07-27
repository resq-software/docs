# Type Alias: PositiveNumber

&gt; **PositiveNumber** = [`Brand`](../../brand/type-aliases/Brand)\<`number`, `"PositiveNumber"`\>

Defined in: [numeric.ts:64](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/numeric.ts#L64)

A finite real number strictly greater than zero — rates, weights, and scale
factors that may legitimately be fractional (e.g. `0.5` requests/second),
unlike [PositiveInt](./PositiveInt). Mint via [toPositiveNumber](../variables/toPositiveNumber),
[coercePositiveNumber](../variables/coercePositiveNumber), or [isPositiveNumber](../variables/isPositiveNumber).
