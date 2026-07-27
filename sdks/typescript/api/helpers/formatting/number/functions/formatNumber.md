# Function: formatNumber()

&gt; **formatNumber**(`num`): `string`

Defined in: [packages/helpers/src/formatting/number.ts:47](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/number.ts#L47)

Format a number with US-English thousands separators using
`Intl.NumberFormat` (default options).

Note: `Intl.NumberFormat` applies its own locale rounding for
presentation — by default it caps fraction digits at 3 for
non-integer values. Pass `Intl.NumberFormat` directly when you
need precise control over `minimumFractionDigits` /
`maximumFractionDigits`.

## Parameters

### num

`number`

The number to format. `NaN` and `Infinity` are formatted
  per the runtime's `Intl` implementation (typically `"NaN"` / `"∞"`).

## Returns

`string`

A locale-formatted string, e.g. `formatNumber(1234567)` →
  `"1,234,567"`.

## Example

```ts
formatNumber(1234567);   // → "1,234,567"
formatNumber(0);         // → "0"
formatNumber(0.5);       // → "0.5"
```
