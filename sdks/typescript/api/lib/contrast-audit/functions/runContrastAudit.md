# Function: runContrastAudit()

> **runContrastAudit**(`themes`, `pairs?`): `object`

Defined in: [packages/ui/src/lib/contrast-audit.ts:567](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/contrast-audit.ts#L567)

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
