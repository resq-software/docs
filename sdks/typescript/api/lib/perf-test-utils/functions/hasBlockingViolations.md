# Function: hasBlockingViolations()

> **hasBlockingViolations**(`violations`): `boolean`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:629](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L629)

Returns true if any violation in the list is severity: "error".
Use as the gate for CI pass/fail.

## Parameters

### violations

[`PerfViolation`](../interfaces/PerfViolation.md)[]

## Returns

`boolean`
