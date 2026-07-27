# Interface: LogMethodOptions

Defined in: [logger.types.ts:154](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L154)

Options for the `@Log` decorator.

## Properties

### level?

&gt; `optional` **level?**: [`SimpleLogLevel`](../type-aliases/SimpleLogLevel)

Defined in: [logger.types.ts:162](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L162)

Log level to use (default: `"debug"`); `"error"` is excluded — see [SimpleLogLevel](../type-aliases/SimpleLogLevel).

***

### logArgs?

&gt; `optional` **logArgs?**: `boolean`

Defined in: [logger.types.ts:156](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L156)

Whether to log method arguments (default: `true`).

***

### logResult?

&gt; `optional` **logResult?**: `boolean`

Defined in: [logger.types.ts:158](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L158)

Whether to log the return value (default: `false`).

***

### message?

&gt; `optional` **message?**: `string`

Defined in: [logger.types.ts:160](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.types.ts#L160)

Custom message prefix.
