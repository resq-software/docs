# Function: toLinearRGB()

&gt; **toLinearRGB**(`raw`): [`LinearRGB`](../interfaces/LinearRGB)

Defined in: [packages/ui/src/lib/contrast-audit.ts:434](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L434)

Decode any supported CSS color string into [LinearRGB](../interfaces/LinearRGB).

Supported inputs (case-insensitive): named colors, `#hex` (3/4/6/8
digits, with or without `#`), `rgb()` / `rgba()`, `hsl()` /
`hsla()`, `oklch()`, `oklab()`, `lab()`, `lch()`.

Pure and deterministic — no I/O or shared state; the same string always
decodes to the same triplet.

## Parameters

### raw

`string`

## Returns

[`LinearRGB`](../interfaces/LinearRGB)

## Throws

When `raw` (after trimming/lowercasing) matches no supported
  format. The message embeds the offending value.
