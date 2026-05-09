# Function: groupByCategory()

> **groupByCategory**(`violations`): `Record`\<[`PerfViolation`](../interfaces/PerfViolation.md)\[`"category"`\], [`PerfViolation`](../interfaces/PerfViolation.md)[]\>

Defined in: [packages/ui/src/lib/perf-test-utils.ts:637](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/lib/perf-test-utils.ts#L637)

Groups violations by category for structured reporting that mirrors the
Storybook Performance panel layout.

## Parameters

### violations

[`PerfViolation`](../interfaces/PerfViolation.md)[]

## Returns

`Record`\<[`PerfViolation`](../interfaces/PerfViolation.md)\[`"category"`\], [`PerfViolation`](../interfaces/PerfViolation.md)[]\>
