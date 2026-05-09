# Function: collectSourceViolations()

> **collectSourceViolations**(`source`, `file`): [`PerfViolation`](../interfaces/PerfViolation.md)[]

Defined in: [packages/ui/src/lib/perf-test-utils.ts:193](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/lib/perf-test-utils.ts#L193)

Collects **all** static performance violations from a source string.
Maps each violation to the Storybook Performance panel category it affects.

## Parameters

### source

`string`

### file

`string`

## Returns

[`PerfViolation`](../interfaces/PerfViolation.md)[]
