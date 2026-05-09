# Function: extractTokensFromCSS()

> **extractTokensFromCSS**(`css`): `Record`\<`string`, [`ColorTokens`](../type-aliases/ColorTokens.md)\>

Defined in: [packages/ui/src/lib/contrast-audit.ts:536](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/lib/contrast-audit.ts#L536)

Extracts color tokens from a CSS string containing :root and .light blocks.
Supports any color format (oklch, hex, rgb, hsl, named, etc.).
Returns &#123; dark: &#123;...&#125;, light: &#123;...&#125; &#125; with token names as keys.

## Parameters

### css

`string`

## Returns

`Record`\<`string`, [`ColorTokens`](../type-aliases/ColorTokens.md)\>
