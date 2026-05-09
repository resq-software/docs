# Function: collectSourceViolations()

> **collectSourceViolations**(`source`, `file`): [`PerfViolation`](../interfaces/PerfViolation.md)[]

Defined in: [packages/ui/src/lib/perf-test-utils.ts:193](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L193)

Collects **all** static performance violations from a source string.
Maps each violation to the Storybook Performance panel category it affects.

## Parameters

### source

`string`

### file

`string`

## Returns

[`PerfViolation`](../interfaces/PerfViolation.md)[]
