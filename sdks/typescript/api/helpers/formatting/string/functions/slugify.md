# Function: slugify()

&gt; **slugify**(`str`): `string`

Defined in: [packages/helpers/src/formatting/string.ts:90](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/string.ts#L90)

Convert an arbitrary string into a URL-safe slug — lower-cased,
non-word characters removed, runs of spaces collapsed to single
hyphens.

Strips anything outside `[A-Za-z0-9_]` (and space). Diacritics are
removed rather than transliterated; for transliteration (`é → e`)
normalize the input first with `str.normalize("NFKD")` and strip
combining marks before passing in.

## Parameters

### str

`string`

Input string (typically a title or human-entered name).

## Returns

`string`

Lower-case kebab-style slug.

## Example

```ts
slugify("Hello, World!");     // → "hello-world"
slugify("  foo   bar  ");     // → "-foo-bar-"  (leading/trailing spaces preserved as hyphens)
slugify("Action: 2026 Plan"); // → "action-2026-plan"
```
