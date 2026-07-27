# Function: isWebpAnimated()

&gt; **isWebpAnimated**(`buffer`): `boolean`

Defined in: [packages/helpers/src/browser/media/webp.ts:68](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/webp.ts#L68)

Determines whether a WebP image file contains animation data by checking the animation flag in the WebP VP8X chunk.

## Parameters

### buffer

`ArrayBuffer`

The ArrayBuffer containing the WebP image data

## Returns

`boolean`

True if the WebP image is animated, false otherwise

## Example

```ts
// Check if a WebP file from user input is animated
const file = new File([...], 'image.webp', { type: 'image/webp' })
const buffer = await file.arrayBuffer()
const animated = isWebpAnimated(buffer)
console.log(animated ? 'Animated WebP' : 'Static WebP')
```
