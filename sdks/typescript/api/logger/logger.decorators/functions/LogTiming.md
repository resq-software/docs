# Function: LogTiming()

&gt; **LogTiming**(`options?`): `MethodDecorator`

Defined in: [logger.decorators.ts:136](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.decorators.ts#L136)

Decorator that logs method execution time, useful for performance monitoring.
A log is emitted only when the measured duration meets or exceeds
[LogTimingOptions.threshold](../../logger.types/interfaces/LogTimingOptions#threshold).

Async calls are timed across the whole promise via `finally`, so their timing
logs even on rejection; a *synchronous* throw skips the timing log entirely
(the duration line never runs). The decorator neither catches nor rethrows —
errors propagate unchanged.

## Parameters

### options?

[`LogTimingOptions`](../../logger.types/interfaces/LogTimingOptions) = `{}`

Configuration options.

## Returns

`MethodDecorator`

The method decorator.

## Example

```ts
class DataService {
  @LogTiming({ threshold: 100 }) // Only log if execution > 100ms.
  async fetchData() {
    // ... slow operation
  }
}
```
