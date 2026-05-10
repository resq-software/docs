# Interface: RateLimitAsyncCounter

Defined in: [rate-limit/rate-limit.types.ts:150](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/rate-limit/rate-limit.types.ts#L150)

Interface for async rate limit counter implementations.
Use this when the counter needs to perform async operations (e.g., Redis, database).

 RateLimitAsyncCounter

## Example

```typescript
class RedisCounter implements RateLimitAsyncCounter {
  async inc(key: string): Promise<void> {
    await redis.incr(`ratelimit:${key}`);
  }

  async dec(key: string): Promise<void> {
    await redis.decr(`ratelimit:${key}`);
  }

  async getCount(key: string): Promise<number> {
    const count = await redis.get(`ratelimit:${key}`);
    return parseInt(count ?? '0', 10);
  }
}
```

## Properties

### dec

> **dec**: (`key`) => `Promise`\<`void`\>

Defined in: [rate-limit/rate-limit.types.ts:154](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/rate-limit/rate-limit.types.ts#L154)

Decrement the count for a key asynchronously

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`void`\>

***

### getCount

> **getCount**: (`key`) => `Promise`\<`number`\>

Defined in: [rate-limit/rate-limit.types.ts:156](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/rate-limit/rate-limit.types.ts#L156)

Get the current count for a key asynchronously

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`number`\>

***

### inc

> **inc**: (`key`) => `Promise`\<`void`\>

Defined in: [rate-limit/rate-limit.types.ts:152](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/rate-limit/rate-limit.types.ts#L152)

Increment the count for a key asynchronously

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`void`\>
