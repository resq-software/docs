# Interface: AsyncMemoizeConfig\<T, D\>

Defined in: [memoize-async/memoize-async.types.ts:81](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize-async/memoize-async.types.ts#L81)

Configuration options for the

## Memoize Async

decorator.

 AsyncMemoizeConfig

## Example

```typescript
const config: AsyncMemoizeConfig<ApiService, User> = {
  cache: redisCache,
  keyResolver: (userId) => `user:${userId}`,
  expirationTimeMs: 300000
};
```

## Type Parameters

### T

`T`

The type of the class containing the decorated method

### D

`D`

The resolved type of the async method

## Properties

### cache?

> `optional` **cache?**: [`Cache`](../../../memoize/memoize.types/interfaces/Cache)\<`D`\> \| [`AsyncCache`](./AsyncCache)\<`D`\>

Defined in: [memoize-async/memoize-async.types.ts:83](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize-async/memoize-async.types.ts#L83)

Custom cache implementation (sync or async)

***

### expirationTimeMs?

> `optional` **expirationTimeMs?**: `number`

Defined in: [memoize-async/memoize-async.types.ts:87](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize-async/memoize-async.types.ts#L87)

Time in milliseconds after which cached values expire

***

### keyResolver?

> `optional` **keyResolver?**: [`KeyResolver`](../../../memoize/memoize.types/type-aliases/KeyResolver) \| keyof `T`

Defined in: [memoize-async/memoize-async.types.ts:85](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize-async/memoize-async.types.ts#L85)

Function or method name for generating cache keys
