# Function: collectSourceViolations()

> **collectSourceViolations**(`source`, `file`): [`PerfViolation`](../interfaces/PerfViolation.md)[]

Defined in: [packages/ui/src/lib/perf-test-utils.ts:193](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L193)

Collects **all** static performance violations from a source string.
Maps each violation to the Storybook Performance panel category it affects.

## Parameters

### source

`string`

### file

`string`

## Returns

[`PerfViolation`](../interfaces/PerfViolation.md)[]
