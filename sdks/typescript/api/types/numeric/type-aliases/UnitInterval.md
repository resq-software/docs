# Type Alias: UnitInterval

&gt; **UnitInterval** = [`Brand`](../../brand/type-aliases/Brand)\<`number`, `"UnitInterval"`\>

Defined in: [numeric.ts:72](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/numeric.ts#L72)

A real number in the **closed** unit interval `[0, 1]` — probabilities, error
rates, fractions, ratios. Both endpoints are valid (`0` and `1` pass);
`±Infinity` and `NaN` do not. Mint via [toUnitInterval](../variables/toUnitInterval),
[coerceUnitInterval](../variables/coerceUnitInterval), or [isUnitInterval](../variables/isUnitInterval).
