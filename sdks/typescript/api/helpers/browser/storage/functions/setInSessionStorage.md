# Function: setInSessionStorage()

&gt; **setInSessionStorage**(`key`, `value`): `void`

Defined in: [packages/helpers/src/browser/storage.ts:148](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/storage.ts#L148)

**`Internal`**

Set a value in session storage. Will not throw an error if sessionStorage is not available.

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
setInSessionStorage('current-tool', 'select')
setInSessionStorage('temp-data', JSON.stringify({ x: 100, y: 200 }))
```
