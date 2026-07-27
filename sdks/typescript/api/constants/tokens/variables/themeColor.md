# Variable: themeColor

&gt; `const` **themeColor**: `object`

Defined in: [tokens.ts:123](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/constants/src/tokens.ts#L123)

Browser + PWA `theme-color` / viewport meta colors, keyed by
`prefers-color-scheme`. `dark` is aliased to [colors](./colors)`.hex.background`
(not a re-typed copy) so the browser chrome always matches the dark page
background exactly; `light` is a standalone light-mode chrome color with no
palette counterpart. Hex, not oklch, because `<meta name="theme-color">`
across browsers doesn't accept `oklch()`.

## Type Declaration

### dark

&gt; `readonly` **dark**: `"#0A0E1A"` = `colors.hex.background`

### light

&gt; `readonly` **light**: `"#E8EAF0"` = `"#E8EAF0"`
