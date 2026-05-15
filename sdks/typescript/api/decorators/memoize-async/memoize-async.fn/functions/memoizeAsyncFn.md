# Function: memoizeAsyncFn()

## Call Signature

> **memoizeAsyncFn**\<`D`, `A`\>(`originalMethod`): [`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

Defined in: [memoize-async/memoize-async.fn.ts:80](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/memoize-async/memoize-async.fn.ts#L80)

Wraps an async method to cache its results and deduplicate concurrent calls.

### Type Parameters

#### D

`D` = `any`

The resolved type of the async method

#### A

`A` *extends* `any`[] = `any`[]

The argument types of the original method

### Parameters

#### originalMethod

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The async method to memoize

### Returns

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The memoized method

### Example

```typescript
class ApiClient {
  async fetchData(endpoint: string): Promise<Data> {
    const response = await fetch(endpoint);
    return response.json();
  }
}

const client = new ApiClient();

// Basic memoization
const memoized = memoizeAsyncFn(client.fetchData.bind(client));

// Concurrent calls share the same promise
const promise1 = memoized('/api/data');
const promise2 = memoized('/api/data'); // Same promise as above
const [data1, data2] = await Promise.all([promise1, promise2]);

// With TTL
const withTTL = memoizeAsyncFn(
  client.fetchData.bind(client),
  60000 // Cache for 60 seconds
);

// With custom config
const withConfig = memoizeAsyncFn(
  client.fetchData.bind(client),
  {
    cache: new Map(),
    keyResolver: (endpoint) => endpoint,
    expirationTimeMs: 300000
  }
);
```

## Call Signature

> **memoizeAsyncFn**\<`D`, `A`\>(`originalMethod`, `config`): [`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

Defined in: [memoize-async/memoize-async.fn.ts:83](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/memoize-async/memoize-async.fn.ts#L83)

Wraps an async method to cache its results and deduplicate concurrent calls.

### Type Parameters

#### D

`D` = `any`

The resolved type of the async method

#### A

`A` *extends* `any`[] = `any`[]

The argument types of the original method

### Parameters

#### originalMethod

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The async method to memoize

#### config

[`AsyncMemoizeConfig`](../../memoize-async.types/interfaces/AsyncMemoizeConfig)\<`any`, `D`\>

Configuration for memoization

### Returns

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The memoized method

### Example

```typescript
class ApiClient {
  async fetchData(endpoint: string): Promise<Data> {
    const response = await fetch(endpoint);
    return response.json();
  }
}

const client = new ApiClient();

// Basic memoization
const memoized = memoizeAsyncFn(client.fetchData.bind(client));

// Concurrent calls share the same promise
const promise1 = memoized('/api/data');
const promise2 = memoized('/api/data'); // Same promise as above
const [data1, data2] = await Promise.all([promise1, promise2]);

// With TTL
const withTTL = memoizeAsyncFn(
  client.fetchData.bind(client),
  60000 // Cache for 60 seconds
);

// With custom config
const withConfig = memoizeAsyncFn(
  client.fetchData.bind(client),
  {
    cache: new Map(),
    keyResolver: (endpoint) => endpoint,
    expirationTimeMs: 300000
  }
);
```

## Call Signature

> **memoizeAsyncFn**\<`D`, `A`\>(`originalMethod`, `expirationTimeMs`): [`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

Defined in: [memoize-async/memoize-async.fn.ts:87](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/memoize-async/memoize-async.fn.ts#L87)

Wraps an async method to cache its results and deduplicate concurrent calls.

### Type Parameters

#### D

`D` = `any`

The resolved type of the async method

#### A

`A` *extends* `any`[] = `any`[]

The argument types of the original method

### Parameters

#### originalMethod

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The async method to memoize

#### expirationTimeMs

`number`

Cache expiration time in milliseconds

### Returns

[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`, `A`\>

The memoized method

### Example

```typescript
class ApiClient {
  async fetchData(endpoint: string): Promise<Data> {
    const response = await fetch(endpoint);
    return response.json();
  }
}

const client = new ApiClient();

// Basic memoization
const memoized = memoizeAsyncFn(client.fetchData.bind(client));

// Concurrent calls share the same promise
const promise1 = memoized('/api/data');
const promise2 = memoized('/api/data'); // Same promise as above
const [data1, data2] = await Promise.all([promise1, promise2]);

// With TTL
const withTTL = memoizeAsyncFn(
  client.fetchData.bind(client),
  60000 // Cache for 60 seconds
);

// With custom config
const withConfig = memoizeAsyncFn(
  client.fetchData.bind(client),
  {
    cache: new Map(),
    keyResolver: (endpoint) => endpoint,
    expirationTimeMs: 300000
  }
);
```
