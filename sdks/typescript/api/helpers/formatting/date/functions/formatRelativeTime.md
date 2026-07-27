# Function: formatRelativeTime()

&gt; **formatRelativeTime**(`date`): `string`

Defined in: [packages/helpers/src/formatting/date.ts:181](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/date.ts#L181)

Formats a relative time string (e.g. "2 days ago").

Reads the current clock (`new Date()`), so the result is **non-deterministic**
and depends on when it is called. Only past instants are described: a `date`
in the future yields a negative delta that falls through every branch and
returns `"Just now"`. Granularity tops out at days (no weeks/months/years).

## Parameters

### date

`string` \| `Date`

The date to compare against now (ISO string or `Date`).

## Returns

`string`

The relative time string — one of `"Just now"`, `"N minute(s) ago"`,
  `"N hour(s) ago"`, or `"N day(s) ago"`.
