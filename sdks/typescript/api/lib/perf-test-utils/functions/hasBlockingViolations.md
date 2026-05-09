# Function: hasBlockingViolations()

> **hasBlockingViolations**(`violations`): `boolean`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:629](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L629)

Returns true if any violation in the list is severity: "error".
Use as the gate for CI pass/fail.

## Parameters

### violations

[`PerfViolation`](../interfaces/PerfViolation.md)[]

## Returns

`boolean`
