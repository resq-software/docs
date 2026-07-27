# Function: isAvifAnimated()

&gt; **isAvifAnimated**(`buffer`): `boolean`

Defined in: [packages/helpers/src/browser/media/avif.ts:95](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/avif.ts#L95)

Determines whether an ArrayBuffer contains an animated AVIF image.

AVIF is an ISOBMFF container. This function parses the leading `ftyp` box and
conservatively reports an animation only when an image-sequence brand
(`"avis"` or `"msf1"`) is present in either the major brand or the list of
compatible brands. It never reads past the buffer or the declared `ftyp` box
size, and prefers false-negatives over false-positives.

## Parameters

### buffer

`ArrayBuffer`

The ArrayBuffer containing the AVIF image data to analyze

## Returns

`boolean`

True if the buffer is detected as an animated AVIF, false otherwise

## Examples

```ts
// Check if an AVIF file is animated
const response = await fetch('image.avif')
const buffer = await response.arrayBuffer()
const isAnimated = isAvifAnimated(buffer)
if (isAnimated) {
  console.log('This AVIF contains animation!')
}
```

```ts
// Use with file input
const fileInput = document.querySelector('input[type="file"]')
fileInput.addEventListener('change', async (event) => {
  const file = event.target.files[0]
  const buffer = await file.arrayBuffer()
  const hasAnimation = isAvifAnimated(buffer)
  console.log(hasAnimation ? 'Animated AVIF' : 'Static AVIF')
})
```
