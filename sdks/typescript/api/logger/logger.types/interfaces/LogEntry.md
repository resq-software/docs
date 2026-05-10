# Interface: LogEntry

Defined in: [logger.types.ts:80](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L80)

Structured log entry for transport/storage

## Properties

### context

> **context**: `string`

Defined in: [logger.types.ts:86](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L86)

Logger context/category

***

### data?

> `optional` **data?**: [`LogData`](./LogData.md)

Defined in: [logger.types.ts:90](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L90)

Optional structured data

***

### environment

> **environment**: `"client"` \| `"server"`

Defined in: [logger.types.ts:92](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L92)

Environment (client/server)

***

### level

> **level**: [`LogLevelString`](../type-aliases/LogLevelString.md)

Defined in: [logger.types.ts:84](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L84)

Log level

***

### message

> **message**: `string`

Defined in: [logger.types.ts:88](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L88)

Log message

***

### timestamp

> **timestamp**: `string`

Defined in: [logger.types.ts:82](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.types.ts#L82)

ISO timestamp of the log
