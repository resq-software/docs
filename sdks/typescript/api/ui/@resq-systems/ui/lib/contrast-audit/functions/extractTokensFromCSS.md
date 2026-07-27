# Function: extractTokensFromCSS()

&gt; **extractTokensFromCSS**(`css`): `Record`\<`string`, [`ColorTokens`](../type-aliases/ColorTokens)\>

Defined in: [packages/ui/src/lib/contrast-audit.ts:649](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L649)

Extract color tokens from a CSS string containing `:root` and `.light` blocks.

The `:root` block maps to the `dark` key and `.light` to the `light` key; a
key is present only when its block is found, so the result may hold `dark`,
`light`, both, or neither. Token names drop the `--` prefix (`--foreground`
becomes `foreground`). Only the first matching block of each kind is read, and
only recognised color-value formats (oklch/oklab/lab/lch/hsl/rgb/hex) are
captured. Pure — no I/O; does not throw on unrecognised input, it simply
yields fewer tokens.

## Parameters

### css

`string`

Raw stylesheet text to scan.

## Returns

`Record`\<`string`, [`ColorTokens`](../type-aliases/ColorTokens)\>

A `mode → ColorTokens` map suitable for [runContrastAudit](./runContrastAudit).
