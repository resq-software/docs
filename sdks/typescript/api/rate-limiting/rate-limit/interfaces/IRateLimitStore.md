# Interface: IRateLimitStore

Defined in: [rate-limit.ts:85](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/rate-limit.ts#L85)

Pluggable backend for rate-limit state.

Implementations decide how counters are stored and how concurrency is
resolved (in-memory, Redis, distributed log, …). Stores are designed
to be reused across multiple `(windowMs, maxRequests)` configurations
keyed by the caller's `key` (typically `userId`, `ip`, or
`route + clientId`).

## Methods

### check()

> **check**(`key`, `windowMs`, `maxRequests`): `Promise`\<\&#123; `limited`: `boolean`; `remaining`: `number`; `resetTime`: `number`; `total`: `number`; \&#125;\>

Defined in: [rate-limit.ts:95](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/rate-limit.ts#L95)

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

***

### reset()

> **reset**(`key`): `Promise`\<`void`\>

Defined in: [rate-limit.ts:100](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/rate-limit.ts#L100)

Drop any state held for `key`. Useful for admin / unit-test reset
paths; not invoked by middleware itself.

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`void`\>
