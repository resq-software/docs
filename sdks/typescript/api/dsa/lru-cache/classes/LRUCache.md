# Class: LRUCache\<K, V\>

Defined in: [lru-cache.ts:93](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L93)

Least-recently-used cache with constant-time `get`, `set`, `has`, and
`delete`.

Implementation: `Map<K, Node>` for `O(1)` key lookup, paired with a
doubly-linked list ordered MRU → LRU. Every access moves the touched node
to the head so the tail is always the eviction candidate.

Optional TTL support is **lazy**: expired entries stay in memory until
the next access touches them, at which point they're removed and treated
as a miss. There is no background sweeper.

## Examples

```ts
const cache = new LRUCache<string, User>({ maxSize: 100 });
cache.set("u:42", user);
cache.get("u:42"); // → User
```

```ts
const cache = new LRUCache<string, Tile>({
  maxSize: 1024,
  defaultTTL: 60_000,
  onEvict: (key, value) => value.dispose(),
});
cache.set("tile:42:17", tile);              // uses defaultTTL
cache.set("tile:42:18", tile, 5_000);       // per-entry override (5s)
```

```ts
const user = await cache.getOrCompute("u:42", () => fetchUser(42));
```

## Type Parameters

### K

`K`

Key type. Compared by `Map` semantics (SameValueZero).

### V

`V`

Value type. The cache stores references — it does not
  copy or freeze values.

## Constructors

### Constructor

> **new LRUCache**\<`K`, `V`\>(`options`): `LRUCache`\<`K`, `V`\>

Defined in: [lru-cache.ts:104](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L104)

#### Parameters

##### options

[`LRUCacheOptions`](../interfaces/LRUCacheOptions)

See [LRUCacheOptions](../interfaces/LRUCacheOptions). `maxSize` is required.

#### Returns

`LRUCache`\<`K`, `V`\>

## Accessors

### size

#### Get Signature

> **get** **size**(): `number`

Defined in: [lru-cache.ts:231](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L231)

Current number of entries (including not-yet-evicted expired entries).

##### Returns

`number`

## Methods

### clear()

> **clear**(): `void`

Defined in: [lru-cache.ts:224](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L224)

Drop every entry. `onEvict` is **not** called for any entry.

#### Returns

`void`

***

### delete()

> **delete**(`key`): `boolean`

Defined in: [lru-cache.ts:212](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L212)

Remove an entry by key.

#### Parameters

##### key

`K`

#### Returns

`boolean`

`true` if a matching entry was found and removed, `false`
  otherwise.

Note: does **not** invoke `onEvict` — that callback is reserved for
capacity-driven eviction.

Time complexity: `O(1)`.

***

### get()

> **get**(`key`): `V` \| `undefined`

Defined in: [lru-cache.ts:120](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L120)

Look up a value and mark its entry as most-recently-used.

#### Parameters

##### key

`K`

Lookup key.

#### Returns

`V` \| `undefined`

The stored value, or `undefined` if the key is absent or
  the entry has expired (in which case it is also evicted).

Time complexity: `O(1)`.

***

### getOrCompute()

> **getOrCompute**(`key`, `compute`, `ttl?`): `Promise`\<`V`\>

Defined in: [lru-cache.ts:258](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L258)

Read-through helper: return the cached value, or call `compute` to
load it on miss and cache the result.

Concurrent calls with the same key may invoke `compute` more than
once — this method does **not** deduplicate in-flight loads. If
single-flight semantics matter, wrap `compute` in your own
promise-deduper or use a memoising decorator.

#### Parameters

##### key

`K`

Lookup key.

##### compute

() => `Promise`\<`V`\>

Async loader called only on miss.

##### ttl?

`number`

Optional TTL applied to the freshly computed value.

#### Returns

`Promise`\<`V`\>

***

### getOrComputeSync()

> **getOrComputeSync**(`key`, `compute`, `ttl?`): `V`

Defined in: [lru-cache.ts:274](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L274)

Synchronous variant of [getOrCompute](#getorcompute).

#### Parameters

##### key

`K`

Lookup key.

##### compute

() => `V`

Synchronous loader called only on miss.

##### ttl?

`number`

Optional TTL applied to the freshly computed value.

#### Returns

`V`

***

### getStats()

> **getStats**(): `object`

Defined in: [lru-cache.ts:241](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L241)

Snapshot of cache statistics.

#### Returns

`object`

`{ size, maxSize, hitRate }`. **Note:** `hitRate` is reserved
  for a future implementation; it currently always returns `0`.

##### hitRate

> **hitRate**: `number`

##### maxSize

> **maxSize**: `number`

##### size

> **size**: `number`

***

### has()

> **has**(`key`): `boolean`

Defined in: [lru-cache.ts:189](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L189)

Membership test. Does **not** affect LRU order.

#### Parameters

##### key

`K`

#### Returns

`boolean`

`true` if `key` has a non-expired entry. Expired entries
  are evicted as a side effect and return `false`.

Time complexity: `O(1)`.

***

### set()

> **set**(`key`, `value`, `ttl?`): `void`

Defined in: [lru-cache.ts:147](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/dsa/src/lru-cache.ts#L147)

Insert or replace an entry. Becomes the most-recently-used entry.

If inserting causes `size` to exceed `maxSize`, the least-recently-used
entry is evicted and [onEvict](../interfaces/LRUCacheOptions#onevict) fires.

#### Parameters

##### key

`K`

Entry key.

##### value

`V`

Entry value.

##### ttl?

`number`

Optional per-call TTL in milliseconds. Overrides
  [defaultTTL](../interfaces/LRUCacheOptions#defaultttl). Omit for "never
  expire by time" (default if no `defaultTTL` is set).

Time complexity: `O(1)`.

#### Returns

`void`
