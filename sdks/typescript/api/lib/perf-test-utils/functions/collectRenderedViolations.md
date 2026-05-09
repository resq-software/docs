# Function: collectRenderedViolations()

> **collectRenderedViolations**(`element`, `componentName`, `budget?`): [`PerfViolation`](../interfaces/PerfViolation.md)[]

Defined in: [packages/ui/src/lib/perf-test-utils.ts:516](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L516)

Runs all rendered-output checks against a React element tree and returns
violations mapped to performance panel categories. Pass a partial budget
to override defaults.

## Parameters

### element

`unknown`

### componentName

`string`

### budget?

`Partial`\<[`PerfBudget`](../interfaces/PerfBudget.md)\> = `&#123;&#125;`

## Returns

[`PerfViolation`](../interfaces/PerfViolation.md)[]
