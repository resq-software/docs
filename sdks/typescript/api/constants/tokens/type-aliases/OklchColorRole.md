# Type Alias: OklchColorRole

&gt; **OklchColorRole** = keyof *typeof* [`oklch`](../variables/colors#oklch)

Defined in: [tokens.ts:110](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/constants/src/tokens.ts#L110)

Roles indexable on `colors.oklch` — exactly [ColorRole](./ColorRole). Type any
lookup into the oklch source with this so a hex-only [StatusRole](./StatusRole) can
never index it (which would type as `string` yet be `undefined` at runtime).
