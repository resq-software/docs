# Function: memoize()

## Call Signature

> **memoize**\<`T`, `D`\>(): [`Memoizable`](../../memoize.types/type-aliases/Memoizable)\<`T`, `D`\>

Defined in: [memoize/memoize.ts:121](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/memoize/memoize.ts#L121)

Decorator that caches method results based on their arguments.
Subsequent calls with the same arguments return the cached result.

### Type Parameters

#### T

`T` = `any`

The type of the class containing the decorated method

#### D

`D` = `any`

The return type of the decorated method

### Returns

[`Memoizable`](../../memoize.types/type-aliases/Memoizable)\<`T`, `D`\>

The decorator function

### Throws

When applied to a non-method property

### Example

```typescript
class DataService {
  // Basic usage - caches indefinitely
  @memoize()
  getUser(id: string): User {
    return this.database.findUser(id);
  }

  // With TTL (time to live)
  @memoize(60000) // Cache for 60 seconds
  getConfig(): Config {
    return this.loadConfig();
  }

  // With custom cache and key resolver
  @memoize({
    cache: new LRUCache<string, User>(100),
    keyResolver: (userId, includeDetails) => `${userId}-${includeDetails}`,
    expirationTimeMs: 300000 // 5 minutes
  })
  getUserWithDetails(userId: string, includeDetails: boolean): User {
    return this.fetchUser(userId, includeDetails);
  }
}

const service = new DataService();

// First call executes the method
const user1 = service.getUser('123');

// Second call with same argument returns cached result
const user2 = service.getUser('123'); // Instant, no database query
```

## Call Signature

> **memoize**\<`T`, `D`\>(`config`): [`Memoizable`](../../memoize.types/type-aliases/Memoizable)\<`T`, `D`\>

Defined in: [memoize/memoize.ts:122](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/memoize/memoize.ts#L122)

Decorator that caches method results based on their arguments.
Subsequent calls with the same arguments return the cached result.

### Type Parameters

#### T

`T` = `any`

The type of the class containing the decorated method

#### D

`D` = `any`

The return type of the decorated method

### Parameters

#### config

[`MemoizeConfig`](../../memoize.types/interfaces/MemoizeConfig)\<`T`, `D`\>

Configuration for memoization

### Returns

[`Memoizable`](../../memoize.types/type-aliases/Memoizable)\<`T`, `D`\>

The decorator function

### Throws

When applied to a non-method property

### Example

```typescript
class DataService {
  // Basic usage - caches indefinitely
  @memoize()
  getUser(id: string): User {
    return this.database.findUser(id);
  }

  // With TTL (time to live)
  @memoize(60000) // Cache for 60 seconds
  getConfig(): Config {
    return this.loadConfig();
  }

  // With custom cache and key resolver
  @memoize({
    cache: new LRUCache<string, User>(100),
    keyResolver: (userId, includeDetails) => `${userId}-${includeDetails}`,
    expirationTimeMs: 300000 // 5 minutes
  })
  getUserWithDetails(userId: string, includeDetails: boolean): User {
    return this.fetchUser(userId, includeDetails);
  }
}

const service = new DataService();

// First call executes the method
const user1 = service.getUser('123');

// Second call with same argument returns cached result
const user2 = service.getUser('123'); // Instant, no database query
```

## Call Signature

> **memoize**\<`T`, `D`\>(`expirationTimeMs`): [`Memoizable`](../../memoize.types/type-aliases/Memoizable)\<`T`, `D`\>

Defined in: [memoize/memoize.ts:123](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/memoize/memoize.ts#L123)

Decorator that caches method results based on their arguments.
Subsequent calls with the same arguments return the cached result.

### Type Parameters

#### T

`T` = `any`

The type of the class containing the decorated method

#### D

`D` = `any`

The return type of the decorated method

### Parameters

#### expirationTimeMs

`number`

Cache expiration time in milliseconds

### Returns

[`Memoizable`](../../memoize.types/type-aliases/Memoizable)\<`T`, `D`\>

The decorator function

### Throws

When applied to a non-method property

### Example

```typescript
class DataService {
  // Basic usage - caches indefinitely
  @memoize()
  getUser(id: string): User {
    return this.database.findUser(id);
  }

  // With TTL (time to live)
  @memoize(60000) // Cache for 60 seconds
  getConfig(): Config {
    return this.loadConfig();
  }

  // With custom cache and key resolver
  @memoize({
    cache: new LRUCache<string, User>(100),
    keyResolver: (userId, includeDetails) => `${userId}-${includeDetails}`,
    expirationTimeMs: 300000 // 5 minutes
  })
  getUserWithDetails(userId: string, includeDetails: boolean): User {
    return this.fetchUser(userId, includeDetails);
  }
}

const service = new DataService();

// First call executes the method
const user1 = service.getUser('123');

// Second call with same argument returns cached result
const user2 = service.getUser('123'); // Instant, no database query
```
