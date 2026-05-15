# Function: LogError()

> **LogError**(`options?`): `MethodDecorator`

Defined in: [logger.decorators.ts:182](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/logger/src/logger.decorators.ts#L182)

Decorator that wraps method in try/catch and logs errors.
Can optionally suppress the error or rethrow it.

## Parameters

### options?

[`LogErrorOptions`](../../logger.types/interfaces/LogErrorOptions) = `{}`

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
