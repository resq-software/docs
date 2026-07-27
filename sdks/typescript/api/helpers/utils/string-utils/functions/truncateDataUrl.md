# Function: truncateDataUrl()

&gt; **truncateDataUrl**(`url`): `string`

Defined in: [packages/helpers/src/utils/string-utils.ts:93](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/string-utils.ts#L93)

Collapse a `data:` URL to its media-type prefix + `…`, dropping the (often
huge) base64 payload. Non-data URLs are returned unchanged.

## Parameters

### url

`string`

## Returns

`string`
