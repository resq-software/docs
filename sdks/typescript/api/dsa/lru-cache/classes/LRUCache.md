# Class: LRUCache\<K, V\>

Defined in: [lru-cache.ts:48](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L48)

High-performance LRU Cache with O(1) get/set operations

 LRUCache

## Type Parameters

### K

`K`

Key type

### V

`V`

Value type

## Constructors

### Constructor

> **new LRUCache**\<`K`, `V`\>(`options`): `LRUCache`\<`K`, `V`\>

Defined in: [lru-cache.ts:56](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L56)

#### Parameters

##### options

[`LRUCacheOptions`](../interfaces/LRUCacheOptions)

#### Returns

`LRUCache`\<`K`, `V`\>

## Accessors

### size

#### Get Signature

> **get** **size**(): `number`

Defined in: [lru-cache.ts:137](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L137)

##### Returns

`number`

## Methods

### clear()

> **clear**(): `void`

Defined in: [lru-cache.ts:131](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L131)

#### Returns

`void`

***

### delete()

> **delete**(`key`): `boolean`

Defined in: [lru-cache.ts:122](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L122)

#### Parameters

##### key

`K`

#### Returns

`boolean`

***

### get()

> **get**(`key`): `V` \| `undefined`

Defined in: [lru-cache.ts:63](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L63)

#### Parameters

##### key

`K`

#### Returns

`V` \| `undefined`

***

### getOrCompute()

> **getOrCompute**(`key`, `compute`, `ttl?`): `Promise`\<`V`\>

Defined in: [lru-cache.ts:145](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L145)

#### Parameters

##### key

`K`

##### compute

() => `Promise`\<`V`\>

##### ttl?

`number`

#### Returns

`Promise`\<`V`\>

***

### getOrComputeSync()

> **getOrComputeSync**(`key`, `compute`, `ttl?`): `V`

Defined in: [lru-cache.ts:154](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L154)

#### Parameters

##### key

`K`

##### compute

() => `V`

##### ttl?

`number`

#### Returns

`V`

***

### getStats()

> **getStats**(): `object`

Defined in: [lru-cache.ts:141](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L141)

#### Returns

`object`

##### hitRate

> **hitRate**: `number`

##### maxSize

> **maxSize**: `number`

##### size

> **size**: `number`

***

### has()

> **has**(`key`): `boolean`

Defined in: [lru-cache.ts:110](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L110)

#### Parameters

##### key

`K`

#### Returns

`boolean`

***

### set()

> **set**(`key`, `value`, `ttl?`): `void`

Defined in: [lru-cache.ts:76](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/dsa/src/lru-cache.ts#L76)

#### Parameters

##### key

`K`

##### value

`V`

##### ttl?

`number`

#### Returns

`void`
