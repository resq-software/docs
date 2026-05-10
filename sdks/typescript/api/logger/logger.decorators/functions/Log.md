# Function: Log()

> **Log**(`options?`): `MethodDecorator`

Defined in: [logger.decorators.ts:47](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.decorators.ts#L47)

Decorator that logs method entry and exit.
Can optionally log arguments and return values.

## Parameters

### options?

[`LogMethodOptions`](../../logger.types/interfaces/LogMethodOptions) = `{}`

Configuration options

## Returns

`MethodDecorator`

The decorator function

## Example

```typescript
class UserService {
  @Log({ logArgs: true, logResult: true })
  async getUser(id: string) {
    return { id, name: 'John' };
  }
}
```
