# Function: getFromLocalStorage()

&gt; **getFromLocalStorage**(`key`): `string` \| `null`

Defined in: [packages/helpers/src/browser/storage.ts:45](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/storage.ts#L45)

**`Internal`**

Get a value from local storage.

## Parameters

### key

`string`

The key to get.

## Returns

`string` \| `null`

The stored value as a string, or null if not found or storage is unavailable.

## Example

```ts
const userTheme = getFromLocalStorage('user-theme')
if (userTheme) {
  console.log('Stored theme:', userTheme)
}
```
