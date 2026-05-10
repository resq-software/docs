# Class: TokenBucketLimiter

Defined in: [throttle.ts:413](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L413)

Rate limiter using token bucket algorithm

## Example

```ts
const limiter = new TokenBucketLimiter(5, 60000); // 5 requests per minute

async function fetchData() {
  await limiter.acquire();
  return fetch('/api/data');
}
```

## Constructors

### Constructor

> **new TokenBucketLimiter**(`capacity`, `windowMs`): `TokenBucketLimiter`

Defined in: [throttle.ts:425](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L425)

#### Parameters

##### capacity

`number`

Maximum number of tokens (requests)

##### windowMs

`number`

Time window in milliseconds

#### Returns

`TokenBucketLimiter`

## Methods

### acquire()

> **acquire**(): `Promise`\<`void`\>

Defined in: [throttle.ts:450](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L450)

Acquire a token (wait if none available)

#### Returns

`Promise`\<`void`\>

***

### getStats()

> **getStats**(): `object`

Defined in: [throttle.ts:501](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L501)

Get rate limiter stats

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

Defined in: [throttle.ts:513](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L513)

Reset the rate limiter

#### Returns

`void`

***

### tryAcquire()

> **tryAcquire**(): `boolean`

Defined in: [throttle.ts:468](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/throttle.ts#L468)

Try to acquire a token without waiting

#### Returns

`boolean`
