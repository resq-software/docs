# Function: readonly()

&gt; **readonly**\<`T`\>(): [`Readonlyable`](../../readonly.types/type-aliases/Readonlyable)\<`T`\>

Defined in: [readonly/readonly.ts:62](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/readonly/readonly.ts#L62)

Mark a method read-only by setting its property descriptor's `writable` flag to
`false`, so it cannot be reassigned after the class is instantiated.

Returns a new descriptor object rather than mutating the one passed in. Intended
for method (value) descriptors — `writable` has no effect on accessor
descriptors. A blocked reassignment throws a `TypeError` in strict-mode code
(including class bodies and ES modules) and fails silently otherwise.

## Type Parameters

### T

`T` = `unknown`

The class type that owns the decorated method.

## Returns

[`Readonlyable`](../../readonly.types/type-aliases/Readonlyable)\<`T`\>

The method decorator.

## Example

```ts
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
