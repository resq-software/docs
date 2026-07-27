# Variable: colors

&gt; `const` **colors**: `object`

Defined in: [tokens.ts:66](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/constants/src/tokens.ts#L66)

The canonical palette in its two representations. `oklch` is the source of
truth; `hex` is a hand-maintained snapshot that must resolve to the same
perceived color for each shared [ColorRole](../type-aliases/ColorRole), because email clients and
older render targets can't evaluate `oklch()`. Editing one representation
without the other silently drifts email away from the app — the two are only
*structurally* linked by the `satisfies` clause below, not value-checked.

## Type Declaration

### chart

&gt; `readonly` **chart**: readonly \[`"oklch(58.50% 0.1877 24.72)"`, `"oklch(64.20% 0.1560 252.61)"`, `"oklch(73.39% 0.1538 161.68)"`, `"oklch(78.37% 0.1587 72.99)"`, `"oklch(68.62% 0.0471 261.10)"`\]

Categorical data-visualization palette — the five `--chart-1..5` oklch
values shipped by `@resq-systems/ui` (canonical dark `:root` scale). Charts
cycle these in order for series colors. `oklch` only (not email-safe).

### hex

&gt; `readonly` **hex**: `object`

#### hex.background

&gt; `readonly` **background**: `"#0A0E1A"` = `"#0A0E1A"`

#### hex.border

&gt; `readonly` **border**: `"#1E2438"` = `"#1E2438"`

#### hex.danger

&gt; `readonly` **danger**: `"#D43E3F"` = `"#D43E3F"`

#### hex.foreground

&gt; `readonly` **foreground**: `"#F0F2FA"` = `"#F0F2FA"`

#### hex.info

&gt; `readonly` **info**: `"#7D8CAE"` = `"#7D8CAE"`

#### hex.muted

&gt; `readonly` **muted**: `"#7D8CAE"` = `"#7D8CAE"`

#### hex.primary

&gt; `readonly` **primary**: `"#D43E3F"` = `"#D43E3F"`

#### hex.success

&gt; `readonly` **success**: `"#3FB984"` = `"#3FB984"`

#### hex.surface

&gt; `readonly` **surface**: `"#171C2B"` = `"#171C2B"`

#### hex.warning

&gt; `readonly` **warning**: `"#E0A100"` = `"#E0A100"`

### oklch

&gt; `readonly` **oklch**: `object`

#### oklch.background

&gt; `readonly` **background**: `"oklch(16.63% 0.0262 269.37)"` = `"oklch(16.63% 0.0262 269.37)"`

#### oklch.border

&gt; `readonly` **border**: `"oklch(26.45% 0.0386 270.81)"` = `"oklch(26.45% 0.0386 270.81)"`

#### oklch.foreground

&gt; `readonly` **foreground**: `"oklch(96.19% 0.0109 274.89)"` = `"oklch(96.19% 0.0109 274.89)"`

#### oklch.muted

&gt; `readonly` **muted**: `"oklch(64.00% 0.0535 266.82)"` = `"oklch(64.00% 0.0535 266.82)"`

#### oklch.primary

&gt; `readonly` **primary**: `"oklch(58.50% 0.1877 24.72)"` = `"oklch(58.50% 0.1877 24.72)"`

#### oklch.surface

&gt; `readonly` **surface**: `"oklch(19.72% 0.0231 268.80)"` = `"oklch(19.72% 0.0231 268.80)"`

## Example

```ts
import { colors } from "@resq-systems/constants/tokens";

colors.oklch.primary; // → "oklch(58.50% 0.1877 24.72)"
colors.hex.danger;    // → "#D43E3F" (status role — hex only)
```
