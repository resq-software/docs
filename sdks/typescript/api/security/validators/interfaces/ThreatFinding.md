# Interface: ThreatFinding

Defined in: [validators.ts:185](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L185)

A single detector hit. Detectors that fire return at most one
finding per call (one example is enough to reject the input).

## Properties

### description

&gt; **description**: `string`

Defined in: [validators.ts:189](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L189)

Human-readable description suitable for log lines (not for end users — use [getThreatErrorMessage](../functions/getThreatErrorMessage) instead).

***

### matchedPattern?

&gt; `optional` **matchedPattern?**: `string`

Defined in: [validators.ts:191](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L191)

First 50 chars of the matching substring, for diagnostics. Truncated to prevent leaking large payloads in logs.

***

### type

&gt; **type**: [`ThreatType`](../type-aliases/ThreatType)

Defined in: [validators.ts:187](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L187)

Discriminant: which detector matched. See [ThreatType](../type-aliases/ThreatType).
