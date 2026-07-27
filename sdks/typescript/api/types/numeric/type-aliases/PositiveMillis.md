# Type Alias: PositiveMillis

&gt; **PositiveMillis** = [`Brand`](../../brand/type-aliases/Brand)\<`number`, `"PositiveMillis"`\>

Defined in: [numeric.ts:56](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/numeric.ts#L56)

A finite duration in milliseconds, strictly greater than zero. Fractional
values are allowed (the brand only enforces finite-and-positive, not integer);
the millisecond unit is a convention the brand name carries, not a runtime
check. Mint via [toPositiveMillis](../variables/toPositiveMillis), [coercePositiveMillis](../variables/coercePositiveMillis), or
[isPositiveMillis](../variables/isPositiveMillis).
