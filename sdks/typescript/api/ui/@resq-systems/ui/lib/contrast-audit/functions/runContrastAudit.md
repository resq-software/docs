# Function: runContrastAudit()

&gt; **runContrastAudit**(`themes`, `pairs?`): `object`

Defined in: [packages/ui/src/lib/contrast-audit.ts:696](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L696)

Run [auditTheme](./auditTheme) across every theme in `themes` and return
an aggregate decision plus per-theme details.

## Parameters

### themes

`Record`\<`string`, [`ColorTokens`](../type-aliases/ColorTokens)\>

Map of `mode → ColorTokens` (e.g. the output of
  [extractTokensFromCSS](./extractTokensFromCSS)).

### pairs?

[`ContrastPair`](../interfaces/ContrastPair)[] = `DEFAULT_PAIRS`

Contrast pairs to enforce. Defaults to
  [DEFAULT\_PAIRS](../variables/DEFAULT_PAIRS).

## Returns

`object`

`{ globalPass, audits }` — `globalPass` is `true` only
  when every theme passes every pair.

### audits

&gt; **audits**: [`ThemeAudit`](../interfaces/ThemeAudit)[]

### globalPass

&gt; **globalPass**: `boolean`

## Throws

Propagated from [auditTheme](./auditTheme)/[toLinearRGB](./toLinearRGB) when
  any present token holds an unsupported color string.
