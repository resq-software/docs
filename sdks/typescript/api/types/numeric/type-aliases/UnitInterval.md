# Type Alias: UnitInterval

&gt; **UnitInterval** = [`Brand`](../../brand/type-aliases/Brand)\<`number`, `"UnitInterval"`\>

Defined in: [numeric.ts:72](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/numeric.ts#L72)

A real number in the **closed** unit interval `[0, 1]` — probabilities, error
rates, fractions, ratios. Both endpoints are valid (`0` and `1` pass);
`±Infinity` and `NaN` do not. Mint via [toUnitInterval](../variables/toUnitInterval),
[coerceUnitInterval](../variables/coerceUnitInterval), or [isUnitInterval](../variables/isUnitInterval).
