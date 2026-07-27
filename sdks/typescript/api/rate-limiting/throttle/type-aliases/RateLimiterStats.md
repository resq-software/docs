# Type Alias: RateLimiterStats

&gt; **RateLimiterStats** = *typeof* `RateLimiterStatsSchema.Type`

Defined in: [throttle.ts:81](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/rate-limiting/src/throttle.ts#L81)

Capacity snapshot for a keyless limiter, inferred from
[RateLimiterStatsSchema](../variables/RateLimiterStatsSchema).

A read-only, point-in-time copy — not a live view; re-call `getStats()` for
a fresh reading. `availableTokens` is interpreted **per implementation**:
for [TokenBucketLimiter](../classes/TokenBucketLimiter) it is the floored count of withdrawable
tokens, while for [LeakyBucketLimiter](../classes/LeakyBucketLimiter) it is the number of free queue
slots (`capacity − queueSize`). `queueSize` is the count of waiters parked
in [RateLimiter.acquire](../interfaces/RateLimiter#acquire).
