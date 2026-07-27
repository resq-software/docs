# Interface: RateLimitAsyncCounter

Defined in: [rate-limit/rate-limit.types.ts:136](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/rate-limit/rate-limit.types.ts#L136)

Asynchronous counter contract for distributed rate limiting; use it when the
counter performs async operations (e.g. Redis or a database).

`getCount` resolves `0` for an unseen or fully-decremented key. Because
`rateLimitFn` reads then increments in two separate awaits, this contract alone
cannot guarantee a hard cap under concurrency; back it with an atomic
increment-and-read for a strict limit (see rateLimitFn).

## Example

```ts
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

&gt; **dec**: (`key`) =&gt; `Promise`\<`void`\>

Defined in: [rate-limit/rate-limit.types.ts:140](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/rate-limit/rate-limit.types.ts#L140)

Decrement the count for a key asynchronously.

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`void`\>

***

### getCount

&gt; **getCount**: (`key`) =&gt; `Promise`\<`number`\>

Defined in: [rate-limit/rate-limit.types.ts:142](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/rate-limit/rate-limit.types.ts#L142)

Get the current count for a key asynchronously.

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`number`\>

***

### inc

&gt; **inc**: (`key`) =&gt; `Promise`\<`void`\>

Defined in: [rate-limit/rate-limit.types.ts:138](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/rate-limit/rate-limit.types.ts#L138)

Increment the count for a key asynchronously.

#### Parameters

##### key

`string`

#### Returns

`Promise`\<`void`\>
