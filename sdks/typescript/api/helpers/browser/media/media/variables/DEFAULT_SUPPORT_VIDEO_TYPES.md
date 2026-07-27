# Variable: DEFAULT\_SUPPORT\_VIDEO\_TYPES

&gt; `const` **DEFAULT\_SUPPORT\_VIDEO\_TYPES**: readonly (`"video/mp4"` \| `"video/webm"` \| `"video/quicktime"`)[]

Defined in: [packages/helpers/src/browser/media/media.ts:112](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L112)

Array of supported video MIME types.

## Example

```ts
import { DEFAULT_SUPPORT_VIDEO_TYPES } from '@resq-systems/helpers/browser'

const isVideo = DEFAULT_SUPPORT_VIDEO_TYPES.includes('video/mp4')
console.log(isVideo) // true
```
