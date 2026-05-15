# Class: MemoryRateLimitStore

Defined in: [rate-limit.ts:192](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/rate-limit.ts#L192)

[IRateLimitStore](../interfaces/IRateLimitStore) that keeps counters in a process-local `Map`.

Suitable for **single-process** deployments only — a multi-instance
deployment will under-count because each instance sees only its own
traffic. Use [RedisRateLimitStore](./RedisRateLimitStore) (or another distributed
backend) in production when more than one node serves traffic.

Counters are reset *implicitly* once the window expires — the next
`check()` past `resetTime` starts a fresh window. There is no
background sweeper, so memory grows with the number of distinct keys
over the lifetime of the process; pair with periodic `reset()` for
long-lived processes that see unbounded key cardinality.

## Implements

- [`IRateLimitStore`](../interfaces/IRateLimitStore)

## Constructors

### Constructor

> **new MemoryRateLimitStore**(): `MemoryRateLimitStore`

#### Returns

`MemoryRateLimitStore`

## Methods

### check()

> **check**(`key`, `windowMs`, `maxRequests`): `Promise`\<\&#123; `limited`: `boolean`; `remaining`: `number`; `resetTime`: `number`; `total`: `number`; \&#125;\>

Defined in: [rate-limit.ts:196](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/rate-limit.ts#L196)

Atomically increment the counter for `key` within a sliding window
of `windowMs` and decide whether to allow the request.

#### Parameters

##### key

`string`

Caller-chosen identity key (e.g. `"user:42"`).

##### windowMs

`number`

Window length in milliseconds.

##### maxRequests

`number`

Maximum requests permitted in the window.

#### Returns

`Promise`\<\&#123; `limited`: `boolean`; `remaining`: `number`; `resetTime`: `number`; `total`: `number`; \&#125;\>

A [RateLimitCheckResult](../type-aliases/RateLimitCheckResult) describing the decision.

#### Implementation of

[`IRateLimitStore`](../interfaces/IRateLimitStore).[`check`](../interfaces/IRateLimitStore#check)

***

### reset()

> **reset**(`key`): `Promise`\<`void`\>

Defined in: [rate-limit.ts:222](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/rate-limit.ts#L222)

Drop any state held for `key`. Useful for admin / unit-test reset
paths; not invoked by middleware itself.

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`void`\>

#### Implementation of

[`IRateLimitStore`](../interfaces/IRateLimitStore).[`reset`](../interfaces/IRateLimitStore#reset)
