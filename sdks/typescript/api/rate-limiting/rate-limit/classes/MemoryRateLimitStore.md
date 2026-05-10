# Class: MemoryRateLimitStore

Defined in: [rate-limit.ts:102](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/rate-limit.ts#L102)

In-memory rate limit store for local development or simple services

## Implements

- [`IRateLimitStore`](../interfaces/IRateLimitStore.md)

## Constructors

### Constructor

> **new MemoryRateLimitStore**(): `MemoryRateLimitStore`

#### Returns

`MemoryRateLimitStore`

## Methods

### check()

> **check**(`key`, `windowMs`, `maxRequests`): `Promise`\<\&#123; `limited`: `boolean`; `remaining`: `number`; `resetTime`: `number`; `total`: `number`; \&#125;\>

Defined in: [rate-limit.ts:105](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/rate-limit.ts#L105)

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

[`IRateLimitStore`](../interfaces/IRateLimitStore.md).[`check`](../interfaces/IRateLimitStore.md#check)

***

### reset()

> **reset**(`key`): `Promise`\<`void`\>

Defined in: [rate-limit.ts:130](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/rate-limiting/src/rate-limit.ts#L130)

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`void`\>

#### Implementation of

[`IRateLimitStore`](../interfaces/IRateLimitStore.md).[`reset`](../interfaces/IRateLimitStore.md#reset)
