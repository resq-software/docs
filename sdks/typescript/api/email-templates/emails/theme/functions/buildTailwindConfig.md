# Function: buildTailwindConfig()

&gt; **buildTailwindConfig**(`theme`): `object`

Defined in: [packages/email-templates/src/emails/theme.tsx:166](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L166)

Build the `<Tailwind config>` object from a resolved theme.

Pure — projects the theme's colors and font stacks into a Tailwind
`theme.extend` config atop the pixel-based preset (email clients need px units,
not rem).

## Parameters

### theme

[`EmailTheme`](../interfaces/EmailTheme)

The resolved theme to project.

## Returns

`object`

The config object to pass to react-email's `<Tailwind>`.

### presets

&gt; **presets**: `TailwindConfig`[]

### theme

&gt; **theme**: `object`

#### theme.extend

&gt; **extend**: `object`

#### theme.extend.colors

&gt; **colors**: `object`

##### Index Signature

\[`key`: `string`\]: `string`

#### theme.extend.fontFamily

&gt; **fontFamily**: `object`

#### theme.extend.fontFamily.display

&gt; **display**: `string`[]

#### theme.extend.fontFamily.mono

&gt; **mono**: `string`[]

#### theme.extend.fontFamily.sans

&gt; **sans**: `string`[]
