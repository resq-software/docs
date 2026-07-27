# Function: sanitizeHtml()

&gt; **sanitizeHtml**(`html`, `options?`): `string`

Defined in: [sanitize.ts:364](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/sanitize.ts#L364)

Sanitizes HTML to prevent XSS attacks.
Uses DOMPurify under the hood. If DOM is not available (e.g. server-side without JSDOM),
it falls back to escaping all HTML characters for safety.

NOTE: Server-side HTML sanitization requires `jsdom` to be installed in the consuming application
environment; otherwise, it will fall back to escaping HTML characters.

On the first server-side call this lazily resolves `node:module` and
`require`s `jsdom` to build a DOMPurify instance; the instance is cached at
module scope, so subsequent calls incur no further module loading. Returns
`""` for non-string or empty input and never throws — any loader failure is
swallowed and downgraded to [escapeHtml](./escapeHtml).

## Parameters

### html

`string`

The HTML string to sanitize.

### options?

`Config`

Optional DOMPurify configuration.

## Returns

`string`

The sanitized HTML string, or the escaped string when no DOM is
  available.
