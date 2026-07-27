# Variable: fonts

&gt; `const` **fonts**: `object`

Defined in: [tokens.ts:138](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/constants/src/tokens.ts#L138)

Brand typefaces, ready-to-use CSS font stacks, and the webfont stylesheet.

Within each [fonts.stacks](#stacks) array the **first** entry is the brand face
and the rest are ordered fallbacks the browser walks until one resolves;
multi-word family names are pre-quoted so the array can be joined into a
`font-family` value verbatim. [fonts.googleFontsHref](#googlefontshref) must stay in sync
with these families and the weights they're actually rendered at — a face or
weight used in the app but missing from the href won't load.

## Type Declaration

### body

&gt; `readonly` **body**: `"DM Sans"` = `"DM Sans"`

### display

&gt; `readonly` **display**: `"Syne"` = `"Syne"`

### googleFontsHref

&gt; `readonly` **googleFontsHref**: `"https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&family=DM+Mono:wght@500&display=swap"` = `"https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&family=DM+Mono:wght@500&display=swap"`

### mono

&gt; `readonly` **mono**: `"DM Mono"` = `"DM Mono"`

### stacks

&gt; `readonly` **stacks**: `object`

#### stacks.body

&gt; `readonly` **body**: readonly \[`"'DM Sans'"`, `"-apple-system"`, `"BlinkMacSystemFont"`, `"'Segoe UI'"`, `"Roboto"`, `"Helvetica"`, `"Arial"`, `"sans-serif"`\]

#### stacks.display

&gt; `readonly` **display**: readonly \[`"Syne"`, `"'Helvetica Neue'"`, `"Arial"`, `"sans-serif"`\]

#### stacks.mono

&gt; `readonly` **mono**: readonly \[`"'DM Mono'"`, `"ui-monospace"`, `"'SF Mono'"`, `"Menlo"`, `"Consolas"`, `"monospace"`\]
