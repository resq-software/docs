# Function: collectSourceViolations()

&gt; **collectSourceViolations**(`source`, `file`): [`PerfViolation`](../interfaces/PerfViolation)[]

Defined in: [packages/ui/src/lib/perf-test-utils.ts:236](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L236)

Collects **all** static performance violations from a source string.
Maps each violation to the Storybook Performance panel category it affects.

## Parameters

### source

`string`

### file

`string`

## Returns

[`PerfViolation`](../interfaces/PerfViolation)[]
