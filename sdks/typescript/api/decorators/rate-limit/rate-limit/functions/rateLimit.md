# Function: rateLimit()

> **rateLimit**\<`T`\>(`config`): (`target`, `propertyName`, `descriptor`) => `TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method)\<`unknown`\>\>

Defined in: [rate-limit/rate-limit.ts:71](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/rate-limit/rate-limit.ts#L71)

Decorator that rate limits method calls.
Only allows a specified number of calls within a time window.

## Type Parameters

### T

`T` = `unknown`

The type of the class containing the decorated method

## Parameters

### config

[`RateLimitConfigs`](../../rate-limit.types/interfaces/RateLimitConfigs)\<`T`\>

Rate limit configuration

## Returns

The decorator function

(`target`, `propertyName`, `descriptor`) => `TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method)\<`unknown`\>\>

## Throws

When applied to a non-method property

## Example

```typescript
class Api {
  @rateLimit({
    timeSpanMs: 1000,  // 1 second
    allowedCalls: 5,   // Max 5 calls
    exceedHandler: () => console.warn('Rate limit exceeded!')
  })
  fetchData() {
    // Only 5 calls allowed per second
  }

  // With custom key resolver for per-user limiting
  @rateLimit({
    timeSpanMs: 60000,  // 1 minute
    allowedCalls: 100,  // Max 100 calls per user per minute
    keyResolver: (userId) => userId  // Limit per user
  })
  getUserData(userId: string) {
    return database.getUser(userId);
  }
}

// With custom counter implementation
class DistributedApi {
  @rateLimit({
    timeSpanMs: 1000,
    allowedCalls: 10,
    rateLimitCounter: new RedisRateLimitCounter()  // Distributed counter
  })
  async heavyOperation(): Promise<void> {
    // Rate limited across all instances
  }
}
```
