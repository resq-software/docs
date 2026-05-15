# Class: LeakyBucketLimiter

Defined in: [throttle.ts:635](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L635)

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

## Constructors

### Constructor

> **new LeakyBucketLimiter**(`capacity`, `requestsPerSecond`): `LeakyBucketLimiter`

Defined in: [throttle.ts:649](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L649)

#### Parameters

##### capacity

`number`

Maximum queue depth. Calls to [acquire](#acquire)
  that exceed this throw immediately ("Rate limit exceeded:
  queue full"); use [tryAcquire](#tryacquire) to test first.

##### requestsPerSecond

`number`

Steady-state drain rate. Internally
  converted to a per-request gap of `1000 / requestsPerSecond`
  milliseconds.

#### Returns

`LeakyBucketLimiter`

## Methods

### acquire()

> **acquire**(): `Promise`\<`void`\>

Defined in: [throttle.ts:661](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L661)

Enqueue and await release.

#### Returns

`Promise`\<`void`\>

#### Throws

Error `"Rate limit exceeded: queue full"` when the queue
  is already at `capacity`. Catch and translate to a 429 in
  HTTP middleware.

***

### getStats()

> **getStats**(): `object`

Defined in: [throttle.ts:728](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L728)

Snapshot of bucket state.

#### Returns

`object`

`{ availableTokens, queueSize, capacity }` where
  `availableTokens = capacity − queueSize` (free queue slots).

##### availableTokens

> **availableTokens**: `number`

##### capacity

> **capacity**: `number`

##### queueSize

> **queueSize**: `number`

***

### reset()

> **reset**(): `void`

Defined in: [throttle.ts:743](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L743)

Drop every queued waiter and stop processing.

Note: pending promises returned by [acquire](#acquire) will **never
resolve** after a `reset()`. Plumb an `AbortSignal` through call
sites if cancellable waits are required.

#### Returns

`void`

***

### tryAcquire()

> **tryAcquire**(): `boolean`

Defined in: [throttle.ts:681](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/rate-limiting/src/throttle.ts#L681)

Non-blocking probe.

#### Returns

`boolean`

`true` only when the queue is empty **and** no drain
  timer is currently armed — i.e. the caller could fire
  immediately. Returns `false` even when there is room in the
  queue but a previous call is still mid-leak; in that case
  [acquire](#acquire) would still succeed but with a wait.
