# Function: delegate()

> **delegate**\<`T`, `D`\>(`keyResolver?`): [`Delegatable`](../../delegate.types/type-aliases/Delegatable)\<`T`, `D`\>

Defined in: [delegate/delegate.ts:90](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/delegate/delegate.ts#L90)

Decorator that deduplicates concurrent async method calls.
Multiple calls with the same arguments will share the same promise
until the first one resolves or rejects.

## Type Parameters

### T

`T` = `any`

The type of the class containing the decorated method

### D

`D` = `any`

The return type of the decorated method (wrapped in Promise)

## Parameters

### keyResolver?

(...`args`) => `string`

Optional function to generate cache keys from arguments

## Returns

[`Delegatable`](../../delegate.types/type-aliases/Delegatable)\<`T`, `D`\>

The decorator function

## Throws

When applied to a non-method property

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
