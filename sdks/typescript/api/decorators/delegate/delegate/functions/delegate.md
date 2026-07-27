# Function: delegate()

&gt; **delegate**\<`T`, `D`\>(`keyResolver?`): [`Delegatable`](../../delegate.types/type-aliases/Delegatable)\<`T`, `D`\>

Defined in: [delegate/delegate.ts:92](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/delegate/delegate.ts#L92)

Decorator that deduplicates concurrent async method calls.
Multiple calls with the same arguments will share the same promise
until the first one resolves or rejects.

Dedup state (the in-flight-promise map) lives in the wrapper installed on the
descriptor, shared across all instances of the class. The default key is
`JSON.stringify(args)`; supply `keyResolver` for arguments that do not
serialize cleanly. See [delegateFn](../../delegate.fn/functions/delegateFn) for the settle-then-evict lifecycle
and the synchronous key-generation failure mode.

## Type Parameters

### T

`T` = `unknown`

The type of the class containing the decorated method.

### D

`D` = `unknown`

The return type of the decorated method (wrapped in a promise).

## Parameters

### keyResolver?

(...`args`) =&gt; `string`

Optional function to generate cache keys from arguments.

## Returns

[`Delegatable`](../../delegate.types/type-aliases/Delegatable)\<`T`, `D`\>

The decorator function.

## Throws

At decoration time, when applied to anything without a method
  value, with message `"@delegate is applicable only on a methods."`.

## Example

```typescript
class ApiService {
  // Basic usage - uses JSON.stringify(args) as key
  @delegate()
  async fetchData(id: string): Promise<Data> {
    return this.http.get(`/data/${id}`);
  }

  // Custom key resolver for complex arguments
  @delegate((userId, options) => `${userId}-${options.cacheKey}`)
  async getUser(userId: string, options: { cacheKey: string }): Promise<User> {
    return this.http.get(`/users/${userId}`);
  }
}

// Usage - concurrent calls with same args share the promise
const api = new ApiService();

// These share the same underlying promise
const [user1, user2] = await Promise.all([
  api.getUser('123', { cacheKey: 'v1' }),
  api.getUser('123', { cacheKey: 'v1' }) // Same key, returns cached promise
]);

// This creates a new promise (different cache key)
const user3 = await api.getUser('123', { cacheKey: 'v2' });
```
