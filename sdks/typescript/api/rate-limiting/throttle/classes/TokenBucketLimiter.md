# Class: TokenBucketLimiter

Defined in: [throttle.ts:601](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L601)

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

## Implements

- [`RateLimiter`](../interfaces/RateLimiter)

## Constructors

### Constructor

&gt; **new TokenBucketLimiter**(`capacity`, `windowMs`): `TokenBucketLimiter`

Defined in: [throttle.ts:618](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L618)

#### Parameters

##### capacity

`PositiveInt`

Maximum bucket size (also the burst limit). Construct
  with `toPositiveInt(...)` so zero, negative, and fractional capacities
  are rejected at the boundary.

##### windowMs

`PositiveMillis`

Time window over which one full bucket of
  tokens accumulates. The steady-state rate is
  `capacity / windowMs` tokens per millisecond. Construct with
  `toPositiveMillis(...)`.

#### Returns

`TokenBucketLimiter`

## Methods

### acquire()

&gt; **acquire**(): `Promise`\<`void`\>

Defined in: [throttle.ts:656](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L656)

Take one token, awaiting future refills if the bucket is empty.

Calls are released in FIFO order. Resolved promises consume one
token each — the resolver `await`s and proceeds with the protected
work without further bookkeeping.

Never rejects and is **not cancellable**: there is no `AbortSignal`
hook, so a waiter enqueued while the bucket is empty resolves only
once a token refills — or, if [reset](#reset) runs in the meantime,
**never** (see [reset](#reset)). Reads the wall clock and arms a
`setTimeout` per queued waiter.

#### Returns

`Promise`\<`void`\>

#### Implementation of

[`RateLimiter`](../interfaces/RateLimiter).[`acquire`](../interfaces/RateLimiter#acquire)

***

### getStats()

&gt; **getStats**(): [`RateLimiterStats`](../type-aliases/RateLimiterStats)

Defined in: [throttle.ts:719](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L719)

Snapshot of bucket state.

#### Returns

[`RateLimiterStats`](../type-aliases/RateLimiterStats)

`{ availableTokens, queueSize, capacity }` —
  `availableTokens` is rounded down so it never claims more
  tokens than a caller could actually withdraw.

#### Implementation of

[`RateLimiter`](../interfaces/RateLimiter).[`getStats`](../interfaces/RateLimiter#getstats)

***

### reset()

&gt; **reset**(): `void`

Defined in: [throttle.ts:736](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L736)

Refill the bucket to capacity and abandon any queued waiters.

Note: queued promises returned by [acquire](#acquire) that were
waiting at the time of `reset()` will **never resolve**. Use
with care in long-running services; prefer plumbing an
`AbortSignal` through call sites instead of resetting.

#### Returns

`void`

#### Implementation of

[`RateLimiter`](../interfaces/RateLimiter).[`reset`](../interfaces/RateLimiter#reset)

***

### tryAcquire()

&gt; **tryAcquire**(): `boolean`

Defined in: [throttle.ts:678](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L678)

Non-blocking variant of [acquire](#acquire).

#### Returns

`boolean`

`true` if a token was consumed, `false` if the bucket
  was empty (the caller should drop the request, return 429, or
  apply its own back-pressure).

#### Implementation of

[`RateLimiter`](../interfaces/RateLimiter).[`tryAcquire`](../interfaces/RateLimiter#tryacquire)
