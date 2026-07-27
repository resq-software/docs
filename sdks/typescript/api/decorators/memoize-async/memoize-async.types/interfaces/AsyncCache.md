# Interface: AsyncCache\<D\>

Defined in: [memoize-async/memoize-async.types.ts:67](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize-async/memoize-async.types.ts#L67)

Async cache contract used by the `@memoizeAsync` decorator. Any store exposing
these four promise-returning operations (e.g. a Redis-backed cache) qualifies.

`get` must resolve `null` for an absent key: `memoizeAsync` distinguishes hit
from miss with a single `get` (never a separate `has` + `get`) to stay race-free
against TTL eviction, so a nullish resolution is read as "not cached". A value
that is itself `null`/`undefined` therefore cannot be cached and is recomputed
each call. All operations share one keyspace.

## Example

```ts
const redisCache: AsyncCache<User> = {
  set: async (key, value) => await redis.set(key, JSON.stringify(value)),
  get: async (key) => {
    const data = await redis.get(key);
    return data ? JSON.parse(data) : null;
  },
  delete: async (key) => await redis.del(key),
  has: async (key) => (await redis.exists(key)) > 0,
};
```

## Type Parameters

### D

`D`

The type of values stored in the cache.

## Properties

### delete

&gt; **delete**: (`key`) =&gt; `Promise`\<`void`\>

Defined in: [memoize-async/memoize-async.types.ts:73](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize-async/memoize-async.types.ts#L73)

Remove the entry for `key`; resolves regardless of prior presence.

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`void`\>

***

### get

&gt; **get**: (`key`) =&gt; `Promise`\<`D` \| `null`\>

Defined in: [memoize-async/memoize-async.types.ts:71](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize-async/memoize-async.types.ts#L71)

Retrieve the value for `key`, resolving `null` when the key is absent.

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`D` \| `null`\>

***

### has

&gt; **has**: (`key`) =&gt; `Promise`\<`boolean`\>

Defined in: [memoize-async/memoize-async.types.ts:75](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize-async/memoize-async.types.ts#L75)

Whether an entry exists for `key`. Not used on the `memoizeAsync` hot path.

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`boolean`\>

***

### set

&gt; **set**: (`key`, `value`) =&gt; `Promise`\<`void`\>

Defined in: [memoize-async/memoize-async.types.ts:69](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize-async/memoize-async.types.ts#L69)

Store a value for `key`, overwriting any existing entry.

#### Parameters

##### key

`string`

##### value

`D`

#### Returns

`Promise`\<`void`\>
