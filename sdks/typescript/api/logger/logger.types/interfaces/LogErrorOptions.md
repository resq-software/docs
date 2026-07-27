# Interface: LogErrorOptions

Defined in: [logger.types.ts:180](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L180)

Options for the `@LogError` decorator.

## Properties

### includeStack?

&gt; `optional` **includeStack?**: `boolean`

Defined in: [logger.types.ts:186](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L186)

Whether to log the stack trace (default: `true`).

***

### message?

&gt; `optional` **message?**: `string`

Defined in: [logger.types.ts:184](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L184)

Custom error message prefix.

***

### rethrow?

&gt; `optional` **rethrow?**: `boolean`

Defined in: [logger.types.ts:182](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L182)

Whether to rethrow the error after logging (default: `true`).
