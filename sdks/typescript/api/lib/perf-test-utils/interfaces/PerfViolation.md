# Interface: PerfViolation

Defined in: [packages/ui/src/lib/perf-test-utils.ts:43](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L43)

A single performance violation with category mapping.

## Properties

### category

> **category**: `"frame-timing"` \| `"layout-stability"` \| `"react-performance"` \| `"dom-nodes"` \| `"style-writes"` \| `"input-responsiveness"` \| `"element-timing"`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:45](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L45)

Which perf panel category this maps to.

***

### match?

> `optional` **match?**: `string`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:55](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L55)

***

### message

> **message**: `string`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:54](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L54)

***

### rule

> **rule**: `string`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:53](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L53)

***

### severity

> **severity**: `"error"` \| `"warning"`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:57](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L57)

Severity: 'error' blocks CI, 'warning' shows up in reports.
