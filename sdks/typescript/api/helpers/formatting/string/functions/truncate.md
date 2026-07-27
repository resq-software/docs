# Function: truncate()

&gt; **truncate**(`str`, `length`): `string`

Defined in: [packages/helpers/src/formatting/string.ts:65](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/string.ts#L65)

Truncate a string to at most `length` characters, appending `"..."`
when truncated. The ellipsis is **additive** — the returned string
may be `length + 3` characters long when truncation occurs.

Operates on UTF-16 code units, so emoji and other surrogate-pair
code points may be split. Use `Intl.Segmenter` if you need
grapheme-cluster-safe truncation.

## Parameters

### str

`string`

Input string.

### length

`number`

Maximum number of code units to keep before
  appending the ellipsis.

## Returns

`string`

The original string when it fits, or `str.slice(0, length)
  + "..."`.

## Example

```ts
truncate("hello world", 5); // → "hello..."
truncate("hi", 5);          // → "hi"
```
