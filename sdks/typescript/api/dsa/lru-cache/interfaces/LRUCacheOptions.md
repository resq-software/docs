# Interface: LRUCacheOptions\<K, V\>

Defined in: [lru-cache.ts:41](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L41)

Configuration for [LRUCache](../classes/LRUCache).

## Type Parameters

### K

`K` = `unknown`

### V

`V` = `unknown`

## Properties

### defaultTTL?

&gt; `optional` **defaultTTL?**: `number`

Defined in: [lru-cache.ts:52](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L52)

Default time-to-live in milliseconds for entries inserted without a
per-call TTL. Omit for entries that never expire by time. Expired
entries are evicted **lazily** on the next `get`/`has` access.

***

### maxSize

&gt; **maxSize**: `number`

Defined in: [lru-cache.ts:46](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L46)

Maximum number of entries the cache will hold. Once exceeded, the
least-recently-used entry is evicted.

***

### onEvict?

&gt; `optional` **onEvict?**: (`key`, `value`) =&gt; `void`

Defined in: [lru-cache.ts:60](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L60)

Optional callback invoked whenever an entry is evicted to make room
for a new one. Receives the key and value of the evicted entry.

Not called on explicit `delete()` or `clear()`, and not called when
an entry is removed because it expired.

#### Parameters

##### key

`K`

##### value

`V`

#### Returns

`void`
