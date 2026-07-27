# Function: isGifAnimated()

&gt; **isGifAnimated**(`buffer`): `boolean`

Defined in: [packages/helpers/src/browser/media/gif.ts:74](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/gif.ts#L74)

Checks if buffer contains animated GIF image by parsing the GIF structure and counting image descriptors.
A GIF is considered animated if it contains more than one image descriptor block.

## Parameters

### buffer

`ArrayBuffer`

The ArrayBuffer containing the GIF image data

## Returns

`boolean`

True if the GIF is animated (contains multiple frames), false otherwise

## Example

```ts
// Check if a GIF file is animated
const file = event.target.files[0]
if (file.type === 'image/gif') {
  const buffer = await file.arrayBuffer()
  const animated = isGifAnimated(buffer)
  console.log(animated ? 'Animated GIF' : 'Static GIF')
}
```
