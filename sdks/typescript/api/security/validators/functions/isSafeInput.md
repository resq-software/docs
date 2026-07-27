# Function: isSafeInput()

&gt; **isSafeInput**(`input`, `config?`): `boolean`

Defined in: [validators.ts:513](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L513)

Boolean shortcut over [detectThreatPatterns](./detectThreatPatterns) — discards the
findings list when you only need a yes/no decision.

## Parameters

### input

`string`

String to test.

### config?

[`ThreatDetectionConfig`](../interfaces/ThreatDetectionConfig)

Optional detector toggles.

## Returns

`boolean`

`true` when no detector fires.
