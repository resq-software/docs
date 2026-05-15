# Function: readonly()

> **readonly**\<`T`\>(): [`Readonlyable`](../../readonly.types/type-aliases/Readonlyable)\<`T`\>

Defined in: [readonly/readonly.ts:52](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/readonly/readonly.ts#L52)

Decorator that makes a method read-only (non-writable).
Prevents the method from being reassigned after class instantiation.

## Type Parameters

### T

`T` = `any`

The type of the class containing the decorated method

## Returns

[`Readonlyable`](../../readonly.types/type-aliases/Readonlyable)\<`T`\>

The decorator function

## Example

```typescript
class SecureApi {
  @readonly()
  authenticate(): Promise<AuthToken> {
    return this.performAuth();
  }

  @readonly()
  getBaseUrl(): string {
    return 'https://api.example.com';
  }
}

const api = new SecureApi();

// These will throw TypeError
// api.authenticate = () => Promise.resolve(fakeToken);
// api.getBaseUrl = () => 'https://evil.com';

// Calling the methods works normally
const token = await api.authenticate();
const url = api.getBaseUrl();
```
