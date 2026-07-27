# Type Alias: StatusRole

&gt; **StatusRole** = `"info"` \| `"success"` \| `"warning"` \| `"danger"`

Defined in: [tokens.ts:48](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/constants/src/tokens.ts#L48)

Status roles that exist only in the email-safe `hex` snapshot. `oklch` does
not define these, so they are indexable on `colors.hex` but never on
[ColorRole](./ColorRole) / `colors.oklch` — the type split enforces that asymmetry at
compile time. In apps these four states come from the `@resq-systems/ui`
theme's own status tokens rather than from here; the hex copies exist so
transactional email (which can't evaluate `oklch()`) still has them.
