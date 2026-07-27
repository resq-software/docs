# Function: formatDatePeriod()

&gt; **formatDatePeriod**(`startDate`, `endDate?`, `isCurrent?`): `string`

Defined in: [packages/helpers/src/formatting/date.ts:92](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/date.ts#L92)

Formats a date period (start to end or start to present).

The period is treated as ongoing (`"… - Present"`) when `isCurrent` is `true`
**or** when `endDate` is omitted/`null` — so a missing end date always reads
as "Present" regardless of `isCurrent`.

## Parameters

### startDate

`string` \| `Date`

The start date.

### endDate?

`string` \| `Date` \| `null`

The end date; `null`/omitted means ongoing ("Present").

### isCurrent?

`boolean` = `false`

Forces the ongoing ("Present") rendering even when an
  `endDate` is supplied.

## Returns

`string`

The formatted date period string.

## Example

```ts
formatDatePeriod('2023-01-01', '2023-12-31')
// Returns: "Jan 2023 - Dec 2023"

formatDatePeriod('2023-01-01', null, true)
// Returns: "Jan 2023 - Present"
```
