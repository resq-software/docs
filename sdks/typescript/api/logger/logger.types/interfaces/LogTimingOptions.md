# Interface: LogTimingOptions

Defined in: [logger.types.ts:125](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L125)

Options for the

## Log Timing

decorator

## Properties

### label?

> `optional` **label?**: `string`

Defined in: [logger.types.ts:127](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L127)

Custom label for timing logs

***

### level?

> `optional` **level?**: [`LogLevelString`](../type-aliases/LogLevelString.md)

Defined in: [logger.types.ts:131](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L131)

Log level to use (default: 'info')

***

### threshold?

> `optional` **threshold?**: `number`

Defined in: [logger.types.ts:129](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L129)

Threshold in ms - only log if execution exceeds this (default: 0)
