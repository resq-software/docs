# Function: getContrastingColor()

> **getContrastingColor**(`col`): `"#000000"` \| `"#ffffff"` \| `undefined`

Defined in: [packages/ui/src/lib/get-contrasting-color.ts:51](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/get-contrasting-color.ts#L51)

Returns a highly contrasting color (#000000 or #ffffff) for a given input color string,
useful for ensuring text or UI elements remain visible against varying backgrounds.

This function only runs in the browser; on the server, it returns undefined.

## Parameters

### col

`string`

The input color (any valid CSS color string, e.g. "#f00", "rgb(255,0,0)", "blue").

## Returns

`"#000000"` \| `"#ffffff"` \| `undefined`

The hex color string for the contrasting color ("#000000" or "#ffffff"), or undefined if not in browser environment.

## Throws

May throw if standardization or parsing of color fails, but usually falls back silently.

## Example

```ts
getContrastingColor('#FFFFFF'); // → "#000000"
getContrastingColor('navy');    // → "#ffffff"
```

## See

https://www.w3.org/WAI/ER/WD-AERT/#color-contrast
