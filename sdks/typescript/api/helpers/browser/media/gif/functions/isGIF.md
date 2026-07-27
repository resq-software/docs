# Function: isGIF()

&gt; **isGIF**(`buffer`): `boolean`

Defined in: [packages/helpers/src/browser/media/gif.ts:50](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/gif.ts#L50)

Checks if buffer contains GIF image by examining the file header.

## Parameters

### buffer

`ArrayBuffer`

The ArrayBuffer containing the image data to check

## Returns

`boolean`

True if the buffer contains a GIF image, false otherwise

## Example

```ts
// Check a file from user input
const file = event.target.files[0]
const buffer = await file.arrayBuffer()
const isGif = isGIF(buffer)
console.log(isGif ? 'GIF image' : 'Not a GIF')
```
