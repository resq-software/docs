# Interface: BackoffOptions

Defined in: [backoff.ts:35](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/backoff.ts#L35)

## Properties

### factor?

&gt; `optional` **factor?**: `number`

Defined in: [backoff.ts:39](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/backoff.ts#L39)

Multiplier applied after each handed-out delay (default 2).

***

### initialDelayMs?

&gt; `optional` **initialDelayMs?**: `number`

Defined in: [backoff.ts:37](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/backoff.ts#L37)

First retry delay in ms (default 1000).

***

### maxDelayMs?

&gt; `optional` **maxDelayMs?**: `number`

Defined in: [backoff.ts:41](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/telemetry/src/backoff.ts#L41)

Upper bound for any single delay in ms (default 30000).
