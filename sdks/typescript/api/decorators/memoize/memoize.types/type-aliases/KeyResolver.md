# Type Alias: KeyResolver

> **KeyResolver** = (...`args`) => `string`

Defined in: [memoize/memoize.types.ts:57](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize/memoize.types.ts#L57)

Function type for resolving cache keys from method arguments.

## Parameters

### args

...`unknown`[]

The method arguments

## Returns

`string`

The cache key string

## Example

```typescript
const keyResolver: KeyResolver = (userId, includeDetails) => {
  return `${userId}-${includeDetails}`;
};
```
