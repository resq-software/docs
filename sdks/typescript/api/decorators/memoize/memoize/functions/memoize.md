# Function: memoize()

## Call Signature

&gt; **memoize**\<`T`\>(): [`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

Defined in: [memoize/memoize.ts:82](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize/memoize.ts#L82)

Cache a synchronous method's results by their arguments; a repeat call with
the same arguments returns the cached value instead of re-running the method.

Call with no argument to cache forever, a number for a TTL in milliseconds, or
a [MemoizeConfig](../../memoize.types/interfaces/MemoizeConfig) for a custom cache, key resolver, and/or expiry.

The cache is built once, when the method is decorated, so it is shared across
every instance of the class rather than being per-instance. The default key is
`JSON.stringify` of the arguments, which omits the instance identity — calls on
different instances with equal arguments therefore collide on one entry. Supply
a `keyResolver` that encodes the instance (or per-instance state) to isolate
caches. Mutates the supplied property descriptor in place.

### Type Parameters

#### T

`T` = `unknown`

The class type that owns the decorated method.

### Returns

[`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

The method decorator.

### Throws

If applied to a member without a `value` descriptor (an
accessor or plain property rather than a method).

### Example

```ts
class DataService {
  // Basic usage — caches indefinitely.
  @memoize()
  getUser(id: string): User {
    return this.database.findUser(id);
  }

  // With a TTL of 60 seconds.
  @memoize(60000)
  getConfig(): Config {
    return this.loadConfig();
  }

  // With a custom cache and key resolver.
  @memoize({
    cache: new LRUCache<string, User>(100),
    keyResolver: (userId, includeDetails) => `${userId}-${includeDetails}`,
    expirationTimeMs: 300000,
  })
  getUserWithDetails(userId: string, includeDetails: boolean): User {
    return this.fetchUser(userId, includeDetails);
  }
}

const service = new DataService();
const user1 = service.getUser("123"); // Executes the method.
const user2 = service.getUser("123"); // Cached — no database query.
```

### See

memoizeAsync for promise-returning methods.

## Call Signature

&gt; **memoize**\<`T`, `D`\>(`config`): [`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

Defined in: [memoize/memoize.ts:83](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize/memoize.ts#L83)

Cache a synchronous method's results by their arguments; a repeat call with
the same arguments returns the cached value instead of re-running the method.

Call with no argument to cache forever, a number for a TTL in milliseconds, or
a [MemoizeConfig](../../memoize.types/interfaces/MemoizeConfig) for a custom cache, key resolver, and/or expiry.

The cache is built once, when the method is decorated, so it is shared across
every instance of the class rather than being per-instance. The default key is
`JSON.stringify` of the arguments, which omits the instance identity — calls on
different instances with equal arguments therefore collide on one entry. Supply
a `keyResolver` that encodes the instance (or per-instance state) to isolate
caches. Mutates the supplied property descriptor in place.

### Type Parameters

#### T

`T` = `unknown`

The class type that owns the decorated method.

#### D

`D` = `unknown`

The return type of the decorated method.

### Parameters

#### config

[`MemoizeConfig`](../../memoize.types/interfaces/MemoizeConfig)\<`T`, `D`\>

### Returns

[`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

The method decorator.

### Throws

If applied to a member without a `value` descriptor (an
accessor or plain property rather than a method).

### Example

```ts
class DataService {
  // Basic usage — caches indefinitely.
  @memoize()
  getUser(id: string): User {
    return this.database.findUser(id);
  }

  // With a TTL of 60 seconds.
  @memoize(60000)
  getConfig(): Config {
    return this.loadConfig();
  }

  // With a custom cache and key resolver.
  @memoize({
    cache: new LRUCache<string, User>(100),
    keyResolver: (userId, includeDetails) => `${userId}-${includeDetails}`,
    expirationTimeMs: 300000,
  })
  getUserWithDetails(userId: string, includeDetails: boolean): User {
    return this.fetchUser(userId, includeDetails);
  }
}

const service = new DataService();
const user1 = service.getUser("123"); // Executes the method.
const user2 = service.getUser("123"); // Cached — no database query.
```

### See

memoizeAsync for promise-returning methods.

## Call Signature

&gt; **memoize**\<`T`\>(`expirationTimeMs`): [`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

Defined in: [memoize/memoize.ts:84](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/memoize/memoize.ts#L84)

Cache a synchronous method's results by their arguments; a repeat call with
the same arguments returns the cached value instead of re-running the method.

Call with no argument to cache forever, a number for a TTL in milliseconds, or
a [MemoizeConfig](../../memoize.types/interfaces/MemoizeConfig) for a custom cache, key resolver, and/or expiry.

The cache is built once, when the method is decorated, so it is shared across
every instance of the class rather than being per-instance. The default key is
`JSON.stringify` of the arguments, which omits the instance identity — calls on
different instances with equal arguments therefore collide on one entry. Supply
a `keyResolver` that encodes the instance (or per-instance state) to isolate
caches. Mutates the supplied property descriptor in place.

### Type Parameters

#### T

`T` = `unknown`

The class type that owns the decorated method.

### Parameters

#### expirationTimeMs

`number`

### Returns

[`Decorator`](../../../types/type-aliases/Decorator)\<`T`\>

The method decorator.

### Throws

If applied to a member without a `value` descriptor (an
accessor or plain property rather than a method).

### Example

```ts
class DataService {
  // Basic usage — caches indefinitely.
  @memoize()
  getUser(id: string): User {
    return this.database.findUser(id);
  }

  // With a TTL of 60 seconds.
  @memoize(60000)
  getConfig(): Config {
    return this.loadConfig();
  }

  // With a custom cache and key resolver.
  @memoize({
    cache: new LRUCache<string, User>(100),
    keyResolver: (userId, includeDetails) => `${userId}-${includeDetails}`,
    expirationTimeMs: 300000,
  })
  getUserWithDetails(userId: string, includeDetails: boolean): User {
    return this.fetchUser(userId, includeDetails);
  }
}

const service = new DataService();
const user1 = service.getUser("123"); // Executes the method.
const user2 = service.getUser("123"); // Cached — no database query.
```

### See

memoizeAsync for promise-returning methods.
