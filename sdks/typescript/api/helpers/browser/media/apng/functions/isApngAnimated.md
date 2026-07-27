# Function: isApngAnimated()

&gt; **isApngAnimated**(`buffer`): `boolean`

Defined in: [packages/helpers/src/browser/media/apng.ts:58](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/apng.ts#L58)

Determines whether an ArrayBuffer contains an animated PNG (APNG) image.

This function checks if the provided buffer contains a valid PNG file with animation
control chunks (acTL) that precede the image data chunks (IDAT), which indicates
it's an animated PNG rather than a static PNG.

## Parameters

### buffer

`ArrayBuffer`

The ArrayBuffer containing the image data to analyze

## Returns

`boolean`

True if the buffer contains an animated PNG, false otherwise

## Examples

```ts
// Check if an uploaded file contains an animated PNG
if (file.type === 'image/apng') {
  const isAnimated = isApngAnimated(await file.arrayBuffer())
  console.log(isAnimated ? 'Animated PNG' : 'Static PNG')
}
```

```ts
// Use with fetch to check remote images
const response = await fetch('image.png')
const buffer = await response.arrayBuffer()
const hasAnimation = isApngAnimated(buffer)
```
