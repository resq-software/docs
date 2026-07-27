# Interface: PerfViolation

Defined in: [packages/ui/src/lib/perf-test-utils.ts:43](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L43)

A single performance violation with category mapping.

## Properties

### category

&gt; **category**: `"frame-timing"` \| `"layout-stability"` \| `"react-performance"` \| `"dom-nodes"` \| `"style-writes"` \| `"input-responsiveness"` \| `"element-timing"`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:45](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L45)

Which perf panel category this maps to.

***

### match?

&gt; `optional` **match?**: `string`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:58](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L58)

The offending substring, when the rule matched a specific literal; absent for count/threshold rules that have no single culprit.

***

### message

&gt; **message**: `string`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:56](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L56)

Human-readable, file-prefixed explanation for reports.

***

### rule

&gt; **rule**: `string`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:54](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L54)

Stable machine-readable rule id (e.g. `"no-transition-all"`).

***

### severity

&gt; **severity**: `"error"` \| `"warning"`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:60](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L60)

Severity: 'error' blocks CI, 'warning' shows up in reports.
