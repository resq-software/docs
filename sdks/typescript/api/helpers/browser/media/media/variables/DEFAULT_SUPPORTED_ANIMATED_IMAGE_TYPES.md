# Variable: DEFAULT\_SUPPORTED\_ANIMATED\_IMAGE\_TYPES

&gt; `const` **DEFAULT\_SUPPORTED\_ANIMATED\_IMAGE\_TYPES**: readonly (`"image/gif"` \| `"image/apng"` \| `"image/avif"`)[]

Defined in: [packages/helpers/src/browser/media/media.ts:78](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L78)

Array of supported animated image MIME types.

## Example

```ts
import { DEFAULT_SUPPORTED_ANIMATED_IMAGE_TYPES } from '@resq-systems/helpers/browser'

const isAnimated = DEFAULT_SUPPORTED_ANIMATED_IMAGE_TYPES.includes('image/gif')
console.log(isAnimated) // true
```
