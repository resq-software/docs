# Function: runContrastAudit()

> **runContrastAudit**(`themes`, `pairs?`): `object`

Defined in: [packages/ui/src/lib/contrast-audit.ts:567](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/lib/contrast-audit.ts#L567)

## Parameters

### themes

`Record`\<`string`, [`ColorTokens`](../type-aliases/ColorTokens.md)\>

### pairs?

[`ContrastPair`](../interfaces/ContrastPair.md)[] = `DEFAULT_PAIRS`

## Returns

`object`

### audits

> **audits**: [`ThemeAudit`](../interfaces/ThemeAudit.md)[]

### globalPass

> **globalPass**: `boolean`
