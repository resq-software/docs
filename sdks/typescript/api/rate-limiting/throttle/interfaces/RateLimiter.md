# Interface: RateLimiter

Defined in: [throttle.ts:536](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L536)

A **keyless** rate limiter: one bucket per instance, guarding a single stream
of work. The Strategy interface shared by [TokenBucketLimiter](../classes/TokenBucketLimiter) (bursty)
and [LeakyBucketLimiter](../classes/LeakyBucketLimiter) (smoothed) — depend on this abstraction and swap
the algorithm without touching call sites, provided call sites already honor
the interface contract (handle a rejected [RateLimiter.acquire](#acquire), and do
not assume [RateLimiter.tryAcquire](#tryacquire) reserves a slot). See each method's
doc for where the two algorithms legitimately diverge.

## Example

```ts
async function guarded(limiter: RateLimiter, work: () => Promise<void>) {
  await limiter.acquire();
  await work();
}
// interchangeable:
guarded(new TokenBucketLimiter(toPositiveInt(5), toPositiveMillis(1000)), work);
guarded(new LeakyBucketLimiter(toPositiveInt(5), toPositiveNumber(2)), work);
```

## Methods

### acquire()

&gt; **acquire**(): `Promise`\<`void`\>

Defined in: [throttle.ts:544](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L544)

Take one slot, awaiting future capacity if none is available.

Implementations backed by a bounded queue (e.g. [LeakyBucketLimiter](../classes/LeakyBucketLimiter))
MAY reject once that bound is exceeded rather than waiting indefinitely, so
callers must handle rejection — not only eventual resolution.

#### Returns

`Promise`\<`void`\>

***

### getStats()

&gt; **getStats**(): [`RateLimiterStats`](../type-aliases/RateLimiterStats)

Defined in: [throttle.ts:556](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L556)

A snapshot of the limiter's current capacity state.

#### Returns

[`RateLimiterStats`](../type-aliases/RateLimiterStats)

***

### reset()

&gt; **reset**(): `void`

Defined in: [throttle.ts:558](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L558)

Restore full capacity, abandoning any queued waiters.

#### Returns

`void`

***

### tryAcquire()

&gt; **tryAcquire**(): `boolean`

Defined in: [throttle.ts:554](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L554)

Non-blocking probe for a free slot.

Implementations that can consume atomically (e.g. [TokenBucketLimiter](../classes/TokenBucketLimiter))
reserve a slot when they return `true`. Implementations that cannot guarantee
atomic reservation (e.g. [LeakyBucketLimiter](../classes/LeakyBucketLimiter)) may probe without
reserving — check the concrete class before relying on `true` to mean a
slot is held for you.

#### Returns

`boolean`
