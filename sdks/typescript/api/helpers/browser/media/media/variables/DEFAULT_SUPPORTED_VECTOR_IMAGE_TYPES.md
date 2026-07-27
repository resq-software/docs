# Variable: DEFAULT\_SUPPORTED\_VECTOR\_IMAGE\_TYPES

&gt; `const` **DEFAULT\_SUPPORTED\_VECTOR\_IMAGE\_TYPES**: readonly `"image/svg+xml"`[]

Defined in: [packages/helpers/src/browser/media/media.ts:48](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L48)

Array of supported vector image MIME types.

## Example

```ts
import { DEFAULT_SUPPORTED_VECTOR_IMAGE_TYPES } from '@resq-systems/helpers/browser'

const isSvg = DEFAULT_SUPPORTED_VECTOR_IMAGE_TYPES.includes('image/svg+xml')
console.log(isSvg) // true
```
