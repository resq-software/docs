# Function: memoizeAsync()

## Call Signature

&gt; **memoizeAsync**\<`T`\>(): [`AsyncDecorator`](../../../types/type-aliases/AsyncDecorator)\<`T`\>

Defined in: [memoize-async/memoize-async.ts:88](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize-async/memoize-async.ts#L88)

Cache a promise-returning method's results by their arguments and deduplicate
concurrent calls: identical calls share one promise until the first resolves.

Call with no argument to cache forever, a number for a TTL in milliseconds, or
an [AsyncMemoizeConfig](../../memoize-async.types/interfaces/AsyncMemoizeConfig) for a custom cache, key resolver, and/or expiry.

The cache and in-flight promise map are built once, at decoration time, so both
the cached values and the concurrent-call deduplication are shared across every
instance of the class. Failure surfaces as a rejected promise — a rejection is
shared by all callers deduped onto the same in-flight promise, and the entry is
then cleared so a later call retries rather than replaying the error. Only
resolved values are cached; rejections are not. Cancellation is not supported
(no `AbortSignal`). Mutates the supplied property descriptor in place.

### Type Parameters

#### T

`T` = `unknown`

The class type that owns the decorated method.

### Returns

[`AsyncDecorator`](../../../types/type-aliases/AsyncDecorator)\<`T`\>

The async method decorator.

### Throws

If applied to a member without a `value` descriptor (an
accessor or plain property rather than a method).

### Example

```ts
class DataService {
  // Basic usage — caches indefinitely.
  @memoizeAsync()
  async fetchConfig(): Promise<Config> {
    return fetch("/api/config").then((r) => r.json());
  }

  // With a TTL of 60 seconds.
  @memoizeAsync(60000)
  async getExchangeRates(): Promise<Rates> {
    return fetch("/api/rates").then((r) => r.json());
  }

  // With a custom cache and key resolver.
  @memoizeAsync({
    cache: new RedisCache<string, Product>(),
    keyResolver: (productId, includeDetails) =>
      `product-${productId}-${includeDetails}`,
    expirationTimeMs: 300000,
  })
  async getProduct(productId: string, includeDetails: boolean): Promise<Product> {
    return this.fetchProduct(productId, includeDetails);
  }
}

const service = new DataService();

// Concurrent calls with the same args share one promise.
const [product1, product2] = await Promise.all([
  service.getProduct("123", true),
  service.getProduct("123", true),
]);
```

### See

[memoize](../../../memoize) for synchronous methods.

## Call Signature

&gt; **memoizeAsync**\<`T`, `D`\>(`config`): [`AsyncDecorator`](../../../types/type-aliases/AsyncDecorator)\<`T`\>

Defined in: [memoize-async/memoize-async.ts:89](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize-async/memoize-async.ts#L89)

Cache a promise-returning method's results by their arguments and deduplicate
concurrent calls: identical calls share one promise until the first resolves.

Call with no argument to cache forever, a number for a TTL in milliseconds, or
an [AsyncMemoizeConfig](../../memoize-async.types/interfaces/AsyncMemoizeConfig) for a custom cache, key resolver, and/or expiry.

The cache and in-flight promise map are built once, at decoration time, so both
the cached values and the concurrent-call deduplication are shared across every
instance of the class. Failure surfaces as a rejected promise — a rejection is
shared by all callers deduped onto the same in-flight promise, and the entry is
then cleared so a later call retries rather than replaying the error. Only
resolved values are cached; rejections are not. Cancellation is not supported
(no `AbortSignal`). Mutates the supplied property descriptor in place.

### Type Parameters

#### T

`T` = `unknown`

The class type that owns the decorated method.

#### D

`D` = `unknown`

The resolved type of the async method.

### Parameters

#### config

[`AsyncMemoizeConfig`](../../memoize-async.types/interfaces/AsyncMemoizeConfig)\<`T`, `D`\>

### Returns

[`AsyncDecorator`](../../../types/type-aliases/AsyncDecorator)\<`T`\>

The async method decorator.

### Throws

If applied to a member without a `value` descriptor (an
accessor or plain property rather than a method).

### Example

```ts
class DataService {
  // Basic usage — caches indefinitely.
  @memoizeAsync()
  async fetchConfig(): Promise<Config> {
    return fetch("/api/config").then((r) => r.json());
  }

  // With a TTL of 60 seconds.
  @memoizeAsync(60000)
  async getExchangeRates(): Promise<Rates> {
    return fetch("/api/rates").then((r) => r.json());
  }

  // With a custom cache and key resolver.
  @memoizeAsync({
    cache: new RedisCache<string, Product>(),
    keyResolver: (productId, includeDetails) =>
      `product-${productId}-${includeDetails}`,
    expirationTimeMs: 300000,
  })
  async getProduct(productId: string, includeDetails: boolean): Promise<Product> {
    return this.fetchProduct(productId, includeDetails);
  }
}

const service = new DataService();

// Concurrent calls with the same args share one promise.
const [product1, product2] = await Promise.all([
  service.getProduct("123", true),
  service.getProduct("123", true),
]);
```

### See

[memoize](../../../memoize) for synchronous methods.

## Call Signature

&gt; **memoizeAsync**\<`T`\>(`expirationTimeMs`): [`AsyncDecorator`](../../../types/type-aliases/AsyncDecorator)\<`T`\>

Defined in: [memoize-async/memoize-async.ts:92](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/memoize-async/memoize-async.ts#L92)

Cache a promise-returning method's results by their arguments and deduplicate
concurrent calls: identical calls share one promise until the first resolves.

Call with no argument to cache forever, a number for a TTL in milliseconds, or
an [AsyncMemoizeConfig](../../memoize-async.types/interfaces/AsyncMemoizeConfig) for a custom cache, key resolver, and/or expiry.

The cache and in-flight promise map are built once, at decoration time, so both
the cached values and the concurrent-call deduplication are shared across every
instance of the class. Failure surfaces as a rejected promise — a rejection is
shared by all callers deduped onto the same in-flight promise, and the entry is
then cleared so a later call retries rather than replaying the error. Only
resolved values are cached; rejections are not. Cancellation is not supported
(no `AbortSignal`). Mutates the supplied property descriptor in place.

### Type Parameters

#### T

`T` = `unknown`

The class type that owns the decorated method.

### Parameters

#### expirationTimeMs

`number`

### Returns

[`AsyncDecorator`](../../../types/type-aliases/AsyncDecorator)\<`T`\>

The async method decorator.

### Throws

If applied to a member without a `value` descriptor (an
accessor or plain property rather than a method).

### Example

```ts
class DataService {
  // Basic usage — caches indefinitely.
  @memoizeAsync()
  async fetchConfig(): Promise<Config> {
    return fetch("/api/config").then((r) => r.json());
  }

  // With a TTL of 60 seconds.
  @memoizeAsync(60000)
  async getExchangeRates(): Promise<Rates> {
    return fetch("/api/rates").then((r) => r.json());
  }

  // With a custom cache and key resolver.
  @memoizeAsync({
    cache: new RedisCache<string, Product>(),
    keyResolver: (productId, includeDetails) =>
      `product-${productId}-${includeDetails}`,
    expirationTimeMs: 300000,
  })
  async getProduct(productId: string, includeDetails: boolean): Promise<Product> {
    return this.fetchProduct(productId, includeDetails);
  }
}

const service = new DataService();

// Concurrent calls with the same args share one promise.
const [product1, product2] = await Promise.all([
  service.getProduct("123", true),
  service.getProduct("123", true),
]);
```

### See

[memoize](../../../memoize) for synchronous methods.
