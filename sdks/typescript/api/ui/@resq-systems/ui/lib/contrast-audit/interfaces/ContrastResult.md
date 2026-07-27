# Interface: ContrastResult

Defined in: [packages/ui/src/lib/contrast-audit.ts:52](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L52)

Result of evaluating a single [ContrastPair](./ContrastPair) against a theme.

## Properties

### bg

&gt; **bg**: `string`

Defined in: [packages/ui/src/lib/contrast-audit.ts:54](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L54)

***

### bgRaw

&gt; **bgRaw**: `string`

Defined in: [packages/ui/src/lib/contrast-audit.ts:58](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L58)

Raw CSS color value of the background.

***

### fg

&gt; **fg**: `string`

Defined in: [packages/ui/src/lib/contrast-audit.ts:53](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L53)

***

### fgRaw

&gt; **fgRaw**: `string`

Defined in: [packages/ui/src/lib/contrast-audit.ts:56](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L56)

Raw CSS color value of the foreground (whatever was in the token map).

***

### label

&gt; **label**: `string`

Defined in: [packages/ui/src/lib/contrast-audit.ts:63](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L63)

***

### pass

&gt; **pass**: `boolean`

Defined in: [packages/ui/src/lib/contrast-audit.ts:65](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L65)

`true` when `ratio >= required`.

***

### ratio

&gt; **ratio**: `number`

Defined in: [packages/ui/src/lib/contrast-audit.ts:60](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L60)

Computed contrast ratio (≥ 1, higher is better).

***

### required

&gt; **required**: `number`

Defined in: [packages/ui/src/lib/contrast-audit.ts:62](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L62)

The minimum ratio that was required to pass.
