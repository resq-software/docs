# Interface: LoggerOptions

Defined in: [logger.types.ts:32](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L32)

Configuration options for the Logger

## Properties

### colorize?

> `optional` **colorize?**: `boolean`

Defined in: [logger.types.ts:44](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L44)

Whether to colorize log output

***

### filePath?

> `optional` **filePath?**: `string`

Defined in: [logger.types.ts:52](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L52)

Path to the log file if logToFile is enabled

***

### includeTimestamp?

> `optional` **includeTimestamp?**: `boolean`

Defined in: [logger.types.ts:40](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L40)

Whether to include timestamps in log messages

***

### logToFile?

> `optional` **logToFile?**: `boolean`

Defined in: [logger.types.ts:48](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L48)

Whether to write logs to a file (server-side only)

***

### minLevel?

> `optional` **minLevel?**: [`LogLevel`](../../logger/enumerations/LogLevel.md)

Defined in: [logger.types.ts:36](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L36)

The minimum level of messages to log
