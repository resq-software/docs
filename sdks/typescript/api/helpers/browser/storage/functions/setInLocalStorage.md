# Function: setInLocalStorage()

&gt; **setInLocalStorage**(`key`, `value`): `void`

Defined in: [packages/helpers/src/browser/storage.ts:65](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/storage.ts#L65)

**`Internal`**

Set a value in local storage. Will not throw an error if localStorage is not available.

## Parameters

### key

`string`

The key to set.

### value

`string`

The value to set.

## Returns

`void`

## Example

```ts
const preferences = { theme: 'dark', language: 'en' }
setInLocalStorage('user-preferences', JSON.stringify(preferences))
```
