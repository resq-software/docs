# Function: LogTiming()

> **LogTiming**(`options?`): `MethodDecorator`

Defined in: [logger.decorators.ts:122](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.decorators.ts#L122)

Decorator that logs method execution time.
Useful for performance monitoring.

## Parameters

### options?

[`LogTimingOptions`](../../logger.types/interfaces/LogTimingOptions) = `{}`

Configuration options

## Returns

`MethodDecorator`

The decorator function

## Example

```typescript
class DataService {
  @LogTiming({ threshold: 100 }) // Only log if execution > 100ms
  async fetchData() {
    // ... slow operation
  }
}
```
