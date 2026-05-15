# Interface: LogErrorOptions

Defined in: [logger.types.ts:138](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.types.ts#L138)

Options for the

## Log Error

decorator

## Properties

### includeStack?

> `optional` **includeStack?**: `boolean`

Defined in: [logger.types.ts:144](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.types.ts#L144)

Whether to log the stack trace (default: true)

***

### message?

> `optional` **message?**: `string`

Defined in: [logger.types.ts:142](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.types.ts#L142)

Custom error message prefix

***

### rethrow?

> `optional` **rethrow?**: `boolean`

Defined in: [logger.types.ts:140](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.types.ts#L140)

Whether to rethrow the error after logging (default: true)
