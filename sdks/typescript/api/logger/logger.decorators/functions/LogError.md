# Function: LogError()

&gt; **LogError**(`options?`): `MethodDecorator`

Defined in: [logger.decorators.ts:200](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/logger/src/logger.decorators.ts#L200)

Decorator that wraps a method in try/catch and logs any error, then either
rethrows it or swallows it (returning `undefined`) per
[LogErrorOptions.rethrow](../../logger.types/interfaces/LogErrorOptions#rethrow).

Both sync throws and async rejections are handled symmetrically. When
`rethrow` is `false` the error is suppressed and the call resolves to
`undefined` — for an async method that means a *resolved* promise, not a
rejected one, so callers lose the failure signal by design.

## Parameters

### options?

[`LogErrorOptions`](../../logger.types/interfaces/LogErrorOptions) = `{}`

Configuration options.

## Returns

`MethodDecorator`

The method decorator.

## Example

```ts
class ApiService {
  @LogError({ rethrow: false, message: "API call failed" })
  async callApi() {
    throw new Error("Network error");
  }
}
```
