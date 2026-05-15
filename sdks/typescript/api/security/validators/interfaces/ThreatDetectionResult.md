# Interface: ThreatDetectionResult

Defined in: [validators.ts:168](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L168)

Outcome of [detectThreatPatterns](../functions/detectThreatPatterns).

`isSafe` is the boolean shortcut; `threats` is the full list of
findings (one per detector that fired). Use
[getThreatErrorMessage](../functions/getThreatErrorMessage) to render a user-facing message for
the first finding.

## Properties

### isSafe

> **isSafe**: `boolean`

Defined in: [validators.ts:170](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L170)

`true` when no detectors fired. Equivalent to `threats.length === 0`.

***

### threats

> **threats**: [`ThreatFinding`](./ThreatFinding)[]

Defined in: [validators.ts:172](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L172)

All findings produced by enabled detectors, in detector order.
