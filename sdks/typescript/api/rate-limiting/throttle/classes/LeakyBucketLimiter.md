# Class: LeakyBucketLimiter

Defined in: [throttle.ts:528](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L528)

Leaky bucket algorithm - requests "leak" out at a constant rate
Provides smoother rate limiting than token bucket

## Constructors

### Constructor

> **new LeakyBucketLimiter**(`capacity`, `requestsPerSecond`): `LeakyBucketLimiter`

Defined in: [throttle.ts:538](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L538)

#### Parameters

##### capacity

`number`

Maximum queue size

##### requestsPerSecond

`number`

How many requests to process per second

#### Returns

`LeakyBucketLimiter`

## Methods

### acquire()

> **acquire**(): `Promise`\<`void`\>

Defined in: [throttle.ts:546](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L546)

Add a request to the bucket

#### Returns

`Promise`\<`void`\>

***

### getStats()

> **getStats**(): `object`

Defined in: [throttle.ts:600](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L600)

Get stats

#### Returns

`object`

##### availableTokens

> **availableTokens**: `number`

##### capacity

> **capacity**: `number`

##### queueSize

> **queueSize**: `number`

***

### reset()

> **reset**(): `void`

Defined in: [throttle.ts:611](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L611)

Clear the queue

#### Returns

`void`

***

### tryAcquire()

> **tryAcquire**(): `boolean`

Defined in: [throttle.ts:560](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L560)

Try to acquire without blocking

#### Returns

`boolean`
