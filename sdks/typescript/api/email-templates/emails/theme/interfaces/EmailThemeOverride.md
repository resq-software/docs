# Interface: EmailThemeOverride

Defined in: [packages/email-templates/src/emails/theme.tsx:93](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L93)

A partial theme a consumer supplies to rebrand; unset keys fall back to the
base. All object fields are **shallow**-merged over the base one level deep (see
[resolveEmailTheme](../functions/resolveEmailTheme)), so supplying `colors` replaces only the named color
tokens, not the whole palette.

## Properties

### colors?

&gt; `optional` **colors?**: `Record`\<`string`, `string`\>

Defined in: [packages/email-templates/src/emails/theme.tsx:95](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L95)

Color tokens to override (email-safe hex); merged over the base palette.

***

### fonts?

&gt; `optional` **fonts?**: `Partial`\<[`EmailThemeFonts`](./EmailThemeFonts)\>

Defined in: [packages/email-templates/src/emails/theme.tsx:97](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L97)

Font stacks to override; unspecified stacks keep the base.

***

### fontsHref?

&gt; `optional` **fontsHref?**: `string` \| `null`

Defined in: [packages/email-templates/src/emails/theme.tsx:101](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L101)

Replace the webfont `<link>` href, or pass `null` to drop it entirely.

***

### org?

&gt; `optional` **org?**: `Partial`\<[`EmailOrgIdentity`](./EmailOrgIdentity)\>

Defined in: [packages/email-templates/src/emails/theme.tsx:99](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L99)

Override organization identity fields (shallow-merged over the base).
