# Function: capitalize()

&gt; **capitalize**(`str`): `string`

Defined in: [packages/helpers/src/formatting/string.ts:39](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/formatting/string.ts#L39)

Upper-case the first character of a string and leave the rest
unchanged. ASCII-aware; for full Unicode title-casing use
`Intl.Segmenter` plus locale-aware case mapping.

## Parameters

### str

`string`

Input string. Empty input returns `""`.

## Returns

`string`

The string with its first character upper-cased.

## Example

```ts
capitalize("hello");      // → "Hello"
capitalize("hELLO");      // → "HELLO" (only first char changes)
capitalize("");           // → ""
```
