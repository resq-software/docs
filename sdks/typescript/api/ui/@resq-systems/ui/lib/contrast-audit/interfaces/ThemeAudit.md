# Interface: ThemeAudit

Defined in: [packages/ui/src/lib/contrast-audit.ts:69](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L69)

Aggregated result of auditing one theme mode (`"dark"`, `"light"`, …).

## Properties

### allPass

&gt; **allPass**: `boolean`

Defined in: [packages/ui/src/lib/contrast-audit.ts:75](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L75)

`true` when every result passed.

***

### mode

&gt; **mode**: `string`

Defined in: [packages/ui/src/lib/contrast-audit.ts:71](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L71)

Theme identifier echoed back from the input.

***

### results

&gt; **results**: [`ContrastResult`](./ContrastResult)[]

Defined in: [packages/ui/src/lib/contrast-audit.ts:73](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L73)

One [ContrastResult](./ContrastResult) per pair audited (skipping pairs whose tokens were missing).
