# Type Alias: ColorRole

&gt; **ColorRole** = `"background"` \| `"surface"` \| `"border"` \| `"foreground"` \| `"muted"` \| `"primary"`

Defined in: [tokens.ts:38](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/constants/src/tokens.ts#L38)

The six canonical color roles present in **both** representations. `oklch`
(the design-system source of truth) and `hex` (the email-safe snapshot) must
each define every one of these.

These are semantic *roles*, not raw swatches: consumers reference
`colors.oklch.primary`, never the literal channel values, so a palette change
updates the token once. The union has no meaningful ordering — membership, not
position, is the contract.
