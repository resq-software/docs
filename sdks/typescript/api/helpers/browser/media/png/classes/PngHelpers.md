# Class: PngHelpers

Defined in: [packages/helpers/src/browser/media/png.ts:120](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/png.ts#L120)

Utility class for reading and manipulating PNG image files.
Provides methods for parsing PNG chunks, validating PNG format, and modifying PNG metadata.

## Example

```ts
// Validate PNG file from blob
const blob = new Blob([pngData], { type: 'image/png' })
const view = new DataView(await blob.arrayBuffer())
const isPng = PngHelpers.isPng(view, 0)

// Parse PNG metadata for image processing
const chunks = PngHelpers.readChunks(view)
const physChunk = PngHelpers.findChunk(view, 'pHYs')

// Create high-DPI PNG for export
const highDpiBlob = PngHelpers.setPhysChunk(view, 2, { type: 'image/png' })
```

## Constructors

### Constructor

&gt; **new PngHelpers**(): `PngHelpers`

#### Returns

`PngHelpers`

## Methods

### findChunk()

&gt; `static` **findChunk**(`view`, `type`): `object`

Defined in: [packages/helpers/src/browser/media/png.ts:301](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/png.ts#L301)

Finds a specific chunk type in the PNG file and returns its metadata.

#### Parameters

##### view

`DataView`

DataView containing the PNG file data

##### type

`string`

4-character chunk type to search for (e.g., 'pHYs', 'IDAT')

#### Returns

`object`

Chunk metadata object if found, undefined otherwise

##### dataOffset

&gt; **dataOffset**: `number`

##### size

&gt; **size**: `number`

##### start

&gt; **start**: `number`

#### Example

```ts
// Look for pixel density information in PNG
const physChunk = PngHelpers.findChunk(dataView, 'pHYs')
if (physChunk) {
  const physData = PngHelpers.parsePhys(dataView, physChunk.dataOffset)
  console.log(`Found pHYs chunk with ${physData.ppux} x ${physData.ppuy} pixels per unit`)
}

// Check for text metadata
const textChunk = PngHelpers.findChunk(dataView, 'tEXt')
if (textChunk) {
  console.log(`Found text metadata at byte ${textChunk.start}`)
}
```

***

### getChunkType()

&gt; `static` **getChunkType**(`view`, `offset`): `string`

Defined in: [packages/helpers/src/browser/media/png.ts:179](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/png.ts#L179)

Reads the 4-character chunk type identifier from a PNG chunk header.

#### Parameters

##### view

`DataView`

DataView containing the PNG data

##### offset

`number`

Byte offset of the chunk type field (after length field)

#### Returns

`string`

4-character string representing the chunk type (e.g., 'IHDR', 'IDAT', 'IEND')

#### Example

```ts
// Read chunk type from PNG header (after 8-byte signature)
const chunkType = PngHelpers.getChunkType(dataView, 8)
console.log(chunkType) // 'IHDR' (Image Header)

// Read chunk type at a specific position during parsing
let offset = 8 // Skip PNG signature
const chunkLength = dataView.getUint32(offset)
const type = PngHelpers.getChunkType(dataView, offset + 4)
```

***

### isPng()

&gt; `static` **isPng**(`view`, `offset`): `boolean`

Defined in: [packages/helpers/src/browser/media/png.ts:144](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/png.ts#L144)

Checks if binary data at the specified offset contains a valid PNG file signature.
Validates the 8-byte PNG signature: 89 50 4E 47 0D 0A 1A 0A.

#### Parameters

##### view

`DataView`

DataView containing the binary data to check

##### offset

`number`

Byte offset where the PNG signature should start

#### Returns

`boolean`

True if the data contains a valid PNG signature, false otherwise

#### Example

```ts
// Validate PNG from file upload
const file = event.target.files[0]
const buffer = await file.arrayBuffer()
const view = new DataView(buffer)

if (PngHelpers.isPng(view, 0)) {
  console.log('Valid PNG file detected')
  // Process PNG file...
} else {
  console.error('Not a valid PNG file')
}
```

***

### parsePhys()

&gt; `static` **parsePhys**(`view`, `offset`): `object`

Defined in: [packages/helpers/src/browser/media/png.ts:270](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/png.ts#L270)

Parses the pHYs (physical pixel dimensions) chunk data.
Reads pixels per unit for X and Y axes, and the unit specifier.

#### Parameters

##### view

`DataView`

DataView containing the PNG data

##### offset

`number`

Byte offset of the pHYs chunk data

#### Returns

`object`

Object with ppux (pixels per unit X), ppuy (pixels per unit Y), and unit specifier

##### ppux

&gt; **ppux**: `number`

##### ppuy

&gt; **ppuy**: `number`

##### unit

&gt; **unit**: `number`

#### Example

```ts
// Extract pixel density information for DPI calculation
const physChunk = PngHelpers.findChunk(dataView, 'pHYs')
if (physChunk) {
  const physData = PngHelpers.parsePhys(dataView, physChunk.dataOffset)

  if (physData.unit === 1) { // meters
    const dpiX = Math.round(physData.ppux * 0.0254)
    const dpiY = Math.round(physData.ppuy * 0.0254)
    console.log(`DPI: ${dpiX} x ${dpiY}`)
  }
}
```

***

### readChunks()

&gt; `static` **readChunks**(`view`, `offset?`): `Record`\<`string`, \{ `dataOffset`: `number`; `size`: `number`; `start`: `number`; \}\>

Defined in: [packages/helpers/src/browser/media/png.ts:214](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/png.ts#L214)

Parses all chunks in a PNG file and returns their metadata.
Skips duplicate IDAT chunks but includes all other chunk types.

#### Parameters

##### view

`DataView`

DataView containing the complete PNG file data

##### offset?

`number` = `0`

Starting byte offset (defaults to 0)

#### Returns

`Record`\<`string`, \{ `dataOffset`: `number`; `size`: `number`; `start`: `number`; \}\>

Record mapping chunk types to their metadata (start position, data offset, and size)

#### Throws

Error if the data is not a valid PNG file

#### Example

```ts
// Parse PNG structure for metadata extraction
const view = new DataView(await blob.arrayBuffer())
const chunks = PngHelpers.readChunks(view)

// Check for specific chunks
const ihdrChunk = chunks['IHDR']
const physChunk = chunks['pHYs']

if (physChunk) {
  console.log(`Found pixel density info at byte ${physChunk.start}`)
} else {
  console.log('No pixel density information found')
}
```

***

### setPhysChunk()

&gt; `static` **setPhysChunk**(`view`, `dpr?`, `options?`): `Blob`

Defined in: [packages/helpers/src/browser/media/png.ts:333](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/png.ts#L333)

Adds or replaces a pHYs chunk in a PNG file to set pixel density for high-DPI displays.
The method determines insertion point by prioritizing IDAT chunk position over existing pHYs,
creates a properly formatted pHYs chunk with CRC validation, and returns a new Blob.

#### Parameters

##### view

`DataView`

DataView containing the original PNG file data

##### dpr?

`number` = `1`

Device pixel ratio multiplier (defaults to 1)

##### options?

`BlobPropertyBag`

Optional Blob constructor options for MIME type and other properties

#### Returns

`Blob`

New Blob containing the PNG with updated pixel density information

#### Example

```ts
// Export PNG with proper pixel density for high-DPI displays
const canvas = document.createElement('canvas')
const ctx = canvas.getContext('2d')
// ... draw content to canvas ...

canvas.toBlob(async (blob) => {
  if (blob) {
    const view = new DataView(await blob.arrayBuffer())
    // Create 2x DPI version for Retina displays
    const highDpiBlob = PngHelpers.setPhysChunk(view, 2, { type: 'image/png' })
    // Download or use the blob...
  }
}, 'image/png')
```
