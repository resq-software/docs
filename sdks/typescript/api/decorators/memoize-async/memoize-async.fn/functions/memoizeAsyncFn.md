# Function: memoizeAsyncFn()

## Call Signature

&gt; **memoizeAsyncFn**\<`D`, `A`\>(`originalMethod`): [`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

Defined in: [memoize-async/memoize-async.fn.ts:90](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize-async/memoize-async.fn.ts#L90)

Wrap a promise-returning method so results are cached and concurrent calls are
deduplicated (function form of memoizeAsync).

While a call is in flight, further calls with the same key share its promise;
the resolved value is then cached for later lookups. The second argument omits
to cache forever, is a number for a TTL in milliseconds, or an
[AsyncMemoizeConfig](../../memoize-async.types/interfaces/AsyncMemoizeConfig) for a custom cache, key resolver, and/or expiry.

Concurrency and failure contract:
- Concurrent same-key calls resolve or reject together — they share one
  in-flight promise, which is cleared once it settles (success or failure), so
  a rejection is not cached and the next call re-runs the method.
- A resolved value of `null`/`undefined` is treated as a miss on the next read
  (the cache lookup gates on `!= null`), so such results are recomputed rather
  than served from cache.
- `TaskExec` schedules a timer to evict each entry after `expirationTimeMs`
  (a clock/timer effect); the TTL runs from insertion.
- Cancellation is not supported (no `AbortSignal`); failure is always a
  rejected promise, never a resolved error-shaped value.

### Type Parameters

#### D

`D` = `unknown`

The resolved type of the async method.

#### A

`A` *extends* `unknown`[] = `unknown`[]

The argument tuple of the original method.

### Parameters

#### originalMethod

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The async method whose results are cached.

### Returns

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The memoized async method; rejects with whatever `originalMethod`
rejects with, and additionally with a `TypeError` when no `keyResolver` is set
and the arguments are circular (the default key uses `JSON.stringify`).

### Example

```ts
class ApiClient {
  async fetchData(endpoint: string): Promise<Data> {
    const response = await fetch(endpoint);
    return response.json();
  }
}

const client = new ApiClient();

// Basic memoization.
const memoized = memoizeAsyncFn(client.fetchData.bind(client));

// Concurrent calls share the same promise.
const promise1 = memoized("/api/data");
const promise2 = memoized("/api/data");
const [data1, data2] = await Promise.all([promise1, promise2]);

// With a TTL of 60 seconds.
const withTTL = memoizeAsyncFn(client.fetchData.bind(client), 60000);

// With a custom config.
const withConfig = memoizeAsyncFn(client.fetchData.bind(client), {
  cache: new Map(),
  keyResolver: (endpoint) => endpoint,
  expirationTimeMs: 300000,
});
```

## Call Signature

&gt; **memoizeAsyncFn**\<`T`, `D`, `A`\>(`originalMethod`, `config`): [`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

Defined in: [memoize-async/memoize-async.fn.ts:93](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize-async/memoize-async.fn.ts#L93)

Wrap a promise-returning method so results are cached and concurrent calls are
deduplicated (function form of memoizeAsync).

While a call is in flight, further calls with the same key share its promise;
the resolved value is then cached for later lookups. The second argument omits
to cache forever, is a number for a TTL in milliseconds, or an
[AsyncMemoizeConfig](../../memoize-async.types/interfaces/AsyncMemoizeConfig) for a custom cache, key resolver, and/or expiry.

Concurrency and failure contract:
- Concurrent same-key calls resolve or reject together — they share one
  in-flight promise, which is cleared once it settles (success or failure), so
  a rejection is not cached and the next call re-runs the method.
- A resolved value of `null`/`undefined` is treated as a miss on the next read
  (the cache lookup gates on `!= null`), so such results are recomputed rather
  than served from cache.
- `TaskExec` schedules a timer to evict each entry after `expirationTimeMs`
  (a clock/timer effect); the TTL runs from insertion.
- Cancellation is not supported (no `AbortSignal`); failure is always a
  rejected promise, never a resolved error-shaped value.

### Type Parameters

#### T

`T` = `unknown`

The class type a `keyof T` key resolver resolves against.

#### D

`D` = `unknown`

The resolved type of the async method.

#### A

`A` *extends* `unknown`[] = `unknown`[]

The argument tuple of the original method.

### Parameters

#### originalMethod

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The async method whose results are cached.

#### config

[`AsyncMemoizeConfig`](../../memoize-async.types/interfaces/AsyncMemoizeConfig)\<`T`, `D`\>

### Returns

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The memoized async method; rejects with whatever `originalMethod`
rejects with, and additionally with a `TypeError` when no `keyResolver` is set
and the arguments are circular (the default key uses `JSON.stringify`).

### Example

```ts
class ApiClient {
  async fetchData(endpoint: string): Promise<Data> {
    const response = await fetch(endpoint);
    return response.json();
  }
}

const client = new ApiClient();

// Basic memoization.
const memoized = memoizeAsyncFn(client.fetchData.bind(client));

// Concurrent calls share the same promise.
const promise1 = memoized("/api/data");
const promise2 = memoized("/api/data");
const [data1, data2] = await Promise.all([promise1, promise2]);

// With a TTL of 60 seconds.
const withTTL = memoizeAsyncFn(client.fetchData.bind(client), 60000);

// With a custom config.
const withConfig = memoizeAsyncFn(client.fetchData.bind(client), {
  cache: new Map(),
  keyResolver: (endpoint) => endpoint,
  expirationTimeMs: 300000,
});
```

## Call Signature

&gt; **memoizeAsyncFn**\<`D`, `A`\>(`originalMethod`, `expirationTimeMs`): [`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

Defined in: [memoize-async/memoize-async.fn.ts:97](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize-async/memoize-async.fn.ts#L97)

Wrap a promise-returning method so results are cached and concurrent calls are
deduplicated (function form of memoizeAsync).

While a call is in flight, further calls with the same key share its promise;
the resolved value is then cached for later lookups. The second argument omits
to cache forever, is a number for a TTL in milliseconds, or an
[AsyncMemoizeConfig](../../memoize-async.types/interfaces/AsyncMemoizeConfig) for a custom cache, key resolver, and/or expiry.

Concurrency and failure contract:
- Concurrent same-key calls resolve or reject together — they share one
  in-flight promise, which is cleared once it settles (success or failure), so
  a rejection is not cached and the next call re-runs the method.
- A resolved value of `null`/`undefined` is treated as a miss on the next read
  (the cache lookup gates on `!= null`), so such results are recomputed rather
  than served from cache.
- `TaskExec` schedules a timer to evict each entry after `expirationTimeMs`
  (a clock/timer effect); the TTL runs from insertion.
- Cancellation is not supported (no `AbortSignal`); failure is always a
  rejected promise, never a resolved error-shaped value.

### Type Parameters

#### D

`D` = `unknown`

The resolved type of the async method.

#### A

`A` *extends* `unknown`[] = `unknown`[]

The argument tuple of the original method.

### Parameters

#### originalMethod

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The async method whose results are cached.

#### expirationTimeMs

`number`

### Returns

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The memoized async method; rejects with whatever `originalMethod`
rejects with, and additionally with a `TypeError` when no `keyResolver` is set
and the arguments are circular (the default key uses `JSON.stringify`).

### Example

```ts
class ApiClient {
  async fetchData(endpoint: string): Promise<Data> {
    const response = await fetch(endpoint);
    return response.json();
  }
}

const client = new ApiClient();

// Basic memoization.
const memoized = memoizeAsyncFn(client.fetchData.bind(client));

// Concurrent calls share the same promise.
const promise1 = memoized("/api/data");
const promise2 = memoized("/api/data");
const [data1, data2] = await Promise.all([promise1, promise2]);

// With a TTL of 60 seconds.
const withTTL = memoizeAsyncFn(client.fetchData.bind(client), 60000);

// With a custom config.
const withConfig = memoizeAsyncFn(client.fetchData.bind(client), {
  cache: new Map(),
  keyResolver: (endpoint) => endpoint,
  expirationTimeMs: 300000,
});
```
