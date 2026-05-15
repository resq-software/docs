# Function: sanitizeForDisplay()

> **sanitizeForDisplay**(`input`): `string`

Defined in: [validators.ts:522](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L522)

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
