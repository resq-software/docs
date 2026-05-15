# Interface: ThreatFinding

Defined in: [validators.ts:179](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L179)

A single detector hit. Detectors that fire return at most one
finding per call (one example is enough to reject the input).

## Properties

### description

> **description**: `string`

Defined in: [validators.ts:183](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L183)

Human-readable description suitable for log lines (not for end users — use [getThreatErrorMessage](../functions/getThreatErrorMessage) instead).

***

### matchedPattern?

> `optional` **matchedPattern?**: `string`

Defined in: [validators.ts:185](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L185)

First 50 chars of the matching substring, for diagnostics. Truncated to prevent leaking large payloads in logs.

***

### type

> **type**: [`ThreatType`](../type-aliases/ThreatType)

Defined in: [validators.ts:181](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L181)

Which detector matched.
