# Variable: DEFAULT\_SUPPORTED\_STATIC\_IMAGE\_TYPES

&gt; `const` **DEFAULT\_SUPPORTED\_STATIC\_IMAGE\_TYPES**: readonly (`"image/jpeg"` \| `"image/png"` \| `"image/webp"`)[]

Defined in: [packages/helpers/src/browser/media/media.ts:61](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L61)

Array of supported static (non-animated) image MIME types.

## Example

```ts
import { DEFAULT_SUPPORTED_STATIC_IMAGE_TYPES } from '@resq-systems/helpers/browser'

const isStatic = DEFAULT_SUPPORTED_STATIC_IMAGE_TYPES.includes('image/jpeg')
console.log(isStatic) // true
```
