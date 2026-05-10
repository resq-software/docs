# Interface: LRUCacheOptions

Defined in: [lru-cache.ts:32](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L32)

LRU Cache configuration

## Properties

### defaultTTL?

> `optional` **defaultTTL?**: `number`

Defined in: [lru-cache.ts:36](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L36)

Default TTL in milliseconds (optional)

***

### maxSize

> **maxSize**: `number`

Defined in: [lru-cache.ts:34](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L34)

Maximum number of items in cache

***

### onEvict?

> `optional` **onEvict?**: \<`K`, `V`\>(`key`, `value`) => `void`

Defined in: [lru-cache.ts:38](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L38)

Callback when item is evicted

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
