# Function: rateLimit()

&gt; **rateLimit**\<`T`\>(`config`): [`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

Defined in: [rate-limit/rate-limit.ts:82](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/rate-limit/rate-limit.ts#L82)

Rate limit a method to at most `allowedCalls` invocations per `timeSpanMs`
window; calls beyond the allowance are dropped and routed to `exceedHandler`.

The counter is built once, at decoration time, so the limit spans every instance
of the class (unless a `keyResolver` partitions it). A dropped call returns
`undefined` in place of the method's value — see [rateLimitFn](../../rate-limit.fn/functions/rateLimitFn) for the
sync-vs-async return shape and the best-effort caveat under concurrency. Mutates
the supplied property descriptor in place.

## Type Parameters

### T

`T` = `unknown`

The class type that owns the decorated method.

## Parameters

### config

[`RateLimitConfigs`](../../rate-limit.types/interfaces/RateLimitConfigs)\<`T`\>

Rate-limit configuration: window size, allowance, and optional
key resolver, counter, and exceed handler.

## Returns

[`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

The method decorator, generic over the decorated method so its
signature is preserved end-to-end.

## Throws

If applied to anything other than a method.

## Example

```ts
class Api {
  @rateLimit({
    timeSpanMs: 1000, // One second.
    allowedCalls: 5, // At most five calls.
    exceedHandler: () => console.warn("Rate limit exceeded!"),
  })
  fetchData() {
    // Only five calls are allowed per second.
  }

  // With a custom key resolver for per-user limiting.
  @rateLimit({
    timeSpanMs: 60000, // One minute.
    allowedCalls: 100, // At most 100 calls per user per minute.
    keyResolver: (userId) => userId, // Limit per user.
  })
  getUserData(userId: string) {
    return database.getUser(userId);
  }
}

// With a custom counter implementation.
class DistributedApi {
  @rateLimit({
    timeSpanMs: 1000,
    allowedCalls: 10,
    rateLimitCounter: new RedisRateLimitCounter(), // Distributed counter.
  })
  async heavyOperation(): Promise<void> {
    // Rate limited across all instances.
  }
}
```

## See

[rateLimitFn](../../rate-limit.fn/functions/rateLimitFn) for the function form.
