# Function: hasBlockingViolations()

&gt; **hasBlockingViolations**(`violations`): `boolean`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:702](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L702)

Returns true if any violation in the list is severity: "error".
Use as the gate for CI pass/fail.

## Parameters

### violations

[`PerfViolation`](../interfaces/PerfViolation)[]

## Returns

`boolean`
