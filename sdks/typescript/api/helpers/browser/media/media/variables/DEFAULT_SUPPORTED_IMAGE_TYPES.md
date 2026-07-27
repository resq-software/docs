# Variable: DEFAULT\_SUPPORTED\_IMAGE\_TYPES

&gt; `const` **DEFAULT\_SUPPORTED\_IMAGE\_TYPES**: readonly (`"image/svg+xml"` \| `"image/jpeg"` \| `"image/png"` \| `"image/webp"` \| `"image/gif"` \| `"image/apng"` \| `"image/avif"`)[]

Defined in: [packages/helpers/src/browser/media/media.ts:95](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L95)

Array of all supported image MIME types, combining static, vector, and animated types.

## Example

```ts
import { DEFAULT_SUPPORTED_IMAGE_TYPES } from '@resq-systems/helpers/browser'

const isSupported = DEFAULT_SUPPORTED_IMAGE_TYPES.includes('image/png')
console.log(isSupported) // true
```
