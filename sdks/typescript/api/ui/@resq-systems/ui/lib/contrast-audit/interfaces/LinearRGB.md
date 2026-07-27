# Interface: LinearRGB

Defined in: [packages/ui/src/lib/contrast-audit.ts:20](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L20)

Linear-RGB triplet (each channel `0..1`, gamma-decoded). The
intermediate representation used by all contrast math — every
supported input format (`#hex`, `rgb()`, `hsl()`, `oklch()`,
`lab()`, `lch()`, `oklab()`, named colors) is decoded into this.

## Properties

### b

&gt; **b**: `number`

Defined in: [packages/ui/src/lib/contrast-audit.ts:26](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L26)

Blue channel, `0..1` linear.

***

### g

&gt; **g**: `number`

Defined in: [packages/ui/src/lib/contrast-audit.ts:24](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L24)

Green channel, `0..1` linear.

***

### r

&gt; **r**: `number`

Defined in: [packages/ui/src/lib/contrast-audit.ts:22](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L22)

Red channel, `0..1` linear.
