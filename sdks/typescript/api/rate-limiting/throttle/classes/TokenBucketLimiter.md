# Class: TokenBucketLimiter

Defined in: [throttle.ts:478](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L478)

Token-bucket rate limiter.

The bucket holds at most `capacity` tokens. Tokens refill **continuously**
over `windowMs` (one full bucket per window — i.e. `capacity / windowMs`
tokens per ms). Each accepted call deducts one token; when no tokens are
available, callers either wait via [acquire](#acquire) or get rejected via
[tryAcquire](#tryacquire).

Token-bucket limiters allow short bursts up to `capacity` while pinning
the long-run average to `capacity / windowMs`. Use this when bursty
traffic is acceptable; pick [LeakyBucketLimiter](./LeakyBucketLimiter) when you need
smoother request spacing.

## Example

```ts
const limiter = new TokenBucketLimiter(5, 60_000); // 5 req/min
await limiter.acquire();
fetch("/api/data");
```

## Constructors

### Constructor

> **new TokenBucketLimiter**(`capacity`, `windowMs`): `TokenBucketLimiter`

Defined in: [throttle.ts:492](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L492)

#### Parameters

##### capacity

`number`

Maximum bucket size (also the burst limit).

##### windowMs

`number`

Time window over which one full bucket of
  tokens accumulates. The steady-state rate is
  `capacity / windowMs` tokens per millisecond.

#### Returns

`TokenBucketLimiter`

## Methods

### acquire()

> **acquire**(): `Promise`\<`void`\>

Defined in: [throttle.ts:524](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L524)

Take one token, awaiting future refills if the bucket is empty.

Calls are released in FIFO order. Resolved promises consume one
token each — the resolver `await`s and proceeds with the protected
work without further bookkeeping.

#### Returns

`Promise`\<`void`\>

***

### getStats()

> **getStats**(): `object`

Defined in: [throttle.ts:587](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L587)

Snapshot of bucket state.

#### Returns

`object`

`{ availableTokens, queueSize, capacity }` —
  `availableTokens` is rounded down so it never claims more
  tokens than a caller could actually withdraw.

##### availableTokens

> **availableTokens**: `number`

##### capacity

> **capacity**: `number`

##### queueSize

> **queueSize**: `number`

***

### reset()

> **reset**(): `void`

Defined in: [throttle.ts:604](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L604)

Refill the bucket to capacity and abandon any queued waiters.

Note: queued promises returned by [acquire](#acquire) that were
waiting at the time of `reset()` will **never resolve**. Use
with care in long-running services; prefer plumbing an
`AbortSignal` through call sites instead of resetting.

#### Returns

`void`

***

### tryAcquire()

> **tryAcquire**(): `boolean`

Defined in: [throttle.ts:546](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L546)

Non-blocking variant of [acquire](#acquire).

#### Returns

`boolean`

`true` if a token was consumed, `false` if the bucket
  was empty (the caller should drop the request, return 429, or
  apply its own back-pressure).
