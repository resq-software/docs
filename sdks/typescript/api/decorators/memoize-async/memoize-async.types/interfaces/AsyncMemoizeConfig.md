# Interface: AsyncMemoizeConfig\<T, D\>

Defined in: [memoize-async/memoize-async.types.ts:93](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize-async/memoize-async.types.ts#L93)

Configuration for the `@memoizeAsync` decorator and memoizeAsyncFn. The
cache may be synchronous or asynchronous.

## Example

```ts
const config: AsyncMemoizeConfig<ApiService, User> = {
  cache: redisCache,
  keyResolver: (userId) => `user:${userId}`,
  expirationTimeMs: 300000,
};
```

## Type Parameters

### T

`T`

The class type a `keyof T` key resolver resolves against.

### D

`D`

The resolved type of the async method.

## Properties

### cache?

&gt; `optional` **cache?**: [`Cache`](../../../memoize/memoize.types/interfaces/Cache)\<`D`\> \| [`AsyncCache`](./AsyncCache)\<`D`\>

Defined in: [memoize-async/memoize-async.types.ts:98](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize-async/memoize-async.types.ts#L98)

Custom cache, synchronous ([Cache](../../../memoize/memoize.types/interfaces/Cache)) or asynchronous ([AsyncCache](./AsyncCache));
when omitted, a fresh `Map` is used.

***

### expirationTimeMs?

&gt; `optional` **expirationTimeMs?**: `number`

Defined in: [memoize-async/memoize-async.types.ts:109](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize-async/memoize-async.types.ts#L109)

Per-entry time-to-live in milliseconds, measured from insertion. When omitted,
entries never expire.

***

### keyResolver?

&gt; `optional` **keyResolver?**: [`KeyResolver`](../../../memoize/memoize.types/type-aliases/KeyResolver) \| keyof `T`

Defined in: [memoize-async/memoize-async.types.ts:104](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize-async/memoize-async.types.ts#L104)

How cache keys are derived. A [KeyResolver](../../../memoize/memoize.types/type-aliases/KeyResolver) is called with the
arguments; a `keyof T` names an instance method resolved and bound to `this`
at call time. When omitted, the key is `JSON.stringify` of the arguments.
