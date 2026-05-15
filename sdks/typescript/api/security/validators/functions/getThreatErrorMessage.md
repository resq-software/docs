# Function: getThreatErrorMessage()

> **getThreatErrorMessage**(`result`): `string`

Defined in: [validators.ts:660](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L660)

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
