# Function: clearSessionStorage()

&gt; **clearSessionStorage**(): `void`

Defined in: [packages/helpers/src/browser/storage.ts:185](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/storage.ts#L185)

**`Internal`**

Clear all values from session storage. Will not throw an error if sessionStorage is not available.

## Returns

`void`

## Example

```ts
clearSessionStorage()
// All sessionStorage data is now cleared
```
