# Interface: LogEntry

Defined in: [logger.types.ts:80](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.types.ts#L80)

Structured log entry for transport/storage

## Properties

### context

> **context**: `string`

Defined in: [logger.types.ts:86](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.types.ts#L86)

Logger context/category

***

### data?

> `optional` **data?**: [`LogData`](./LogData)

Defined in: [logger.types.ts:90](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.types.ts#L90)

Optional structured data

***

### environment

> **environment**: `"client"` \| `"server"`

Defined in: [logger.types.ts:92](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.types.ts#L92)

Environment (client/server)

***

### level

> **level**: [`LogLevelString`](../type-aliases/LogLevelString)

Defined in: [logger.types.ts:84](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.types.ts#L84)

Log level

***

### message

> **message**: `string`

Defined in: [logger.types.ts:88](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.types.ts#L88)

Log message

***

### timestamp

> **timestamp**: `string`

Defined in: [logger.types.ts:82](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.types.ts#L82)

ISO timestamp of the log
