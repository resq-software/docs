# Function: formatDateTime()

&gt; **formatDateTime**(`date`): `string`

Defined in: [packages/helpers/src/formatting/date.ts:122](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/date.ts#L122)

Formats a full date with time for display.

## Parameters

### date

`string` \| `Date`

The date to format.

## Returns

`string`

The formatted date and time string.

## Example

```ts
formatDateTime('2023-01-15T14:30:00Z')
// Returns: "January 15, 2023, 02:30 PM"
```
