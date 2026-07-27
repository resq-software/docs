# Class: RedisRateLimitStore

Defined in: [rate-limit.ts:131](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L131)

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
import { RedisRateLimitStore } from "@resq-systems/rate-limiting";

const store = new RedisRateLimitStore(Redis.fromEnv());
const decision = await store.check("user:42", 60_000, 100);
if (!decision.allowed) return new Response("Too many requests", { status: 429 });
```

## Implements

- [`IRateLimitStore`](../interfaces/IRateLimitStore)

## Constructors

### Constructor

&gt; **new RedisRateLimitStore**(`redisClient`): `RedisRateLimitStore`

Defined in: [rate-limit.ts:139](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L139)

#### Parameters

##### redisClient

`Redis`

Connected Upstash Redis client. Reuse the same
  client across stores; do not allocate per request.

#### Returns

`RedisRateLimitStore`

## Methods

### check()

&gt; **check**(`key`, `windowMs`, `maxRequests`): `Promise`\<`ReadonlySide`\<\{ `allowed`: `Literal`\<`true`\>; `limit`: `Number`; `remaining`: `Number`; `resetAt`: `Number`; \}, `"Type"`\> \| `ReadonlySide`\<\{ `allowed`: `Literal`\<`false`\>; `limit`: `Number`; `remaining`: `Literal`\<`0`\>; `resetAt`: `Number`; \}, `"Type"`\>\>

Defined in: [rate-limit.ts:170](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L170)

#### Parameters

##### key

`string`

##### windowMs

`number`

##### maxRequests

`number`

#### Returns

`Promise`\<`ReadonlySide`\<\{ `allowed`: `Literal`\<`true`\>; `limit`: `Number`; `remaining`: `Number`; `resetAt`: `Number`; \}, `"Type"`\> \| `ReadonlySide`\<\{ `allowed`: `Literal`\<`false`\>; `limit`: `Number`; `remaining`: `Literal`\<`0`\>; `resetAt`: `Number`; \}, `"Type"`\>\>

#### Inherit Doc

**Performs**

a network round-trip to Redis and records the request there;
the counter update is atomic across all processes sharing the client.
Failure is surfaced as a **rejected** `Promise`, not a decision — a
`false` result means "rate limited", never "Redis was unreachable".

#### Throws

If the underlying Redis call fails (connection refused,
  auth failure, timeout). Propagated from `@upstash/ratelimit`; decide
  per route whether to fail open (admit) or closed (reject) in a
  surrounding `catch`.

#### Implementation of

[`IRateLimitStore`](../interfaces/IRateLimitStore).[`check`](../interfaces/IRateLimitStore#check)

***

### reset()

&gt; **reset**(`_key`): `Promise`\<`void`\>

Defined in: [rate-limit.ts:195](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/rate-limit.ts#L195)

#### Parameters

##### \_key

`string`

#### Returns

`Promise`\<`void`\>

#### Inherit Doc

**\*\*Currently**

a no-op.** `@upstash/ratelimit` distributes counters
across multiple sliding-window keys per limiter, and there is no
single delete that resets all of them. Provided for interface
conformance; future versions may scan the prefix and clear all
matching keys.

#### Implementation of

[`IRateLimitStore`](../interfaces/IRateLimitStore).[`reset`](../interfaces/IRateLimitStore#reset)
