# Function: hasBlockingViolations()

> **hasBlockingViolations**(`violations`): `boolean`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:629](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/lib/perf-test-utils.ts#L629)

Returns true if any violation in the list is severity: "error".
Use as the gate for CI pass/fail.

## Parameters

### violations

[`PerfViolation`](../interfaces/PerfViolation.md)[]

## Returns

`boolean`
