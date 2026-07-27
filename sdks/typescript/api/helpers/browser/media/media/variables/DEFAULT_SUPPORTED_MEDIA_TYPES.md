# Variable: DEFAULT\_SUPPORTED\_MEDIA\_TYPES

&gt; `const` **DEFAULT\_SUPPORTED\_MEDIA\_TYPES**: readonly (`"image/svg+xml"` \| `"image/jpeg"` \| `"image/png"` \| `"image/webp"` \| `"image/gif"` \| `"image/apng"` \| `"image/avif"` \| `"video/mp4"` \| `"video/webm"` \| `"video/quicktime"`)[]

Defined in: [packages/helpers/src/browser/media/media.ts:129](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L129)

Array of all supported media MIME types, combining images and videos.

## Example

```ts
import { DEFAULT_SUPPORTED_MEDIA_TYPES } from '@resq-systems/helpers/browser'

const isMediaFile = DEFAULT_SUPPORTED_MEDIA_TYPES.includes('video/mp4')
console.log(isMediaFile) // true
```
