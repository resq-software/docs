# Class: Logger

Defined in: [logger.ts:111](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L111)

A versatile logging utility that works in both browser and Node.js environments.
Supports multiple log levels, colorized output, and structured data logging.

## Constructors

### Constructor

> **new Logger**(`context`, `options?`): `Logger`

Defined in: [logger.ts:152](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L152)

Create a new Logger instance or return an existing one for the given context

#### Parameters

##### context

`string`

The context name for this logger (e.g., component or service name)

##### options?

[`LoggerOptions`](../interfaces/LoggerOptions.md) = `{}`

Optional logger configuration

#### Returns

`Logger`

## Methods

### action()

> **action**(`message`, `data?`): `void`

Defined in: [logger.ts:308](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L308)

Log an action message (for server actions or important user interactions)

#### Parameters

##### message

`string`

The action message

##### data?

[`LogData`](../interfaces/LogData.md)

Optional data to include

#### Returns

`void`

***

### debug()

> **debug**(`message`, `data?`): `void`

Defined in: [logger.ts:286](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L286)

Log a debug message

#### Parameters

##### message

`string`

The debug message

##### data?

[`LogData`](../interfaces/LogData.md)

Optional data to include

#### Returns

`void`

***

### error()

> **error**(`message`, `error?`, `data?`): `void`

Defined in: [logger.ts:255](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L255)

Log an error message

#### Parameters

##### message

`string`

The error message

##### error?

`unknown`

Optional Error object or unknown error

##### data?

[`LogData`](../interfaces/LogData.md)

Optional additional data

#### Returns

`void`

***

### group()

> **group**(`label`): `void`

Defined in: [logger.ts:329](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L329)

Group related log messages (console.group wrapper)

#### Parameters

##### label

`string`

The group label

#### Returns

`void`

***

### groupEnd()

> **groupEnd**(): `void`

Defined in: [logger.ts:337](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L337)

End a log group (console.groupEnd wrapper)

#### Returns

`void`

***

### info()

> **info**(`message`, `data?`): `void`

Defined in: [logger.ts:243](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L243)

Log an informational message

#### Parameters

##### message

`string`

The message to log

##### data?

[`LogData`](../interfaces/LogData.md)

Optional data to include

#### Returns

`void`

***

### success()

> **success**(`message`, `data?`): `void`

Defined in: [logger.ts:319](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L319)

Log a success message

#### Parameters

##### message

`string`

The success message

##### data?

[`LogData`](../interfaces/LogData.md)

Optional data to include

#### Returns

`void`

***

### time()

> **time**\<`T`\>(`label`, `fn`): `Promise`\<`T`\>

Defined in: [logger.ts:350](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L350)

Log execution time of a function

#### Type Parameters

##### T

`T`

The return type of the function being timed

#### Parameters

##### label

`string`

Description of the operation being timed

##### fn

() => `T` \| `Promise`\<`T`\>

Function to execute and time

#### Returns

`Promise`\<`T`\>

The result of the function execution

***

### trace()

> **trace**(`message`, `data?`): `void`

Defined in: [logger.ts:297](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L297)

Log a trace message (most verbose level)

#### Parameters

##### message

`string`

The trace message

##### data?

[`LogData`](../interfaces/LogData.md)

Optional data to include

#### Returns

`void`

***

### warn()

> **warn**(`message`, `data?`): `void`

Defined in: [logger.ts:275](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L275)

Log a warning message

#### Parameters

##### message

`string`

The warning message

##### data?

[`LogData`](../interfaces/LogData.md)

Optional data to include

#### Returns

`void`

***

### getLogger()

> `static` **getLogger**(`context`, `options?`): `Logger`

Defined in: [logger.ts:173](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L173)

Get a logger instance for the given context.
If a logger with this context already exists, returns the existing instance.

#### Parameters

##### context

`string`

The context name

##### options?

[`LoggerOptions`](../interfaces/LoggerOptions.md)

Optional logger configuration

#### Returns

`Logger`

A logger instance for the specified context

***

### setGlobalLogLevel()

> `static` **setGlobalLogLevel**(`level`): `void`

Defined in: [logger.ts:189](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.ts#L189)

Set global minimum log level for all logger instances

#### Parameters

##### level

[`LogLevel`](../enumerations/LogLevel.md)

The minimum level to log across all loggers

#### Returns

`void`
