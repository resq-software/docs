# Interface: Cache\<D\>

Defined in: [memoize/memoize.types.ts:79](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize/memoize.types.ts#L79)

Interface for cache implementations used by the memoize decorator.

 Cache

## Example

```typescript
const cache: Cache<User> = {
  set: (key, value) => storage.set(key, value),
  get: (key) => storage.get(key),
  delete: (key) => storage.delete(key),
  has: (key) => storage.has(key)
};
```

## Type Parameters

### D

`D`

The type of values stored in the cache

## Properties

### delete

> **delete**: (`key`) => `void`

Defined in: [memoize/memoize.types.ts:85](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize/memoize.types.ts#L85)

Remove a value from the cache

#### Parameters

##### key

`string`

#### Returns

`void`

***

### get

> **get**: (`key`) => `D` \| `null` \| `undefined`

Defined in: [memoize/memoize.types.ts:83](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize/memoize.types.ts#L83)

Retrieve a value from the cache

#### Parameters

##### key

`string`

#### Returns

`D` \| `null` \| `undefined`

***

### has

> **has**: (`key`) => `boolean`

Defined in: [memoize/memoize.types.ts:87](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize/memoize.types.ts#L87)

Check if a key exists in the cache

#### Parameters

##### key

`string`

#### Returns

`boolean`

***

### set

> **set**: (`key`, `value`) => `void`

Defined in: [memoize/memoize.types.ts:81](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize/memoize.types.ts#L81)

Store a value in the cache

#### Parameters

##### key

`string`

##### value

`D`

#### Returns

`void`
