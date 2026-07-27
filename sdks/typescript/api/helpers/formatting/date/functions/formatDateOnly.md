# Function: formatDateOnly()

&gt; **formatDateOnly**(`date`): `string`

Defined in: [packages/helpers/src/formatting/date.ts:143](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/date.ts#L143)

Formats a date for display without time.

## Parameters

### date

`string` \| `Date`

The date to format.

## Returns

`string`

The formatted date string.

## Example

```ts
formatDateOnly('2023-01-15')
// Returns: "January 15, 2023"
```
