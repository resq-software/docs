# Function: safeParseUrl()

&gt; **safeParseUrl**(`url`, `baseUrl?`): `URL` \| `undefined`

Defined in: [packages/helpers/src/browser/url.ts:62](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/browser/url.ts#L62)

Safely parse a URL string, returning `undefined` instead of throwing on
invalid input.

## Parameters

### url

`string`

The URL string to parse.

### baseUrl?

`string` \| `URL`

Optional base URL to resolve relative URLs against.

## Returns

`URL` \| `undefined`

A `URL` object if parsing succeeds, or `undefined` if it fails.

## Example

```ts
// Valid absolute URL
const url1 = safeParseUrl('https://example.com')
if (url1) {
  console.log(`Valid URL: ${url1.href}`) // "Valid URL: https://example.com/"
}

// Invalid URL
const url2 = safeParseUrl('not-a-url')
console.log(url2) // undefined

// Relative URL with base
const url3 = safeParseUrl('/path', 'https://example.com')
if (url3) {
  console.log(url3.href) // "https://example.com/path"
}

// Error handling
function handleUserUrl(input: string) {
  const url = safeParseUrl(input)
  if (url) {
    return url
  } else {
    console.log('Invalid URL provided')
    return null
  }
}
```
