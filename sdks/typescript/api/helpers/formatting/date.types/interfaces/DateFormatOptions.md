# Interface: DateFormatOptions

Defined in: [packages/helpers/src/formatting/date.types.ts:34](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/date.types.ts#L34)

Format options for date display — the subset of `Intl.DateTimeFormat`
component options the formatters expose.

Every field is optional and passed straight through to `Intl`: only the
components you set appear in the output, and the set of present fields
determines the shape of the result (e.g. `month` + `year` yields `"Jan 2023"`,
adding `hour` + `minute` yields a date-time). The token values match `Intl`'s
own vocabulary.

## Properties

### day?

&gt; `optional` **day?**: `"numeric"` \| `"2-digit"`

Defined in: [packages/helpers/src/formatting/date.types.ts:40](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/date.types.ts#L40)

`"numeric"` → `5`, `"2-digit"` → `05`.

***

### hour?

&gt; `optional` **hour?**: `"numeric"` \| `"2-digit"`

Defined in: [packages/helpers/src/formatting/date.types.ts:42](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/date.types.ts#L42)

Hour digits; rendered in the formatter's fixed UTC zone.

***

### minute?

&gt; `optional` **minute?**: `"numeric"` \| `"2-digit"`

Defined in: [packages/helpers/src/formatting/date.types.ts:44](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/date.types.ts#L44)

Minute digits, e.g. `"2-digit"` → `07`.

***

### month?

&gt; `optional` **month?**: `"short"` \| `"long"` \| `"numeric"`

Defined in: [packages/helpers/src/formatting/date.types.ts:36](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/date.types.ts#L36)

`"short"` → `Jan`, `"long"` → `January`, `"numeric"` → `1`.

***

### year?

&gt; `optional` **year?**: `"numeric"` \| `"2-digit"`

Defined in: [packages/helpers/src/formatting/date.types.ts:38](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/date.types.ts#L38)

`"numeric"` → `2023`, `"2-digit"` → `23`.
