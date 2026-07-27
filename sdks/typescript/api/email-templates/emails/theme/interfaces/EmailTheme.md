# Interface: EmailTheme

Defined in: [packages/email-templates/src/emails/theme.tsx:76](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L76)

The full, resolved theme every template renders against.

## Properties

### colors

&gt; **colors**: `Record`\<`string`, `string`\>

Defined in: [packages/email-templates/src/emails/theme.tsx:78](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L78)

Color tokens → Tailwind `theme.extend.colors` (email-safe hex).

***

### fonts

&gt; **fonts**: [`EmailThemeFonts`](./EmailThemeFonts)

Defined in: [packages/email-templates/src/emails/theme.tsx:80](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L80)

Font stacks → Tailwind `theme.extend.fontFamily` (pre-quoted multi-word names).

***

### fontsHref?

&gt; `optional` **fontsHref?**: `string`

Defined in: [packages/email-templates/src/emails/theme.tsx:84](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L84)

Optional stylesheet `<link>` injected in `<Head>` for brand webfonts.

***

### org

&gt; **org**: [`EmailOrgIdentity`](./EmailOrgIdentity)

Defined in: [packages/email-templates/src/emails/theme.tsx:82](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/theme.tsx#L82)

Organization identity for header lockup, signatures, and legal footer.
