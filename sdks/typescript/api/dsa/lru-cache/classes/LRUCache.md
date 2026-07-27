# Class: LRUCache\<K, V\>

Defined in: [lru-cache.ts:106](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L106)

Least-recently-used cache with constant-time `get`, `set`, `has`, and
`delete`.

Implementation: `Map<K, Node>` for `O(1)` key lookup, paired with a
doubly-linked list ordered MRU → LRU. Every access moves the touched node
to the head so the tail is always the eviction candidate.

Optional TTL support is **lazy**: expired entries stay in memory until
the next access touches them, at which point they're removed and treated
as a miss. There is no background sweeper.

## Examples

**Basic use**

```ts
const cache = new LRUCache<string, User>({ maxSize: 100 });
cache.set("u:42", user);
cache.get("u:42"); // → User
```

**With TTL and eviction callback**

```ts
const cache = new LRUCache<string, Tile>({
  maxSize: 1024,
  defaultTTL: 60_000,
  onEvict: (key, value) => value.dispose(),
});
cache.set("tile:42:17", tile);              // uses defaultTTL
cache.set("tile:42:18", tile, 5_000);       // per-entry override (5s)
```

**Compute-on-miss**

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

&gt; **new LRUCache**\<`K`, `V`\>(`options`): `LRUCache`\<`K`, `V`\>

Defined in: [lru-cache.ts:117](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L117)

#### Parameters

##### options

[`LRUCacheOptions`](../interfaces/LRUCacheOptions)\<`K`, `V`\>

See [LRUCacheOptions](../interfaces/LRUCacheOptions). `maxSize` is required.

#### Returns

`LRUCache`\<`K`, `V`\>

## Accessors

### size

#### Get Signature

&gt; **get** **size**(): `number`

Defined in: [lru-cache.ts:244](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L244)

Current number of entries (including not-yet-evicted expired entries).

##### Returns

`number`

## Methods

### \[iterator\]()

&gt; **\[iterator\]**(): `Generator`\<\[`K`, `V`\]\>

Defined in: [lru-cache.ts:397](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L397)

Default iterator returning entries.

#### Returns

`Generator`\<\[`K`, `V`\]\>

***

### clear()

&gt; **clear**(): `void`

Defined in: [lru-cache.ts:237](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L237)

Drop every entry. `onEvict` is **not** called for any entry.

#### Returns

`void`

***

### delete()

&gt; **delete**(`key`): `boolean`

Defined in: [lru-cache.ts:225](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L225)

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

### entries()

&gt; **entries**(): `Generator`\<\[`K`, `V`\]\>

Defined in: [lru-cache.ts:383](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L383)

Iterate `[key, value]` pairs from most-recently-used to
least-recently-used. Skips (but does not evict) expired entries and leaves
LRU order untouched.

#### Returns

`Generator`\<\[`K`, `V`\]\>

***

### get()

&gt; **get**(`key`): `V` \| `undefined`

Defined in: [lru-cache.ts:133](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L133)

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

&gt; **getOrCompute**(`key`, `compute`, `ttl?`): `Promise`\<`V`\>

Defined in: [lru-cache.ts:271](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L271)

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

() =&gt; `Promise`\<`V`\>

Async loader called only on miss.

##### ttl?

`number`

Optional TTL applied to the freshly computed value.

#### Returns

`Promise`\<`V`\>

***

### getOrComputeSync()

&gt; **getOrComputeSync**(`key`, `compute`, `ttl?`): `V`

Defined in: [lru-cache.ts:287](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L287)

Synchronous variant of [getOrCompute](#getorcompute).

#### Parameters

##### key

`K`

Lookup key.

##### compute

() =&gt; `V`

Synchronous loader called only on miss.

##### ttl?

`number`

Optional TTL applied to the freshly computed value.

#### Returns

`V`

***

### getStats()

&gt; **getStats**(): `object`

Defined in: [lru-cache.ts:254](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L254)

Snapshot of cache statistics.

#### Returns

`object`

`{ size, maxSize, hitRate }`. **Note:** `hitRate` is reserved
  for a future implementation; it currently always returns `0`.

##### hitRate

&gt; **hitRate**: `number`

##### maxSize

&gt; **maxSize**: `number`

##### size

&gt; **size**: `number`

***

### has()

&gt; **has**(`key`): `boolean`

Defined in: [lru-cache.ts:202](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L202)

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

### keys()

&gt; **keys**(): `Generator`\<`K`\>

Defined in: [lru-cache.ts:352](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L352)

Iterate the keys from most-recently-used to least-recently-used.

Expired entries are skipped but — unlike [get](#get)/[has](#has) — **not**
evicted, so they still count toward [size](#size) until a keyed access
removes them. Iterating does not change LRU order.

#### Returns

`Generator`\<`K`\>

***

### set()

&gt; **set**(`key`, `value`, `ttl?`): `void`

Defined in: [lru-cache.ts:160](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L160)

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

***

### values()

&gt; **values**(): `Generator`\<`V`\>

Defined in: [lru-cache.ts:367](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/dsa/src/lru-cache.ts#L367)

Iterate the values from most-recently-used to least-recently-used.
Skips (but does not evict) expired entries and leaves LRU order untouched.

#### Returns

`Generator`\<`V`\>
