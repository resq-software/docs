# Function: groupByCategory()

> **groupByCategory**(`violations`): `Record`\<[`PerfViolation`](../interfaces/PerfViolation.md)\[`"category"`\], [`PerfViolation`](../interfaces/PerfViolation.md)[]\>

Defined in: [packages/ui/src/lib/perf-test-utils.ts:637](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L637)

Groups violations by category for structured reporting that mirrors the
Storybook Performance panel layout.

## Parameters

### violations

[`PerfViolation`](../interfaces/PerfViolation.md)[]

## Returns

`Record`\<[`PerfViolation`](../interfaces/PerfViolation.md)\[`"category"`\], [`PerfViolation`](../interfaces/PerfViolation.md)[]\>
