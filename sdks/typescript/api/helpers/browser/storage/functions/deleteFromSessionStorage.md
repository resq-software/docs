# Function: deleteFromSessionStorage()

&gt; **deleteFromSessionStorage**(`key`): `void`

Defined in: [packages/helpers/src/browser/storage.ts:167](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/storage.ts#L167)

**`Internal`**

Remove a value from session storage. Will not throw an error if sessionStorage is not available.

## Parameters

### key

`string`

The key to remove.

## Returns

`void`

## Example

```ts
deleteFromSessionStorage('temp-data')
// Value is now removed from sessionStorage
```
