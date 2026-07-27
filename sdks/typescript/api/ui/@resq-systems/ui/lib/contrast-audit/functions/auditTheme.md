# Function: auditTheme()

&gt; **auditTheme**(`mode`, `tokens`, `pairs`): [`ThemeAudit`](../interfaces/ThemeAudit)

Defined in: [packages/ui/src/lib/contrast-audit.ts:498](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L498)

Run every [ContrastPair](../interfaces/ContrastPair) against the theme's `tokens` and
return a [ThemeAudit](../interfaces/ThemeAudit).

Pairs whose `fg` or `bg` token is missing from `tokens` are
silently skipped (so partial themes can still audit their defined
tokens). Luminance is memoised across pairs to keep the audit
`O(tokens + pairs)` rather than `O(tokens × pairs)`.

## Parameters

### mode

`string`

Echoed back as `audit.mode` for reporting.

### tokens

[`ColorTokens`](../type-aliases/ColorTokens)

Theme token map (token name → CSS color value).

### pairs

[`ContrastPair`](../interfaces/ContrastPair)[]

Pairs to evaluate. Use [DEFAULT\_PAIRS](../variables/DEFAULT_PAIRS) for the
  project's standard checks.

## Returns

[`ThemeAudit`](../interfaces/ThemeAudit)

A [ThemeAudit](../interfaces/ThemeAudit) whose `results` omit any pair with a missing
  token; `allPass` is `true` only when every included result passed.

## Throws

Propagated from [toLinearRGB](./toLinearRGB) when a token that *is*
  present holds a CSS value in no supported color format. A missing token is
  skipped, not thrown.
