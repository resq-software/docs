# Function: sanitizeForDisplay()

&gt; **sanitizeForDisplay**(`input`): `string`

Defined in: [validators.ts:531](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L531)

HTML-entity escape `&`, `<`, `>`, `"`, `'`, and `/` for safe
insertion into HTML text and attribute contexts.

**Limited scope.** This is appropriate for plain text destined for
`textContent` or attribute values, not for unfiltered HTML
rendering. For rich-text use a vetted sanitizer (DOMPurify on the
client, sanitize-html or similar on the server).

Returns `""` for non-string or empty input.

## Parameters

### input

`string`

Untrusted string.

## Returns

`string`

Entity-escaped output safe to interpolate into HTML.
