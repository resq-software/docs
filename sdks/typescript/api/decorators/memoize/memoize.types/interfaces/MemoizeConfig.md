# Interface: MemoizeConfig\<T, D\>

Defined in: [memoize/memoize.types.ts:109](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize/memoize.types.ts#L109)

Configuration options for the

## Memoize

decorator.

 MemoizeConfig

## Example

```typescript
const config: MemoizeConfig<MyService, User> = {
  cache: new LRUCache<string, User>(100),
  keyResolver: (id) => `user-${id}`,
  expirationTimeMs: 300000 // 5 minutes
};
```

## Type Parameters

### T

`T`

The type of the class containing the decorated method

### D

`D`

The return type of the decorated method

## Properties

### cache?

> `optional` **cache?**: [`Cache`](./Cache.md)\<`D`\>

Defined in: [memoize/memoize.types.ts:111](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize/memoize.types.ts#L111)

Custom cache implementation (defaults to Map)

***

### expirationTimeMs?

> `optional` **expirationTimeMs?**: `number`

Defined in: [memoize/memoize.types.ts:115](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize/memoize.types.ts#L115)

Time in milliseconds after which cached values expire

***

### keyResolver?

> `optional` **keyResolver?**: [`KeyResolver`](../type-aliases/KeyResolver.md) \| keyof `T`

Defined in: [memoize/memoize.types.ts:113](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize/memoize.types.ts#L113)

Function or method name for generating cache keys
