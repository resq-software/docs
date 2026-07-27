# Interface: ThreatDetectionResult

Defined in: [validators.ts:174](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L174)

Outcome of [detectThreatPatterns](../functions/detectThreatPatterns).

`isSafe` is the boolean shortcut; `threats` is the full list of
findings (one per detector that fired). Use
[getThreatErrorMessage](../functions/getThreatErrorMessage) to render a user-facing message for
the first finding.

## Properties

### isSafe

&gt; **isSafe**: `boolean`

Defined in: [validators.ts:176](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L176)

`true` when no detectors fired. Equivalent to `threats.length === 0`.

***

### threats

&gt; **threats**: [`ThreatFinding`](./ThreatFinding)[]

Defined in: [validators.ts:178](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L178)

All findings produced by enabled detectors, in detector order.
