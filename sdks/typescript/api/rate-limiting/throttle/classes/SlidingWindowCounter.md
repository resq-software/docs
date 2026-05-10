# Class: SlidingWindowCounter

Defined in: [throttle.ts:624](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L624)

Sliding window counter for accurate rate limiting

## Constructors

### Constructor

> **new SlidingWindowCounter**(`windowMs`, `maxRequests`): `SlidingWindowCounter`

Defined in: [throttle.ts:629](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L629)

#### Parameters

##### windowMs

`number`

##### maxRequests

`number`

#### Returns

`SlidingWindowCounter`

## Methods

### check()

> **check**(`key`): `object`

Defined in: [throttle.ts:640](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L640)

Check and increment counter for a key

#### Parameters

##### key

`string`

#### Returns

`object`

##### allowed

> **allowed**: `boolean`

##### remaining

> **remaining**: `number`

##### resetAt

> **resetAt**: `number`

***

### getStats()

> **getStats**(): `object`

Defined in: [throttle.ts:702](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L702)

Get stats

#### Returns

`object`

##### activeKeys

> **activeKeys**: `number`

##### keys

> **keys**: readonly `string`[]

***

### reset()

> **reset**(`key`): `void`

Defined in: [throttle.ts:683](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L683)

Reset counter for a key

#### Parameters

##### key

`string`

#### Returns

`void`
