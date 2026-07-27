# Function: getThreatErrorMessage()

&gt; **getThreatErrorMessage**(`result`): `string`

Defined in: [validators.ts:669](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L669)

Map a [ThreatDetectionResult](../interfaces/ThreatDetectionResult) into a user-facing error
message string suitable for an HTTP 400 response or form
validation error. Returns `""` when the result is safe (so
`error || undefined` works).

Uses only the **first** finding for the message — exposing every
threat type to the user can leak information about the detection
rules. For full diagnostics, log `result.threats` server-side
rather than returning them.

## Parameters

### result

[`ThreatDetectionResult`](../interfaces/ThreatDetectionResult)

## Returns

`string`
