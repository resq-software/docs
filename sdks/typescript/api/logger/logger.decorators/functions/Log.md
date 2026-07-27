# Function: Log()

&gt; **Log**(`options?`): `MethodDecorator`

Defined in: [logger.decorators.ts:58](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/logger/src/logger.decorators.ts#L58)

Decorator that logs method entry and exit, optionally including the arguments
and return value. Async methods are awaited so completion and failure are
logged after the promise settles.

Failure logging is async-only: a rejected promise is logged as `failed` and
re-thrown, but a *synchronous* throw propagates without a failure log (the
entry log has already fired). The returned decorator replaces
`descriptor.value` in place; it does not preserve the original method's `length`.

## Parameters

### options?

[`LogMethodOptions`](../../logger.types/interfaces/LogMethodOptions) = `{}`

Configuration options.

## Returns

`MethodDecorator`

The method decorator.

## Example

```ts
class UserService {
  @Log({ logArgs: true, logResult: true })
  async getUser(id: string) {
    return { id, name: "John" };
  }
}
```
