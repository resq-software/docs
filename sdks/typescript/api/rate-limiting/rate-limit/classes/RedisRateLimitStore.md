# Class: RedisRateLimitStore

Defined in: [rate-limit.ts:59](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/rate-limit.ts#L59)

Redis-backed rate limit store using @upstash/ratelimit

## Implements

- [`IRateLimitStore`](../interfaces/IRateLimitStore)

## Constructors

### Constructor

> **new RedisRateLimitStore**(`redisClient`): `RedisRateLimitStore`

Defined in: [rate-limit.ts:63](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/rate-limit.ts#L63)

#### Parameters

##### redisClient

`Redis`

#### Returns

`RedisRateLimitStore`

## Methods

### check()

> **check**(`key`, `windowMs`, `maxRequests`): `Promise`\<\&#123; `limited`: `boolean`; `remaining`: `number`; `resetTime`: `number`; `total`: `number`; \&#125;\>

Defined in: [rate-limit.ts:81](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/rate-limit.ts#L81)

#### Parameters

##### key

`string`

##### windowMs

`number`

##### maxRequests

`number`

#### Returns

`Promise`\<\&#123; `limited`: `boolean`; `remaining`: `number`; `resetTime`: `number`; `total`: `number`; \&#125;\>

#### Implementation of

[`IRateLimitStore`](../interfaces/IRateLimitStore).[`check`](../interfaces/IRateLimitStore#check)

***

### reset()

> **reset**(`_key`): `Promise`\<`void`\>

Defined in: [rate-limit.ts:93](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/rate-limit.ts#L93)

#### Parameters

##### \_key

`string`

#### Returns

`Promise`\<`void`\>

#### Implementation of

[`IRateLimitStore`](../interfaces/IRateLimitStore).[`reset`](../interfaces/IRateLimitStore#reset)
