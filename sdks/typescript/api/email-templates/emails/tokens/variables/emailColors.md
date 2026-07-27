# Variable: emailColors

&gt; `const` **emailColors**: `any` = `colors.hex`

Defined in: [packages/email-templates/src/emails/tokens.ts:33](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/email-templates/src/emails/tokens.ts#L33)

Email-safe hex color tokens, sourced from the shared `@resq-systems/constants`
design tokens so the brand palette lives in one place across apps. Email
clients don't support `oklch()`, so the hex snapshot is used here.
