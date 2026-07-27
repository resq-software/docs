# Interface: LogEntry

Defined in: [logger.types.ts:109](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L109)

A structured log entry as delivered to every registered [LogTransport](./LogTransport).

Assembled fresh per emitted log after level filtering; the same object
instance is handed to every transport, so a transport must treat it as
read-only rather than mutate the shared entry.

## Properties

### context

&gt; **context**: `string`

Defined in: [logger.types.ts:115](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L115)

Logger context/category that emitted the entry.

***

### data?

&gt; `optional` **data?**: [`LogData`](./LogData)

Defined in: [logger.types.ts:122](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L122)

Structured payload. Absent when no data was passed *or* the passed object
was empty — an empty bag is dropped rather than emitted as `{}`.

***

### environment

&gt; **environment**: `"client"` \| `"server"`

Defined in: [logger.types.ts:127](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L127)

Where the entry originated, derived from `typeof window`: `"server"` when
`window` is undefined, otherwise `"client"`.

***

### level

&gt; **level**: [`LogLevelString`](../type-aliases/LogLevelString)

Defined in: [logger.types.ts:113](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L113)

Severity level of the entry.

***

### message

&gt; **message**: `string`

Defined in: [logger.types.ts:117](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L117)

Human-readable log message.

***

### timestamp

&gt; **timestamp**: `string`

Defined in: [logger.types.ts:111](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L111)

UTC timestamp in ISO-8601 (`Date#toISOString`), captured at dispatch time.
