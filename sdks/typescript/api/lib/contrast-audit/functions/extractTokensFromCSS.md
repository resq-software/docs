# Function: extractTokensFromCSS()

> **extractTokensFromCSS**(`css`): `Record`\<`string`, [`ColorTokens`](../type-aliases/ColorTokens.md)\>

Defined in: [packages/ui/src/lib/contrast-audit.ts:536](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/contrast-audit.ts#L536)

Extracts color tokens from a CSS string containing :root and .light blocks.
Supports any color format (oklch, hex, rgb, hsl, named, etc.).
Returns &#123; dark: &#123;...&#125;, light: &#123;...&#125; &#125; with token names as keys.

## Parameters

### css

`string`

## Returns

`Record`\<`string`, [`ColorTokens`](../type-aliases/ColorTokens.md)\>
