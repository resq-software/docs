# Function: groupByCategory()

&gt; **groupByCategory**(`violations`): `Record`\<[`PerfViolation`](../interfaces/PerfViolation)\[`"category"`\], [`PerfViolation`](../interfaces/PerfViolation)[]\>

Defined in: [packages/ui/src/lib/perf-test-utils.ts:710](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L710)

Groups violations by category for structured reporting that mirrors the
Storybook Performance panel layout.

## Parameters

### violations

[`PerfViolation`](../interfaces/PerfViolation)[]

## Returns

`Record`\<[`PerfViolation`](../interfaces/PerfViolation)\[`"category"`\], [`PerfViolation`](../interfaces/PerfViolation)[]\>
