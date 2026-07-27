# Variable: DEFAULT\_PAIRS

&gt; `const` **DEFAULT\_PAIRS**: [`ContrastPair`](../interfaces/ContrastPair)[]

Defined in: [packages/ui/src/lib/contrast-audit.ts:572](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L572)

The full list of contrast pairs the design system commits to.
Every entry pairs a foreground token with a background surface and
encodes the WCAG-required ratio (4.5 : 1 for body text and small
UI text, 3 : 1 for non-text UI affordances).

Adding a new pair here automatically extends every theme's audit.
Keep entries grouped by category and sorted by surface for
readability.
