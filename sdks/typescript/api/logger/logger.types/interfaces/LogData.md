# Interface: LogData

Defined in: [logger.types.ts:38](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/logger.types.ts#L38)

Structured data attached to a log message — an open bag of key-value pairs.

Values should be JSON-serializable: the console formatter and
JsonTransport render this bag via `JSON.stringify`, and a value that
cannot be stringified (circular references, `BigInt`, …) is replaced with an
unserializable marker rather than throwing. Keys are not namespaced, so a
caller-supplied `error` key collides with the one [Logger.error](../../logger/classes/Logger#error) injects.

## Indexable

&gt; \[`key`: `string`\]: `unknown`

Arbitrary key-value pairs to include in the log.
