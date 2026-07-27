# Function: getFromSessionStorage()

&gt; **getFromSessionStorage**(`key`): `string` \| `null`

Defined in: [packages/helpers/src/browser/storage.ts:128](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/storage.ts#L128)

**`Internal`**

Get a value from session storage.

## Parameters

### key

`string`

The key to get.

## Returns

`string` \| `null`

The stored value as a string, or null if not found or storage is unavailable.

## Example

```ts
const currentTool = getFromSessionStorage('current-tool')
if (currentTool) {
  console.log('Active tool:', currentTool)
}
```
