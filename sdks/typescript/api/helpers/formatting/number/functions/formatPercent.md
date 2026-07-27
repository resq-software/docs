# Function: formatPercent()

&gt; **formatPercent**(`value`): `string`

Defined in: [packages/helpers/src/formatting/number.ts:107](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/number.ts#L107)

Format a fractional value (0–1 range) as a percentage with one
decimal place.

## Parameters

### value

`number`

Fractional value where `1` = 100%. Inputs outside the
  `[0, 1]` range are formatted as-is (e.g. `formatPercent(2)` →
  `"200.0%"`); the helper does not clamp.

## Returns

`string`

Percentage string with one decimal place.

## Example

```ts
formatPercent(0);     // → "0.0%"
formatPercent(0.5);   // → "50.0%"
formatPercent(0.123); // → "12.3%"
formatPercent(1);     // → "100.0%"
```
