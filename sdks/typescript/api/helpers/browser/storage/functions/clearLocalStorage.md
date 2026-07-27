# Function: clearLocalStorage()

&gt; **clearLocalStorage**(): `void`

Defined in: [packages/helpers/src/browser/storage.ts:102](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/storage.ts#L102)

**`Internal`**

Clear all values from local storage. Will not throw an error if localStorage is not available.

## Returns

`void`

## Example

```ts
clearLocalStorage()
// All localStorage data is now cleared
```
