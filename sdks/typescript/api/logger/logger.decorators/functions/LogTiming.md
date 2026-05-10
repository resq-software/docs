# Function: LogTiming()

> **LogTiming**(`options?`): `MethodDecorator`

Defined in: [logger.decorators.ts:122](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.decorators.ts#L122)

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
