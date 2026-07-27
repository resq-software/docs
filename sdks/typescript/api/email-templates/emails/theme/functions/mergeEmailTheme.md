# Function: mergeEmailTheme()

&gt; **mergeEmailTheme**(`override?`): [`EmailTheme`](../interfaces/EmailTheme)

Defined in: [packages/email-templates/src/emails/theme.tsx:152](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L152)

Merge an override onto the default ResQ Systems theme.

Pure convenience wrapper over [resolveEmailTheme](./resolveEmailTheme) with
[defaultEmailTheme](../variables/defaultEmailTheme) as the base.

## Parameters

### override?

[`EmailThemeOverride`](../interfaces/EmailThemeOverride)

Fields to overlay on the default theme.

## Returns

[`EmailTheme`](../interfaces/EmailTheme)

The resolved theme.
