# Interface: ContrastPair

Defined in: [packages/ui/src/lib/contrast-audit.ts:40](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L40)

Specification for one contrast check: foreground token, background
token, required WCAG ratio, and a category label for reports.

## Properties

### bg

&gt; **bg**: `string`

Defined in: [packages/ui/src/lib/contrast-audit.ts:44](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L44)

Background token name.

***

### fg

&gt; **fg**: `string`

Defined in: [packages/ui/src/lib/contrast-audit.ts:42](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L42)

Foreground token name.

***

### label

&gt; **label**: `string`

Defined in: [packages/ui/src/lib/contrast-audit.ts:48](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L48)

Free-form category label (`"text"`, `"UI"`, `"large"`, …).

***

### minRatio

&gt; **minRatio**: `number`

Defined in: [packages/ui/src/lib/contrast-audit.ts:46](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/contrast-audit.ts#L46)

Minimum ratio required (4.5 for normal text, 3 for UI / large text).
