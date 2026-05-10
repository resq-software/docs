# Function: rateLimitFn()

> **rateLimitFn**\<`D`, `A`\>(`originalMethod`, `config`): [`Method`](../../../types/type-aliases/Method.md)\<`D` \| `undefined`, `A`\>

Defined in: [rate-limit/rate-limit.fn.ts:56](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/rate-limit/rate-limit.fn.ts#L56)

Creates a rate-limited version of a method.

## Type Parameters

### D

`D` = `unknown`

The return type of the original method

### A

`A` *extends* `unknown`[] = `unknown`[]

The argument types of the original method

## Parameters

### originalMethod

[`Method`](../../../types/type-aliases/Method.md)\<`D`, `A`\>

The method to rate limit

### config

[`RateLimitConfigs`](../../rate-limit.types/interfaces/RateLimitConfigs.md)

The rate limit configuration

## Returns

[`Method`](../../../types/type-aliases/Method.md)\<`D` \| `undefined`, `A`\>

A rate-limited method

## Example

```typescript
class ApiService {
  async fetchData(id: string): Promise<Data> {
    return await fetch(`/api/data/${id}`).then(r => r.json());
  }
}

const service = new ApiService();

// Rate limit to 3 calls per 5 seconds
const limited = rateLimitFn(
  service.fetchData.bind(service),
  {
    timeSpanMs: 5000,
    allowedCalls: 3,
    exceedHandler: () => console.warn('Too many requests!')
  }
);

await limited('1'); // Executes
await limited('2'); // Executes
await limited('3'); // Executes
const result = await limited('4'); // Returns undefined, logs warning
```
