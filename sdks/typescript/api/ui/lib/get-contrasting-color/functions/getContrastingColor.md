# Function: getContrastingColor()

&gt; **getContrastingColor**(`col`): `"#000000"` \| `"#ffffff"` \| `undefined`

Defined in: [packages/ui/src/lib/get-contrasting-color.ts:60](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/get-contrasting-color.ts#L60)

Returns a highly contrasting color (`"#000000"` or `"#ffffff"`) for a given
input color string, useful for ensuring text or UI elements remain visible
against varying backgrounds.

Requires a DOM: it normalizes `col` through a detached `<canvas>` 2D context
(`document.createElement`), so it returns `undefined` in any non-browser
environment where `window` is absent. The canvas is transient — nothing is
attached to the document and no state persists across calls.

Never throws: an unparseable or unsupported `col`, or a missing canvas
context, silently falls back to `"#ffffff"` rather than surfacing an error.

## Parameters

### col

`string`

The input color (any valid CSS color string, e.g. `"#f00"`,
  `"rgb(255,0,0)"`, `"blue"`).

## Returns

`"#000000"` \| `"#ffffff"` \| `undefined`

`"#000000"` when dark text reads best (light background) or
  `"#ffffff"` when light text reads best (dark background); the sentinel
  `undefined` when called during server-side rendering (no `window`).
  Unparseable input resolves to `"#ffffff"`.

## Example

```ts
getContrastingColor('#FFFFFF'); // → "#000000"
getContrastingColor('navy');    // → "#ffffff"
```

## See

https://www.w3.org/WAI/ER/WD-AERT/#color-contrast
