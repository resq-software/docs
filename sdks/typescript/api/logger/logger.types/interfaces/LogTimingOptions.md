# Interface: LogTimingOptions

Defined in: [logger.types.ts:168](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/logger.types.ts#L168)

Options for the `@LogTiming` decorator.

## Properties

### label?

&gt; `optional` **label?**: `string`

Defined in: [logger.types.ts:170](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/logger.types.ts#L170)

Custom label for timing logs.

***

### level?

&gt; `optional` **level?**: [`LogLevelString`](../type-aliases/LogLevelString)

Defined in: [logger.types.ts:174](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/logger.types.ts#L174)

Log level to use (default: `"info"`).

***

### threshold?

&gt; `optional` **threshold?**: `number`

Defined in: [logger.types.ts:172](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/logger.types.ts#L172)

Threshold in ms — only log when execution exceeds this (default: `0`).
