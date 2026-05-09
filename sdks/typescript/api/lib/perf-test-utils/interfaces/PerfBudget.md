# Interface: PerfBudget

Defined in: [packages/ui/src/lib/perf-test-utils.ts:61](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L61)

Thresholds matching the Storybook Performance panel "good" ranges.

## Properties

### maxDomNodes

> **maxDomNodes**: `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:63](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L63)

Max DOM element count (Memory & Rendering panel). Default: 800.

***

### maxElementNodes

> **maxElementNodes**: `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:67](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L67)

Max React element count in a single component tree. Default: 200.

***

### maxInlineStyles

> **maxInlineStyles**: `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:69](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L69)

Max inline `style` props allowed (Style Writes). Default: 0.

***

### maxNestingDepth

> **maxNestingDepth**: `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:65](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L65)

Max nesting depth. Default: 12.

***

### maxWillChange

> **maxWillChange**: `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:71](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L71)

Max `will-change` declarations (Frame Timing). Default: 3.
