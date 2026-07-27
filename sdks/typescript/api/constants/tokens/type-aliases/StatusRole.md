# Type Alias: StatusRole

&gt; **StatusRole** = `"info"` \| `"success"` \| `"warning"` \| `"danger"`

Defined in: [tokens.ts:48](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/constants/src/tokens.ts#L48)

Status roles that exist only in the email-safe `hex` snapshot. `oklch` does
not define these, so they are indexable on `colors.hex` but never on
[ColorRole](./ColorRole) / `colors.oklch` — the type split enforces that asymmetry at
compile time. In apps these four states come from the `@resq-systems/ui`
theme's own status tokens rather than from here; the hex copies exist so
transactional email (which can't evaluate `oklch()`) still has them.
