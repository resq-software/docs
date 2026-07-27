# Function: isWebp()

&gt; **isWebp**(`view`): `boolean`

Defined in: [packages/helpers/src/browser/media/webp.ts:45](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/webp.ts#L45)

**`Internal`**

Determines whether a byte array represents a WebP image by checking the WebP file signature.

## Parameters

### view

`Uint8Array`

The Uint8Array containing the potential WebP image data

## Returns

`boolean`

True if the byte array is a valid WebP image, false otherwise

## Example

```ts
// Check if file data is WebP format
const file = new File([...], 'image.webp', { type: 'image/webp' })
const buffer = await file.arrayBuffer()
const view = new Uint8Array(buffer)
const isWebPImage = isWebp(view)
console.log(isWebPImage ? 'Valid WebP' : 'Not WebP')
```
