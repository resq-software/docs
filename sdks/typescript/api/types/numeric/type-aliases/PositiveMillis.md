# Type Alias: PositiveMillis

&gt; **PositiveMillis** = [`Brand`](../../brand/type-aliases/Brand)\<`number`, `"PositiveMillis"`\>

Defined in: [numeric.ts:56](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/numeric.ts#L56)

A finite duration in milliseconds, strictly greater than zero. Fractional
values are allowed (the brand only enforces finite-and-positive, not integer);
the millisecond unit is a convention the brand name carries, not a runtime
check. Mint via [toPositiveMillis](../variables/toPositiveMillis), [coercePositiveMillis](../variables/coercePositiveMillis), or
[isPositiveMillis](../variables/isPositiveMillis).
