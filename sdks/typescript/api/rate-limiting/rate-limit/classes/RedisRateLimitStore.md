# Class: RedisRateLimitStore

Defined in: [rate-limit.ts:124](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/rate-limit.ts#L124)

[IRateLimitStore](../interfaces/IRateLimitStore) backed by Upstash Redis using the
`@upstash/ratelimit` sliding-window algorithm.

Internally caches one `Ratelimit` instance per `(windowMs,
maxRequests)` pair so re-using the same store across multiple routes
does not allocate a new limiter every call.

Use this for any deployment that runs more than one process — counters
are shared across all nodes via Redis.

## Example

```ts
import { Redis } from "@upstash/redis";
import { RedisRateLimitStore } from "@resq-sw/rate-limiting";

const store = new RedisRateLimitStore(Redis.fromEnv());
const decision = await store.check("user:42", 60_000, 100);
if (decision.limited) return new Response("Too many requests", { status: 429 });
```

## Implements

- [`IRateLimitStore`](../interfaces/IRateLimitStore)

## Constructors

### Constructor

> **new RedisRateLimitStore**(`redisClient`): `RedisRateLimitStore`

Defined in: [rate-limit.ts:132](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/rate-limit.ts#L132)

#### Parameters

##### redisClient

`Redis`

Connected Upstash Redis client. Reuse the same
  client across stores; do not allocate per request.

#### Returns

`RedisRateLimitStore`

## Methods

### check()

> **check**(`key`, `windowMs`, `maxRequests`): `Promise`\<\&#123; `limited`: `boolean`; `remaining`: `number`; `resetTime`: `number`; `total`: `number`; \&#125;\>

Defined in: [rate-limit.ts:151](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/rate-limit.ts#L151)

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

> **reset**(`_key`): `Promise`\<`void`\>

Defined in: [rate-limit.ts:172](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/rate-limit.ts#L172)

#### Parameters

##### \_key

`string`

#### Returns

`Promise`\<`void`\>

#### Inherit Doc

a no-op.** `@upstash/ratelimit` distributes counters
across multiple sliding-window keys per limiter, and there is no
single delete that resets all of them. Provided for interface
conformance; future versions may scan the prefix and clear all
matching keys.

#### Implementation of

[`IRateLimitStore`](../interfaces/IRateLimitStore).[`reset`](../interfaces/IRateLimitStore#reset)
