# Function: rateLimitFn()

&gt; **rateLimitFn**\<`T`, `D`, `A`\>(`originalMethod`, `config`): [`Method`](../../../types/type-aliases/Method)\<`D` \| `Promise`\<`D` \| `undefined`\> \| `undefined`, `A`\>

Defined in: [rate-limit/rate-limit.fn.ts:119](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/rate-limit/rate-limit.fn.ts#L119)

Create a rate-limited version of a method (function form of rateLimit).

With a distributed `rateLimitAsyncCounter`, limiting is best-effort under
concurrency: the check-then-increment is not atomic, so bursts can briefly
exceed `allowedCalls`. Back the counter with an atomic increment for a hard cap.

On an admitted call it increments the counter and schedules a `setTimeout` to
decrement it after `timeSpanMs` (a clock/timer effect); on a dropped call it
invokes `config.exceedHandler` (if any) for its side effects.

## Type Parameters

### T

`T` = `unknown`

The class type a `keyof T` key resolver resolves against.

### D

`D` = `unknown`

The return type of the original method.

### A

`A` *extends* `unknown`[] = `unknown`[]

The argument tuple of the original method.

## Parameters

### originalMethod

[`Method`](../../../types/type-aliases/Method)\<`D`, `A`\>

The method to rate limit.

### config

[`RateLimitConfigs`](../../rate-limit.types/interfaces/RateLimitConfigs)\<`T`\>

The rate-limit configuration.

## Returns

[`Method`](../../../types/type-aliases/Method)\<`D` \| `Promise`\<`D` \| `undefined`\> \| `undefined`, `A`\>

A rate-limited method that yields the original result when admitted and
the sentinel `undefined` when dropped; the result is wrapped in a promise when a
distributed `rateLimitAsyncCounter` is configured, otherwise it is synchronous.

## Example

```ts
class ApiService {
  async fetchData(id: string): Promise<Data> {
    return await fetch(`/api/data/${id}`).then((r) => r.json());
  }
}

const service = new ApiService();

// Rate limit to three calls per five seconds.
const limited = rateLimitFn(service.fetchData.bind(service), {
  timeSpanMs: 5000,
  allowedCalls: 3,
  exceedHandler: () => console.warn("Too many requests!"),
});

await limited("1"); // Executes.
await limited("2"); // Executes.
await limited("3"); // Executes.
const result = await limited("4"); // → undefined; logs the warning.
```
