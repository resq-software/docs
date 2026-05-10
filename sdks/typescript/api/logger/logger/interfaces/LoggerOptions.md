# Interface: LoggerOptions

Defined in: [logger.ts:80](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L80)

Configuration options for the Logger

## Properties

### colorize?

> `optional` **colorize?**: `boolean`

Defined in: [logger.ts:94](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L94)

Whether to colorize log output

***

### filePath?

> `optional` **filePath?**: `string`

Defined in: [logger.ts:104](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L104)

Path to the log file if logToFile is enabled

***

### includeTimestamp?

> `optional` **includeTimestamp?**: `boolean`

Defined in: [logger.ts:89](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L89)

Whether to include timestamps in log messages

***

### logToFile?

> `optional` **logToFile?**: `boolean`

Defined in: [logger.ts:99](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L99)

Whether to write logs to a file (server-side only)

***

### minLevel?

> `optional` **minLevel?**: [`LogLevel`](../enumerations/LogLevel.md)

Defined in: [logger.ts:84](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L84)

The minimum level of messages to log
