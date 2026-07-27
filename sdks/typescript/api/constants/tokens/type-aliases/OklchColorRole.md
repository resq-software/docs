# Type Alias: OklchColorRole

&gt; **OklchColorRole** = keyof *typeof* [`oklch`](../variables/colors#oklch)

Defined in: [tokens.ts:110](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/constants/src/tokens.ts#L110)

Roles indexable on `colors.oklch` — exactly [ColorRole](./ColorRole). Type any
lookup into the oklch source with this so a hex-only [StatusRole](./StatusRole) can
never index it (which would type as `string` yet be `undefined` at runtime).
