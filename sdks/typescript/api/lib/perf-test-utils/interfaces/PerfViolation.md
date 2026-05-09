# Interface: PerfViolation

Defined in: [packages/ui/src/lib/perf-test-utils.ts:43](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L43)

A single performance violation with category mapping.

## Properties

### category

> **category**: `"frame-timing"` \| `"layout-stability"` \| `"react-performance"` \| `"dom-nodes"` \| `"style-writes"` \| `"input-responsiveness"` \| `"element-timing"`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:45](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L45)

Which perf panel category this maps to.

***

### match?

> `optional` **match?**: `string`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:55](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L55)

***

### message

> **message**: `string`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:54](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L54)

***

### rule

> **rule**: `string`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:53](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L53)

***

### severity

> **severity**: `"error"` \| `"warning"`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:57](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L57)

Severity: 'error' blocks CI, 'warning' shows up in reports.
