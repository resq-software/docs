# Interface: EmailThemeFonts

Defined in: [packages/email-templates/src/emails/theme.tsx:38](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L38)

Font stacks the theme exposes to Tailwind's `fontFamily` extension. Each array
is a CSS font-family stack in priority order (preferred face first, generic
fallback last); multi-word names are pre-quoted so they drop straight into a
`font-family` value.

## Properties

### display

&gt; **display**: `string`[]

Defined in: [packages/email-templates/src/emails/theme.tsx:40](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L40)

Stack for display/heading text.

***

### mono

&gt; **mono**: `string`[]

Defined in: [packages/email-templates/src/emails/theme.tsx:44](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L44)

Stack for monospace text (codes, metadata).

***

### sans

&gt; **sans**: `string`[]

Defined in: [packages/email-templates/src/emails/theme.tsx:42](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L42)

Stack for body/sans text.
