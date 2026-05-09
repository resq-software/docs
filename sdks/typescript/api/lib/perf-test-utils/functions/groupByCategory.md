# Function: groupByCategory()

> **groupByCategory**(`violations`): `Record`\<[`PerfViolation`](../interfaces/PerfViolation.md)\[`"category"`\], [`PerfViolation`](../interfaces/PerfViolation.md)[]\>

Defined in: [packages/ui/src/lib/perf-test-utils.ts:637](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L637)

Groups violations by category for structured reporting that mirrors the
Storybook Performance panel layout.

## Parameters

### violations

[`PerfViolation`](../interfaces/PerfViolation.md)[]

## Returns

`Record`\<[`PerfViolation`](../interfaces/PerfViolation.md)\[`"category"`\], [`PerfViolation`](../interfaces/PerfViolation.md)[]\>
