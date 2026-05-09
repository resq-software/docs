# Function: collectRenderedViolations()

> **collectRenderedViolations**(`element`, `componentName`, `budget?`): [`PerfViolation`](../interfaces/PerfViolation.md)[]

Defined in: [packages/ui/src/lib/perf-test-utils.ts:516](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L516)

Runs all rendered-output checks against a React element tree and returns
violations mapped to performance panel categories. Pass a partial budget
to override defaults.

## Parameters

### element

`unknown`

### componentName

`string`

### budget?

`Partial`\<[`PerfBudget`](../interfaces/PerfBudget.md)\> = `{}`

## Returns

[`PerfViolation`](../interfaces/PerfViolation.md)[]
