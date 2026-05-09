# Function: collectRenderedViolations()

> **collectRenderedViolations**(`element`, `componentName`, `budget?`): [`PerfViolation`](../interfaces/PerfViolation.md)[]

Defined in: [packages/ui/src/lib/perf-test-utils.ts:516](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/lib/perf-test-utils.ts#L516)

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
