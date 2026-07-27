# Class: MediaHelpers

Defined in: [packages/helpers/src/browser/media/media.ts:234](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L234)

Helpers for media

## Constructors

### Constructor

&gt; **new MediaHelpers**(): `MediaHelpers`

#### Returns

`MediaHelpers`

## Methods

### getImageAndDimensions()

&gt; `static` **getImageAndDimensions**(`src`, `doc?`): `Promise`\<\{ `h`: `number`; `image`: `HTMLImageElement`; `w`: `number`; \}\>

Defined in: [packages/helpers/src/browser/media/media.ts:383](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L383)

Load an image from a URL and get its dimensions along with the image element.

Starts a cross-origin image load. When the image reports no
`naturalWidth` (Firefox with SVGs), it briefly appends the element to
`doc.body` to measure `clientWidth`/`clientHeight`, then removes it — a
transient DOM mutation. Failure is a **rejected** promise.

#### Parameters

##### src

`string`

The URL of the image to load

##### doc?

`Document`

Optional document to use for DOM operations (e.g. measuring SVG dimensions)

#### Returns

`Promise`\<\{ `h`: `number`; `image`: `HTMLImageElement`; `w`: `number`; \}\>

Promise that resolves to an object with width, height, and the image element

#### Throws

Rejects with `"Could not load image"` if the element emits
  an `error` event (bad URL, decode failure, CORS denial).

#### Example

```ts
const { w, h, image } = await MediaHelpers.getImageAndDimensions('https://example.com/image.png')
console.log(`Image size: ${w}x${h}`)
// Image is ready to use
document.body.appendChild(image)
```

***

### getImageSize()

&gt; `static` **getImageSize**(`blob`, `doc?`): `Promise`\<\{ `h`: `number`; `pixelRatio`: `number`; `w`: `number`; \}\>

Defined in: [packages/helpers/src/browser/media/media.ts:470](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L470)

Get the size of an image blob

For PNGs, inspects the `pHYs` chunk to recover a device pixel ratio and
divides the raw pixel dimensions by it; any error while parsing the chunk
is swallowed and the raw size with `pixelRatio: 1` is returned instead.

#### Parameters

##### blob

`Blob`

A Blob containing the image

##### doc?

`Document`

Optional document to use for DOM operations

#### Returns

`Promise`\<\{ `h`: `number`; `pixelRatio`: `number`; `w`: `number`; \}\>

Promise that resolves to an object with `w`, `h`, and the resolved
  `pixelRatio` (`1` when no high-DPI metadata applies or parsing failed).

#### Throws

Rejects with `"Could not load image"` when the blob cannot
  be decoded (the image-load step; the PNG-metadata step never rejects).

#### Example

```ts
const file = new File([...], 'image.png', { type: 'image/png' })
const { w, h } = await MediaHelpers.getImageSize(file)
console.log(`Image dimensions: ${w}x${h}`)
```

***

### getVideoFrameAsDataUrl()

&gt; `static` **getVideoFrameAsDataUrl**(`video`, `time?`): `Promise`\<`string`\>

Defined in: [packages/helpers/src/browser/media/media.ts:294](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L294)

Extract a frame from a video element as a data URL.

For a non-zero `time` this **mutates the passed `video`**: it sets
`video.currentTime` to seek, then captures once the `seeked` event fires.
Event listeners are attached and removed internally, so the element is left
as found apart from its playback position. Failure is a **rejected**
promise.

#### Parameters

##### video

`HTMLVideoElement`

The HTMLVideoElement to extract frame from

##### time?

`number` = `0`

The time in seconds to extract the frame from (default: 0)

#### Returns

`Promise`\<`string`\>

Promise that resolves to a data URL of the video frame

#### Throws

Rejects with `"Could not get video frame"` on the video's
  `error` / `stalled` events. If a 2D canvas context cannot be obtained, an
  `Error("Could not get 2d context")` is thrown inside the event handler and
  the promise never settles.

#### Example

```ts
const video = await MediaHelpers.loadVideo('https://example.com/video.mp4')
const frameDataUrl = await MediaHelpers.getVideoFrameAsDataUrl(video, 5.0)
// Use frameDataUrl as image thumbnail
const img = document.createElement('img')
img.src = frameDataUrl
```

***

### getVideoSize()

&gt; `static` **getVideoSize**(`blob`, `doc?`): `Promise`\<\{ `h`: `number`; `w`: `number`; \}\>

Defined in: [packages/helpers/src/browser/media/media.ts:442](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L442)

Get the size of a video blob

Creates and revokes a temporary object URL around a [loadVideo](#loadvideo) call.

#### Parameters

##### blob

`Blob`

A Blob containing the video

##### doc?

`Document`

Optional document to create elements in

#### Returns

`Promise`\<\{ `h`: `number`; `w`: `number`; \}\>

Promise that resolves to an object with width and height properties

#### Throws

Rejects with `"Could not load video"` when the blob cannot
  be decoded as a playable video.

#### Example

```ts
const file = new File([...], 'video.mp4', { type: 'video/mp4' })
const { w, h } = await MediaHelpers.getVideoSize(file)
console.log(`Video dimensions: ${w}x${h}`)
```

***

### isAnimated()

&gt; `static` **isAnimated**(`file`): `Promise`\<`boolean`\>

Defined in: [packages/helpers/src/browser/media/media.ts:528](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L528)

Check if a media file blob contains animation data.

#### Parameters

##### file

`Blob`

The Blob to check for animation

#### Returns

`Promise`\<`boolean`\>

Promise that resolves to true if the file is animated, false otherwise

#### Example

```ts
const file = new File([...], 'animation.gif', { type: 'image/gif' })
const animated = await MediaHelpers.isAnimated(file)
console.log(animated ? 'Animated' : 'Static')
```

***

### isAnimatedImageType()

&gt; `static` **isAnimatedImageType**(`mimeType`): mimeType is "image/gif" \| "image/apng" \| "image/avif"

Defined in: [packages/helpers/src/browser/media/media.ts:560](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L560)

Check if a MIME type represents an animated image format.

#### Parameters

##### mimeType

`string` \| `null`

The MIME type to check

#### Returns

mimeType is "image/gif" \| "image/apng" \| "image/avif"

True if the MIME type is an animated image format, false otherwise

#### Example

```ts
const isAnimated = MediaHelpers.isAnimatedImageType('image/gif')
console.log(isAnimated) // true
```

***

### isImageType()

&gt; `static` **isImageType**(`mimeType`): mimeType is "image/svg+xml" \| "image/jpeg" \| "image/png" \| "image/webp" \| "image/gif" \| "image/apng" \| "image/avif"

Defined in: [packages/helpers/src/browser/media/media.ts:608](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L608)

Check if a MIME type represents any supported image format (static, animated, or vector).

#### Parameters

##### mimeType

`string`

The MIME type to check

#### Returns

mimeType is "image/svg+xml" \| "image/jpeg" \| "image/png" \| "image/webp" \| "image/gif" \| "image/apng" \| "image/avif"

True if the MIME type is a supported image format, false otherwise

#### Example

```ts
const isImage = MediaHelpers.isImageType('image/png')
console.log(isImage) // true
```

***

### isStaticImageType()

&gt; `static` **isStaticImageType**(`mimeType`): mimeType is "image/jpeg" \| "image/png" \| "image/webp"

Defined in: [packages/helpers/src/browser/media/media.ts:576](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L576)

Check if a MIME type represents a static (non-animated) image format.

#### Parameters

##### mimeType

`string` \| `null`

The MIME type to check

#### Returns

mimeType is "image/jpeg" \| "image/png" \| "image/webp"

True if the MIME type is a static image format, false otherwise

#### Example

```ts
const isStatic = MediaHelpers.isStaticImageType('image/jpeg')
console.log(isStatic) // true
```

***

### isVectorImageType()

&gt; `static` **isVectorImageType**(`mimeType`): `mimeType is "image/svg+xml"`

Defined in: [packages/helpers/src/browser/media/media.ts:592](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L592)

Check if a MIME type represents a vector image format.

#### Parameters

##### mimeType

`string` \| `null`

The MIME type to check

#### Returns

`mimeType is "image/svg+xml"`

True if the MIME type is a vector image format, false otherwise

#### Example

```ts
const isVector = MediaHelpers.isVectorImageType('image/svg+xml')
console.log(isVector) // true
```

***

### loadVideo()

&gt; `static` **loadVideo**(`src`, `doc?`): `Promise`\<`HTMLVideoElement`\>

Defined in: [packages/helpers/src/browser/media/media.ts:254](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L254)

Load a video element from a URL with cross-origin support.

Creates a detached `<video>` element and starts a cross-origin network
load (side effects). Failure is a **rejected** promise, not a resolved
error value.

#### Parameters

##### src

`string`

The URL of the video to load

##### doc?

`Document`

Optional document to create the video element in

#### Returns

`Promise`\<`HTMLVideoElement`\>

Promise that resolves to the loaded HTMLVideoElement

#### Throws

Rejects with `"Could not load video"` if the element emits
  an `error` event (bad URL, decode failure, CORS denial).

#### Example

```ts
const video = await MediaHelpers.loadVideo('https://example.com/video.mp4')
console.log(`Video dimensions: ${video.videoWidth}x${video.videoHeight}`)
```

***

### usingObjectURL()

&gt; `static` **usingObjectURL**\<`T`\>(`blob`, `fn`): `Promise`\<`T`\>

Defined in: [packages/helpers/src/browser/media/media.ts:633](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L633)

Utility function to create an object URL from a blob, execute a function with it, and automatically clean it up.

`URL.revokeObjectURL` runs in a `finally`, so the URL is released whether
`fn` resolves or rejects. A rejection from `fn` propagates unchanged.

#### Type Parameters

##### T

`T`

The value `fn` resolves to and this method returns.

#### Parameters

##### blob

`Blob`

The Blob to create an object URL for

##### fn

(`url`) =&gt; `Promise`\<`T`\>

Function to execute with the object URL

#### Returns

`Promise`\<`T`\>

Promise that resolves to the result of the function

#### Example

```ts
const result = await MediaHelpers.usingObjectURL(imageBlob, async (url) => {
  const { w, h } = await MediaHelpers.getImageAndDimensions(url)
  return { width: w, height: h }
})
// Object URL is automatically revoked after function completes
console.log(`Image dimensions: ${result.width}x${result.height}`)
```
