# Function: formatDate()

&gt; **formatDate**(`date`, `options?`): `string`

Defined in: [packages/helpers/src/formatting/date.ts:45](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/date.ts#L45)

Format a date to a consistent, UTC-fixed string to prevent hydration
mismatches. Invalid dates return `"Invalid date"` rather than throwing.

Pure aside from a `console.error` emitted on the unexpected-`Intl`-failure
path before the sentinel is returned.

## Parameters

### date

`string` \| `Date`

The date to format (ISO string or `Date` object).

### options?

[`DateFormatOptions`](../../date.types/interfaces/DateFormatOptions) = `...`

Optional formatting options.

## Returns

`string`

The formatted date string, or the `"Invalid date"` sentinel when the
  input cannot be parsed or `Intl` formatting throws — branch on this string
  rather than assuming a valid result.

## Example

```ts
formatDate('2023-01-15T10:00:00Z', { month: 'short', year: 'numeric' })
// Returns: "Jan 2023"
```
