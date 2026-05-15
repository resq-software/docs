# Function: memoizeAsync()

## Call Signature

> **memoizeAsync**\<`T`, `D`\>(): [`AsyncMemoizable`](../../memoize-async.types/type-aliases/AsyncMemoizable)\<`T`, `D`\>

Defined in: [memoize-async/memoize-async.ts:105](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/memoize-async/memoize-async.ts#L105)

Decorator that caches async method results based on their arguments.
Prevents duplicate concurrent requests by returning the same promise
for identical calls until the first one resolves.

### Type Parameters

#### T

`T` = `any`

The type of the class containing the decorated method

#### D

`D` = `any`

The resolved type of the async method

### Returns

[`AsyncMemoizable`](../../memoize-async.types/type-aliases/AsyncMemoizable)\<`T`, `D`\>

The decorator function

### Throws

When applied to a non-method property

### Example

```typescript
class DataService {
  // Basic usage - caches indefinitely
  @memoizeAsync()
  async fetchConfig(): Promise<Config> {
    return fetch('/api/config').then(r => r.json());
  }

  // With TTL
  @memoizeAsync(60000) // Cache for 60 seconds
  async getExchangeRates(): Promise<Rates> {
    return fetch('/api/rates').then(r => r.json());
  }

  // With custom cache and key resolver
  @memoizeAsync({
    cache: new RedisCache<string, Product>(),
    keyResolver: (productId, includeDetails) => `product-${productId}-${includeDetails}`,
    expirationTimeMs: 300000
  })
  async getProduct(productId: string, includeDetails: boolean): Promise<Product> {
    return this.fetchProduct(productId, includeDetails);
  }
}

const service = new DataService();

// Concurrent calls with same args share the same promise
const [product1, product2] = await Promise.all([
  service.getProduct('123', true),
  service.getProduct('123', true) // Same promise as above
]);
```

## Call Signature

> **memoizeAsync**\<`T`, `D`\>(`config`): [`AsyncMemoizable`](../../memoize-async.types/type-aliases/AsyncMemoizable)\<`T`, `D`\>

Defined in: [memoize-async/memoize-async.ts:106](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/memoize-async/memoize-async.ts#L106)

Decorator that caches async method results based on their arguments.
Prevents duplicate concurrent requests by returning the same promise
for identical calls until the first one resolves.

### Type Parameters

#### T

`T` = `any`

The type of the class containing the decorated method

#### D

`D` = `any`

The resolved type of the async method

### Parameters

#### config

[`AsyncMemoizeConfig`](../../memoize-async.types/interfaces/AsyncMemoizeConfig)\<`T`, `D`\>

Configuration for memoization

### Returns

[`AsyncMemoizable`](../../memoize-async.types/type-aliases/AsyncMemoizable)\<`T`, `D`\>

The decorator function

### Throws

When applied to a non-method property

### Example

```typescript
class DataService {
  // Basic usage - caches indefinitely
  @memoizeAsync()
  async fetchConfig(): Promise<Config> {
    return fetch('/api/config').then(r => r.json());
  }

  // With TTL
  @memoizeAsync(60000) // Cache for 60 seconds
  async getExchangeRates(): Promise<Rates> {
    return fetch('/api/rates').then(r => r.json());
  }

  // With custom cache and key resolver
  @memoizeAsync({
    cache: new RedisCache<string, Product>(),
    keyResolver: (productId, includeDetails) => `product-${productId}-${includeDetails}`,
    expirationTimeMs: 300000
  })
  async getProduct(productId: string, includeDetails: boolean): Promise<Product> {
    return this.fetchProduct(productId, includeDetails);
  }
}

const service = new DataService();

// Concurrent calls with same args share the same promise
const [product1, product2] = await Promise.all([
  service.getProduct('123', true),
  service.getProduct('123', true) // Same promise as above
]);
```

## Call Signature

> **memoizeAsync**\<`T`, `D`\>(`expirationTimeMs`): [`AsyncMemoizable`](../../memoize-async.types/type-aliases/AsyncMemoizable)\<`T`, `D`\>

Defined in: [memoize-async/memoize-async.ts:109](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/memoize-async/memoize-async.ts#L109)

Decorator that caches async method results based on their arguments.
Prevents duplicate concurrent requests by returning the same promise
for identical calls until the first one resolves.

### Type Parameters

#### T

`T` = `any`

The type of the class containing the decorated method

#### D

`D` = `any`

The resolved type of the async method

### Parameters

#### expirationTimeMs

`number`

Cache expiration time in milliseconds

### Returns

[`AsyncMemoizable`](../../memoize-async.types/type-aliases/AsyncMemoizable)\<`T`, `D`\>

The decorator function

### Throws

When applied to a non-method property

### Example

```typescript
class DataService {
  // Basic usage - caches indefinitely
  @memoizeAsync()
  async fetchConfig(): Promise<Config> {
    return fetch('/api/config').then(r => r.json());
  }

  // With TTL
  @memoizeAsync(60000) // Cache for 60 seconds
  async getExchangeRates(): Promise<Rates> {
    return fetch('/api/rates').then(r => r.json());
  }

  // With custom cache and key resolver
  @memoizeAsync({
    cache: new RedisCache<string, Product>(),
    keyResolver: (productId, includeDetails) => `product-${productId}-${includeDetails}`,
    expirationTimeMs: 300000
  })
  async getProduct(productId: string, includeDetails: boolean): Promise<Product> {
    return this.fetchProduct(productId, includeDetails);
  }
}

const service = new DataService();

// Concurrent calls with same args share the same promise
const [product1, product2] = await Promise.all([
  service.getProduct('123', true),
  service.getProduct('123', true) // Same promise as above
]);
```
