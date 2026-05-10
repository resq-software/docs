# Interface: RateLimitConfigs\<T\>

Defined in: [rate-limit/rate-limit.types.ts:66](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/rate-limit/rate-limit.types.ts#L66)

Configuration options for rate limiting.

 RateLimitConfigs

## Example

```typescript
const config: RateLimitConfigs<ApiService> = {
  timeSpanMs: 60000,     // 1 minute
  allowedCalls: 100,     // 100 calls per minute
  keyResolver: (userId) => `user-${userId}`,
  exceedHandler: () => { throw new Error('Rate limit exceeded'); }
};
```

## Type Parameters

### T

`T` = `any`

The type of the class containing the decorated method

## Properties

### allowedCalls

> **allowedCalls**: `number`

Defined in: [rate-limit/rate-limit.types.ts:70](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/rate-limit/rate-limit.types.ts#L70)

Maximum number of calls allowed in the time window

***

### exceedHandler?

> `optional` **exceedHandler?**: () => `void`

Defined in: [rate-limit/rate-limit.types.ts:78](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/rate-limit/rate-limit.types.ts#L78)

Handler called when rate limit is exceeded

#### Returns

`void`

***

### keyResolver?

> `optional` **keyResolver?**: ((...`args`) => `string`) \| keyof `T`

Defined in: [rate-limit/rate-limit.types.ts:72](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/rate-limit/rate-limit.types.ts#L72)

Function to generate rate limit keys (for per-user/entity limiting)

***

### rateLimitAsyncCounter?

> `optional` **rateLimitAsyncCounter?**: [`RateLimitAsyncCounter`](./RateLimitAsyncCounter)

Defined in: [rate-limit/rate-limit.types.ts:76](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/rate-limit/rate-limit.types.ts#L76)

Async counter implementation

***

### rateLimitCounter?

> `optional` **rateLimitCounter?**: [`RateLimitCounter`](./RateLimitCounter)

Defined in: [rate-limit/rate-limit.types.ts:74](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/rate-limit/rate-limit.types.ts#L74)

Custom counter implementation

***

### timeSpanMs

> **timeSpanMs**: `number`

Defined in: [rate-limit/rate-limit.types.ts:68](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/rate-limit/rate-limit.types.ts#L68)

The time window in milliseconds
