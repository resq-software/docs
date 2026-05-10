# Function: LogClass()

> **LogClass**(`options?`): \<`T`\>(`target`) => `T`

Defined in: [logger.decorators.ts:246](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/logger/src/logger.decorators.ts#L246)

Class decorator that applies logging to all methods of a class.
Can be configured to exclude specific methods.

## Parameters

### options?

[`LogClassOptions`](../../logger.types/interfaces/LogClassOptions) = `{}`

Configuration options

## Returns

The decorator function

\<`T`\>(`target`) => `T`

## Example

```typescript
@LogClass({ exclude: ['privateMethod'], timing: true })
class MyService {
  publicMethod() { ... }
  privateMethod() { ... } // Won't be logged
}
```
