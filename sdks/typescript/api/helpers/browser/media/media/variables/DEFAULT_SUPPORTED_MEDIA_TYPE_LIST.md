# Variable: DEFAULT\_SUPPORTED\_MEDIA\_TYPE\_LIST

&gt; `const` **DEFAULT\_SUPPORTED\_MEDIA\_TYPE\_LIST**: `string`

Defined in: [packages/helpers/src/browser/media/media.ts:151](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/media/media.ts#L151)

Comma-separated string of all supported media MIME types, useful for HTML file input accept attributes.

## Example

```ts
import { DEFAULT_SUPPORTED_MEDIA_TYPE_LIST } from '@resq-systems/helpers/browser'

// Use in HTML file input for media uploads
const input = document.createElement('input')
input.type = 'file'
input.accept = DEFAULT_SUPPORTED_MEDIA_TYPE_LIST
input.addEventListener('change', (e) => {
  const files = (e.target as HTMLInputElement).files
  if (files) console.log(`Selected ${files.length} file(s)`)
})
```
