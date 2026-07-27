# Function: throttleAsyncFn()

&gt; **throttleAsyncFn**\<`D`, `A`\>(`originalMethod`, `parallelCalls?`): [`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

Defined in: [throttle-async/throttle-async.fn.ts:65](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/throttle-async/throttle-async.fn.ts#L65)

Wrap an async method to limit concurrent executions (function form of
throttleAsync). Calls beyond the limit queue and run in FIFO order.

Each call to `throttleAsyncFn` owns its own [ThrottleAsyncExecutor](../../throttle-async-executor/classes/ThrottleAsyncExecutor) and
queue. The queue is unbounded; a rejected call frees its slot so later calls
still run. There is no cancellation. `parallelCalls` must be `>= 1` — a value
below `1` never dispatches and every call queues indefinitely.

## Type Parameters

### D

`D` = `unknown`

The resolved type of the async method.

### A

`A` *extends* `unknown`[] = `unknown`[]

The argument tuple of the original method.

## Parameters

### originalMethod

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The async method to throttle.

### parallelCalls?

`number` = `1`

Maximum number of concurrent calls; defaults to `1`. Must
be `>= 1`.

## Returns

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The throttled async method; each returned promise settles with its own
call's result or rejection.

## Example

```ts
class ApiClient {
  async fetchUser(userId: string): Promise<User> {
    return fetch(`/api/users/${userId}`).then((r) => r.json());
  }
}

const client = new ApiClient();

// Limit to two concurrent requests.
const throttledFetch = throttleAsyncFn(client.fetchUser.bind(client), 2);

// Execute multiple calls; only two run concurrently.
const users = await Promise.all([
  throttledFetch("1"), // Starts immediately.
  throttledFetch("2"), // Starts immediately.
  throttledFetch("3"), // Queued; starts when 1 or 2 completes.
  throttledFetch("4"), // Queued; starts when a slot frees up.
]);
```
