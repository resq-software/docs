# Function: deleteFromLocalStorage()

&gt; **deleteFromLocalStorage**(`key`): `void`

Defined in: [packages/helpers/src/browser/storage.ts:84](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/storage.ts#L84)

**`Internal`**

Remove a value from local storage. Will not throw an error if localStorage is not available.

## Parameters

### key

`string`

The key to remove.

## Returns

`void`

## Example

```ts
deleteFromLocalStorage('user-preferences')
// Value is now removed from localStorage
```
