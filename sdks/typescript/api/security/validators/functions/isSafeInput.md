# Function: isSafeInput()

> **isSafeInput**(`input`, `config?`): `boolean`

Defined in: [validators.ts:504](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L504)

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
