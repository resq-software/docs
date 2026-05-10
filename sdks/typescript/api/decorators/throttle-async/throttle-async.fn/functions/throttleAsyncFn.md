# Function: throttleAsyncFn()

> **throttleAsyncFn**\<`D`, `A`\>(`originalMethod`, `parallelCalls?`): [`AsyncMethod`](../../../types/type-aliases/AsyncMethod.md)\<`D`, `A`\>

Defined in: [throttle-async/throttle-async.fn.ts:54](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/throttle-async/throttle-async.fn.ts#L54)

Wraps an async method to limit concurrent executions.

## Type Parameters

### D

`D` = `any`

The resolved type of the async method

### A

`A` *extends* `any`[] = `any`[]

The argument types of the original method

## Parameters

### originalMethod

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod.md)\<`D`, `A`\>

The async method to throttle

### parallelCalls?

`number` = `1`

Maximum number of concurrent calls

## Returns

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod.md)\<`D`, `A`\>

The throttled async method

## Example

```typescript
class ApiClient {
  async fetchUser(userId: string): Promise<User> {
    return fetch(`/api/users/${userId}`).then(r => r.json());
  }
}

const client = new ApiClient();

// Limit to 2 concurrent requests
const throttledFetch = throttleAsyncFn(
  client.fetchUser.bind(client),
  2
);

// Execute multiple calls, only 2 run concurrently
const users = await Promise.all([
  throttledFetch('1'), // Starts immediately
  throttledFetch('2'), // Starts immediately
  throttledFetch('3'), // Queued, starts when 1 or 2 completes
  throttledFetch('4'), // Queued, starts when slot available
]);
```
