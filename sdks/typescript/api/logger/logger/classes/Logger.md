# Class: Logger

Defined in: [logger.ts:73](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L73)

A versatile logging utility that works in both browser and Node.js environments.
Supports multiple log levels, colorized output, and structured data logging.

## Constructors

### Constructor

&gt; **new Logger**(`context`, `options?`): `Logger`

Defined in: [logger.ts:135](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L135)

Create a new logger for the given context. Prefer [Logger.getLogger](#getlogger)
to reuse a shared instance per context.

#### Parameters

##### context

`string`

The context name for this logger (e.g. component or service name).

##### options?

[`LoggerOptions`](../../logger.types/interfaces/LoggerOptions) = `{}`

Optional logger configuration.

#### Returns

`Logger`

## Methods

### action()

&gt; **action**(`message`, `data?`): `void`

Defined in: [logger.ts:407](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L407)

Log an action message (for server actions or important user interactions).

#### Parameters

##### message

`string`

The action message.

##### data?

[`LogData`](../../logger.types/interfaces/LogData)

Optional structured data to include.

#### Returns

`void`

***

### debug()

&gt; **debug**(`message`, `data?`): `void`

Defined in: [logger.ts:385](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L385)

Log a debug message.

#### Parameters

##### message

`string`

The debug message.

##### data?

[`LogData`](../../logger.types/interfaces/LogData)

Optional structured data to include.

#### Returns

`void`

***

### error()

&gt; **error**(`message`, `error?`, `data?`): `void`

Defined in: [logger.ts:354](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L354)

Log an error message. An `Error` value is flattened to `{ name, message,
stack &#125;` (falling back to `error.cause.message` when the top-level message
is empty) before being attached under `data.error`.

#### Parameters

##### message

`string`

The error message.

##### error?

`unknown`

Optional `Error` or otherwise-unknown error value.

##### data?

[`LogData`](../../logger.types/interfaces/LogData)

Optional additional structured data.

#### Returns

`void`

***

### group()

&gt; **group**(`label`): `void`

Defined in: [logger.ts:428](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L428)

Open a console group for related log messages (a `console.group` wrapper).

#### Parameters

##### label

`string`

The group label.

#### Returns

`void`

***

### groupEnd()

&gt; **groupEnd**(): `void`

Defined in: [logger.ts:436](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L436)

Close the current console group (a `console.groupEnd` wrapper).

#### Returns

`void`

***

### info()

&gt; **info**(`message`, `data?`): `void`

Defined in: [logger.ts:340](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L340)

Log an informational message.

#### Parameters

##### message

`string`

The message to log.

##### data?

[`LogData`](../../logger.types/interfaces/LogData)

Optional structured data to include.

#### Returns

`void`

***

### success()

&gt; **success**(`message`, `data?`): `void`

Defined in: [logger.ts:418](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L418)

Log a success message.

#### Parameters

##### message

`string`

The success message.

##### data?

[`LogData`](../../logger.types/interfaces/LogData)

Optional structured data to include.

#### Returns

`void`

***

### time()

&gt; **time**\<`T`\>(`label`, `fn`): `Promise`\<`T`\>

Defined in: [logger.ts:456](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L456)

Run a function and log how long it took. Below `DEBUG` level the timing is
skipped and the function is still invoked. On failure the elapsed time is
logged via [Logger.error](#error) and the error is rethrown.

Failure is surfaced as a rejected `Promise`: whatever `fn` throws or rejects
with is re-thrown unchanged after the elapsed time is logged. There is no
cancellation hook — `fn` runs to completion.

#### Type Parameters

##### T

`T`

The value the timed function resolves to (its return type).

#### Parameters

##### label

`string`

Description of the operation being timed.

##### fn

() =&gt; `T` \| `Promise`\<`T`\>

Function to execute and time; may be sync or async.

#### Returns

`Promise`\<`T`\>

The resolved result of the function execution.

#### Throws

The exact error `fn` threw or rejected with, re-thrown after logging.

***

### trace()

&gt; **trace**(`message`, `data?`): `void`

Defined in: [logger.ts:396](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L396)

Log a trace message (the most verbose level).

#### Parameters

##### message

`string`

The trace message.

##### data?

[`LogData`](../../logger.types/interfaces/LogData)

Optional structured data to include.

#### Returns

`void`

***

### warn()

&gt; **warn**(`message`, `data?`): `void`

Defined in: [logger.ts:374](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L374)

Log a warning message.

#### Parameters

##### message

`string`

The warning message.

##### data?

[`LogData`](../../logger.types/interfaces/LogData)

Optional structured data to include.

#### Returns

`void`

***

### addTransport()

&gt; `static` **addTransport**(`transport`): () =&gt; `void`

Defined in: [logger.ts:214](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L214)

Register a [LogTransport](../../logger.types/interfaces/LogTransport) to receive a structured [LogEntry](../../logger.types/interfaces/LogEntry) for
every log emitted by any logger instance (after level filtering).

Mutates the process-global transport registry shared by all `Logger`
instances. Idempotent by identity: re-adding the same reference is a no-op
(but a distinct object with the same `name` *is* added again). Calling the
returned unsubscribe more than once is safe.

#### Parameters

##### transport

[`LogTransport`](../../logger.types/interfaces/LogTransport)

The transport to add. A transport already present (by
  identity) is not added twice.

#### Returns

An unsubscribe function that removes this transport.

() =&gt; `void`

#### Example

```ts
const off = Logger.addTransport(new MemoryTransport());
// ... later
off();
```

***

### clearTransports()

&gt; `static` **clearTransports**(): `void`

Defined in: [logger.ts:242](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L242)

Remove every registered transport.

#### Returns

`void`

***

### getLogger()

&gt; `static` **getLogger**(`context`, `options?`): `Logger`

Defined in: [logger.ts:161](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L161)

Get the shared logger instance for the given context, creating it on first
use. Subsequent calls with the same context return the same instance, so
`options` is honoured only on creation.

On first use for a context this mutates the process-global instance
registry; the cached instance then lives for the process lifetime.

#### Parameters

##### context

`string`

The context name.

##### options?

[`LoggerOptions`](../../logger.types/interfaces/LoggerOptions)

Optional logger configuration, applied only when creating.

#### Returns

`Logger`

The logger instance for the specified context.

***

### getTransports()

&gt; `static` **getTransports**(): readonly [`LogTransport`](../../logger.types/interfaces/LogTransport)[]

Defined in: [logger.ts:247](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L247)

A read-only snapshot of the currently-registered transports.

#### Returns

readonly [`LogTransport`](../../logger.types/interfaces/LogTransport)[]

***

### removeTransport()

&gt; `static` **removeTransport**(`transport`): `void`

Defined in: [logger.ts:232](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L232)

Remove a previously-registered transport, matched by identity or by its
`name`. No-op if it is not registered.

Mutates the process-global transport registry. When matching by `name` and
several transports share it, only the first match is removed.

#### Parameters

##### transport

`string` \| [`LogTransport`](../../logger.types/interfaces/LogTransport)

The transport instance to remove, or the `name` to match.

#### Returns

`void`

***

### setGlobalLogLevel()

&gt; `static` **setGlobalLogLevel**(`level`): `void`

Defined in: [logger.ts:181](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.ts#L181)

Set the global minimum log level across every existing logger instance.

Mutates the `minLevel` of every logger currently in the registry. Instances
created *after* this call are unaffected and resolve their own level from
options/env as usual — this is a one-shot sweep, not a persistent floor.

#### Parameters

##### level

[`LogLevel`](../enumerations/LogLevel)

The minimum level to log across all loggers.

#### Returns

`void`
