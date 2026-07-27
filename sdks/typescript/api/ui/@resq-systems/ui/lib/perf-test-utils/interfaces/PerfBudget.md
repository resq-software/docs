# Interface: PerfBudget

Defined in: [packages/ui/src/lib/perf-test-utils.ts:64](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L64)

Thresholds matching the Storybook Performance panel "good" ranges.

## Properties

### maxDomNodes

&gt; **maxDomNodes**: `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:66](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L66)

Max DOM element count (Memory & Rendering panel). Default: 800.

***

### maxElementNodes

&gt; **maxElementNodes**: `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:70](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L70)

Max React element count in a single component tree. Default: 200.

***

### maxInlineStyles

&gt; **maxInlineStyles**: `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:72](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L72)

Max inline `style` props allowed (Style Writes). Default: 0.

***

### maxNestingDepth

&gt; **maxNestingDepth**: `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:68](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L68)

Max nesting depth. Default: 12.

***

### maxWillChange

&gt; **maxWillChange**: `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:74](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L74)

Max `will-change` declarations (Frame Timing). Default: 3.
