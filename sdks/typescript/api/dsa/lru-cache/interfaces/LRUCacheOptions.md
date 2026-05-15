# Interface: LRUCacheOptions

Defined in: [lru-cache.ts:32](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L32)

Configuration for [LRUCache](../classes/LRUCache).

## Properties

### defaultTTL?

> `optional` **defaultTTL?**: `number`

Defined in: [lru-cache.ts:43](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L43)

Default time-to-live in milliseconds for entries inserted without a
per-call TTL. Omit for entries that never expire by time. Expired
entries are evicted **lazily** on the next `get`/`has` access.

***

### maxSize

> **maxSize**: `number`

Defined in: [lru-cache.ts:37](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L37)

Maximum number of entries the cache will hold. Once exceeded, the
least-recently-used entry is evicted.

***

### onEvict?

> `optional` **onEvict?**: \<`K`, `V`\>(`key`, `value`) => `void`

Defined in: [lru-cache.ts:51](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L51)

Optional callback invoked whenever an entry is evicted to make room
for a new one. Receives the key and value of the evicted entry.

Not called on explicit `delete()` or `clear()`, and not called when
an entry is removed because it expired.

#### Type Parameters

##### K

`K`

##### V

`V`

#### Parameters

##### key

`K`

##### value

`V`

#### Returns

`void`
