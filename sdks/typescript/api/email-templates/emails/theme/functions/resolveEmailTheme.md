# Function: resolveEmailTheme()

&gt; **resolveEmailTheme**(`base`, `override?`): [`EmailTheme`](../interfaces/EmailTheme)

Defined in: [packages/email-templates/src/emails/theme.tsx:133](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L133)

Merge an override onto a base theme, producing a new resolved theme.

Pure — never mutates `base`. `colors`, `fonts`, and `org` are **shallow**-merged
(override keys replace base keys one level deep), so a partial `fonts` override
keeps the base's other stacks. `fontsHref` follows a three-way rule: `null`
drops the webfont link entirely, absent/`undefined` keeps the base href, and any
string replaces it.

## Parameters

### base

[`EmailTheme`](../interfaces/EmailTheme)

The theme to start from.

### override?

[`EmailThemeOverride`](../interfaces/EmailThemeOverride)

Fields to overlay; when omitted, `base` is returned by reference.

## Returns

[`EmailTheme`](../interfaces/EmailTheme)

The merged theme, or `base` itself when there is no override.
