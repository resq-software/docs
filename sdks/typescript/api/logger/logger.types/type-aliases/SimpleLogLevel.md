# Type Alias: SimpleLogLevel

&gt; **SimpleLogLevel** = \{ \[K in LogLevelString\]: Parameters\<Logger\[K\]\>\[1\] extends LogData \| undefined ? K : never \}\[[`LogLevelString`](./LogLevelString)\]

Defined in: [logger.types.ts:98](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/logger.types.ts#L98)

The subset of [LogLevelString](./LogLevelString) whose [Logger](../../logger/classes/Logger) method accepts a
`(message: string, data?: LogData)` call signature.

Deliberately excludes `"error"`: `Logger.error`'s second parameter is an
`Error`/`unknown`, not structured [LogData](../interfaces/LogData), so routing log data
through it would silently misinterpret the payload. Derived from the actual
method signatures on [Logger](../../logger/classes/Logger) (a method's second parameter must accept
only [LogData](../interfaces/LogData)), so it cannot drift from the class.
