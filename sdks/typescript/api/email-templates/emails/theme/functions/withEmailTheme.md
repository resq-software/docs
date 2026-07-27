# Function: withEmailTheme()

&gt; **withEmailTheme**(`element`, `override?`): `ReactElement`

Defined in: [packages/email-templates/src/emails/theme.tsx:196](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L196)

Wrap an element so it renders against a theme override (used by `renderEmail`).
Returns the element unchanged when there is no override, so the default theme
flows through context.

Pure — builds a new provider element and does not mutate `element`.

## Parameters

### element

`ReactElement`

The email element tree to wrap.

### override?

[`EmailThemeOverride`](../interfaces/EmailThemeOverride)

Theme fields to overlay; when omitted, `element` is returned unchanged.

## Returns

`ReactElement`

`element`, wrapped in an [EmailThemeContext](../variables/EmailThemeContext) provider when an override is given.
