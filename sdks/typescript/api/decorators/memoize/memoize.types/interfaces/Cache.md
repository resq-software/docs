# Interface: Cache\<D\>

Defined in: [memoize/memoize.types.ts:66](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize/memoize.types.ts#L66)

Cache contract used by the `@memoize` decorator. Any store with these four
synchronous operations (a plain `Map`, an LRU, etc.) can back the cache.

`has` is the authority on presence, not `get`: a stored value may legitimately
be `null`/`undefined`, so `memoize` calls `has` first and only then `get`. An
implementation must therefore keep the two consistent for the same key. All
four operations share one keyspace and run synchronously (use
AsyncCache for a promise-based store).

## Example

```ts
const cache: Cache<User> = {
  set: (key, value) => storage.set(key, value),
  get: (key) => storage.get(key),
  delete: (key) => storage.delete(key),
  has: (key) => storage.has(key),
};
```

## Type Parameters

### D

`D`

The type of values stored in the cache.

## Properties

### delete

&gt; **delete**: (`key`) =&gt; `void`

Defined in: [memoize/memoize.types.ts:75](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize/memoize.types.ts#L75)

Remove the entry for `key`; a no-op when the key is absent.

#### Parameters

##### key

`string`

#### Returns

`void`

***

### get

&gt; **get**: (`key`) =&gt; `D` \| `null` \| `undefined`

Defined in: [memoize/memoize.types.ts:73](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize/memoize.types.ts#L73)

Retrieve a value for `key`. A `null`/`undefined` result is ambiguous — it may
be an absent key or a stored nullish value — so callers must gate on `has`.

#### Parameters

##### key

`string`

#### Returns

`D` \| `null` \| `undefined`

***

### has

&gt; **has**: (`key`) =&gt; `boolean`

Defined in: [memoize/memoize.types.ts:77](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize/memoize.types.ts#L77)

Whether an entry exists for `key`; the authoritative presence check.

#### Parameters

##### key

`string`

#### Returns

`boolean`

***

### set

&gt; **set**: (`key`, `value`) =&gt; `void`

Defined in: [memoize/memoize.types.ts:68](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize/memoize.types.ts#L68)

Store a value in the cache, overwriting any existing entry for `key`.

#### Parameters

##### key

`string`

##### value

`D`

#### Returns

`void`
