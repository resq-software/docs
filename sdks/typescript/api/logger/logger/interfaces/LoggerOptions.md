# Interface: LoggerOptions

Defined in: [logger.ts:80](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.ts#L80)

Configuration options for the Logger

## Properties

### colorize?

> `optional` **colorize?**: `boolean`

Defined in: [logger.ts:94](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.ts#L94)

Whether to colorize log output

***

### filePath?

> `optional` **filePath?**: `string`

Defined in: [logger.ts:104](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.ts#L104)

Path to the log file if logToFile is enabled

***

### includeTimestamp?

> `optional` **includeTimestamp?**: `boolean`

Defined in: [logger.ts:89](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.ts#L89)

Whether to include timestamps in log messages

***

### logToFile?

> `optional` **logToFile?**: `boolean`

Defined in: [logger.ts:99](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.ts#L99)

Whether to write logs to a file (server-side only)

***

### minLevel?

> `optional` **minLevel?**: [`LogLevel`](../enumerations/LogLevel)

Defined in: [logger.ts:84](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.ts#L84)

The minimum level of messages to log
