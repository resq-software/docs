# Class: LeakyBucketLimiter

Defined in: [throttle.ts:767](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L767)

Leaky-bucket rate limiter.

Requests are appended to a fixed-capacity FIFO queue and "leak" out
at a constant rate (`requestsPerSecond`). The result is **smoothed**
traffic: even if `acquire` is called in a burst, each protected
action fires at fixed `1000 / requestsPerSecond` millisecond
intervals.

Compared to [TokenBucketLimiter](./TokenBucketLimiter), leaky-bucket does not allow
bursts — pick this when downstream systems can't tolerate spiky
load.

## Example

```ts
const limiter = new LeakyBucketLimiter(50, 5); // up to 50 queued, drains 5/sec
await limiter.acquire();
await downstreamCall();
```

## Implements

- [`RateLimiter`](../interfaces/RateLimiter)

## Constructors

### Constructor

&gt; **new LeakyBucketLimiter**(`capacity`, `requestsPerSecond`): `LeakyBucketLimiter`

Defined in: [throttle.ts:783](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L783)

#### Parameters

##### capacity

`PositiveInt`

Maximum queue depth. Calls to [acquire](#acquire)
  that exceed this throw immediately ("Rate limit exceeded:
  queue full"); use [tryAcquire](#tryacquire) to test first. Construct with
  `toPositiveInt(...)` so invalid depths are rejected at the boundary.

##### requestsPerSecond

`PositiveNumber`

Steady-state drain rate. Internally
  converted to a per-request gap of `1000 / requestsPerSecond`
  milliseconds. May be fractional (e.g. `0.5` = one request every two
  seconds); construct with `toPositiveNumber(...)`.

#### Returns

`LeakyBucketLimiter`

## Methods

### acquire()

&gt; **acquire**(): `Promise`\<`void`\>

Defined in: [throttle.ts:802](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L802)

Enqueue and await release.

Because it is `async`, the overflow failure surfaces as a **rejected**
`Promise` (await/`.catch`), not a synchronous throw. Not cancellable:
no `AbortSignal` hook, and a waiter that made it into the queue resolves
on its scheduled leak — or never, if [reset](#reset) runs first (see
[reset](#reset)). Reads the wall clock and arms a `setTimeout` between
leaks.

#### Returns

`Promise`\<`void`\>

#### Throws

With message `"Rate limit exceeded: queue full"` when
  the queue is already at `capacity`. Catch and translate to a 429 in
  HTTP middleware.

#### Implementation of

[`RateLimiter`](../interfaces/RateLimiter).[`acquire`](../interfaces/RateLimiter#acquire)

***

### getStats()

&gt; **getStats**(): [`RateLimiterStats`](../type-aliases/RateLimiterStats)

Defined in: [throttle.ts:869](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L869)

Snapshot of bucket state.

#### Returns

[`RateLimiterStats`](../type-aliases/RateLimiterStats)

`{ availableTokens, queueSize, capacity }` where
  `availableTokens = capacity − queueSize` (free queue slots).

#### Implementation of

[`RateLimiter`](../interfaces/RateLimiter).[`getStats`](../interfaces/RateLimiter#getstats)

***

### reset()

&gt; **reset**(): `void`

Defined in: [throttle.ts:884](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L884)

Drop every queued waiter and stop processing.

Note: pending promises returned by [acquire](#acquire) will **never
resolve** after a `reset()`. Plumb an `AbortSignal` through call
sites if cancellable waits are required.

#### Returns

`void`

#### Implementation of

[`RateLimiter`](../interfaces/RateLimiter).[`reset`](../interfaces/RateLimiter#reset)

***

### tryAcquire()

&gt; **tryAcquire**(): `boolean`

Defined in: [throttle.ts:822](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L822)

Non-blocking probe.

#### Returns

`boolean`

`true` only when the queue is empty **and** no drain
  timer is currently armed — i.e. the caller could fire
  immediately. Returns `false` even when there is room in the
  queue but a previous call is still mid-leak; in that case
  [acquire](#acquire) would still succeed but with a wait.

#### Implementation of

[`RateLimiter`](../interfaces/RateLimiter).[`tryAcquire`](../interfaces/RateLimiter#tryacquire)
