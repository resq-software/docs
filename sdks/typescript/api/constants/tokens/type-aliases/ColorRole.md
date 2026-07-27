# Type Alias: ColorRole

&gt; **ColorRole** = `"background"` \| `"surface"` \| `"border"` \| `"foreground"` \| `"muted"` \| `"primary"`

Defined in: [tokens.ts:38](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/constants/src/tokens.ts#L38)

The six canonical color roles present in **both** representations. `oklch`
(the design-system source of truth) and `hex` (the email-safe snapshot) must
each define every one of these.

These are semantic *roles*, not raw swatches: consumers reference
`colors.oklch.primary`, never the literal channel values, so a palette change
updates the token once. The union has no meaningful ordering — membership, not
position, is the contract.
