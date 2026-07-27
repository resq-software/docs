# Interface: LoggerOptions

Defined in: [logger.types.ts:51](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/logger.types.ts#L51)

Configuration options for a [Logger](../../logger/classes/Logger) instance.

Only [LoggerOptions.minLevel](#minlevel) currently influences behavior; the
remaining fields are accepted but not yet applied by the console formatter —
timestamps are always emitted and output is never colorized regardless of what
is passed. Treat the formatting/file fields as reserved surface.

## Properties

### colorize?

&gt; `optional` **colorize?**: `boolean`

Defined in: [logger.types.ts:61](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/logger.types.ts#L61)

Reserved: console output is not currently colorized.

***

### filePath?

&gt; `optional` **filePath?**: `string`

Defined in: [logger.types.ts:65](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/logger.types.ts#L65)

Reserved: only meaningful alongside [LoggerOptions.logToFile](#logtofile).

***

### includeTimestamp?

&gt; `optional` **includeTimestamp?**: `boolean`

Defined in: [logger.types.ts:59](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/logger.types.ts#L59)

Reserved: timestamps are currently emitted unconditionally.

***

### logToFile?

&gt; `optional` **logToFile?**: `boolean`

Defined in: [logger.types.ts:63](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/logger.types.ts#L63)

Reserved: file output is not currently implemented (server-side intent).

***

### minLevel?

&gt; `optional` **minLevel?**: [`LogLevel`](../../logger/enumerations/LogLevel)

Defined in: [logger.types.ts:57](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/logger.types.ts#L57)

Minimum level a message must meet to be emitted. When omitted, the
constructor falls back to the `LOG_LEVEL`/`BUN_LOG_LEVEL` env var, then to a
`NODE_ENV`-based default (`ERROR` in production, `ALL` otherwise).
