# Function: collectRenderedViolations()

&gt; **collectRenderedViolations**(`element`, `componentName`, `budget?`): [`PerfViolation`](../interfaces/PerfViolation)[]

Defined in: [packages/ui/src/lib/perf-test-utils.ts:589](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L589)

Runs all rendered-output checks against a React element tree and returns
violations mapped to performance panel categories. Pass a partial budget
to override defaults.

## Parameters

### element

`unknown`

### componentName

`string`

### budget?

`Partial`\<[`PerfBudget`](../interfaces/PerfBudget)\> = `{}`

## Returns

[`PerfViolation`](../interfaces/PerfViolation)[]
