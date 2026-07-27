# Type Alias: SimpleLogLevel

&gt; **SimpleLogLevel** = \{ \[K in LogLevelString\]: Parameters\<Logger\[K\]\>\[1\] extends LogData \| undefined ? K : never \}\[[`LogLevelString`](./LogLevelString)\]

Defined in: [logger.types.ts:98](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L98)

The subset of [LogLevelString](./LogLevelString) whose [Logger](../../logger/classes/Logger) method accepts a
`(message: string, data?: LogData)` call signature.

Deliberately excludes `"error"`: `Logger.error`'s second parameter is an
`Error`/`unknown`, not structured [LogData](../interfaces/LogData), so routing log data
through it would silently misinterpret the payload. Derived from the actual
method signatures on [Logger](../../logger/classes/Logger) (a method's second parameter must accept
only [LogData](../interfaces/LogData)), so it cannot drift from the class.
