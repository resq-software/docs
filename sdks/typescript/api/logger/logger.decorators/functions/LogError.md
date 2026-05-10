# Function: LogError()

> **LogError**(`options?`): `MethodDecorator`

Defined in: [logger.decorators.ts:182](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.decorators.ts#L182)

Decorator that wraps method in try/catch and logs errors.
Can optionally suppress the error or rethrow it.

## Parameters

### options?

[`LogErrorOptions`](../../logger.types/interfaces/LogErrorOptions.md) = `{}`

Configuration options

## Returns

`MethodDecorator`

The decorator function

## Example

```typescript
class ApiService {
  @LogError({ rethrow: false, message: 'API call failed' })
  async callApi() {
    throw new Error('Network error');
  }
}
```
