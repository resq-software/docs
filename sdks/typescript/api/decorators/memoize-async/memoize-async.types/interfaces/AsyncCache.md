# Interface: AsyncCache\<D\>

Defined in: [memoize-async/memoize-async.types.ts:51](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize-async/memoize-async.types.ts#L51)

Interface for async cache implementations used by the memoizeAsync decorator.

 AsyncCache

## Example

```typescript
const redisCache: AsyncCache<User> = {
  set: async (key, value) => await redis.set(key, JSON.stringify(value)),
  get: async (key) => {
    const data = await redis.get(key);
    return data ? JSON.parse(data) : null;
  },
  delete: async (key) => await redis.del(key),
  has: async (key) => await redis.exists(key) > 0
};
```

## Type Parameters

### D

`D`

The type of values stored in the cache

## Properties

### delete

> **delete**: (`key`) => `Promise`\<`void`\>

Defined in: [memoize-async/memoize-async.types.ts:57](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize-async/memoize-async.types.ts#L57)

Remove a value from the cache asynchronously

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`void`\>

***

### get

> **get**: (`key`) => `Promise`\<`D`\> \| `Promise`\<`null`\>

Defined in: [memoize-async/memoize-async.types.ts:55](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize-async/memoize-async.types.ts#L55)

Retrieve a value from the cache asynchronously

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`D`\> \| `Promise`\<`null`\>

***

### has

> **has**: (`key`) => `Promise`\<`boolean`\>

Defined in: [memoize-async/memoize-async.types.ts:59](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize-async/memoize-async.types.ts#L59)

Check if a key exists in the cache asynchronously

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`boolean`\>

***

### set

> **set**: (`key`, `value`) => `Promise`\<`void`\>

Defined in: [memoize-async/memoize-async.types.ts:53](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize-async/memoize-async.types.ts#L53)

Store a value in the cache asynchronously

#### Parameters

##### key

`string`

##### value

`D`

#### Returns

`Promise`\<`void`\>
