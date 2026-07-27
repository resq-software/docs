# Interface: LogTimingOptions

Defined in: [logger.types.ts:168](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L168)

Options for the `@LogTiming` decorator.

## Properties

### label?

&gt; `optional` **label?**: `string`

Defined in: [logger.types.ts:170](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L170)

Custom label for timing logs.

***

### level?

&gt; `optional` **level?**: [`LogLevelString`](../type-aliases/LogLevelString)

Defined in: [logger.types.ts:174](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L174)

Log level to use (default: `"info"`).

***

### threshold?

&gt; `optional` **threshold?**: `number`

Defined in: [logger.types.ts:172](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L172)

Threshold in ms — only log when execution exceeds this (default: `0`).
