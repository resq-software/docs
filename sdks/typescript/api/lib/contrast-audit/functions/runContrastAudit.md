# Function: runContrastAudit()

> **runContrastAudit**(`themes`, `pairs?`): `object`

Defined in: [packages/ui/src/lib/contrast-audit.ts:567](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/contrast-audit.ts#L567)

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
