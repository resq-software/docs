# Function: containsHomoglyphs()

> **containsHomoglyphs**(`input`): [`ThreatFinding`](../interfaces/ThreatFinding)[]

Defined in: [validators.ts:379](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L379)

Detect lookalike Unicode characters (Cyrillic / Greek glyphs that
render identically to common ASCII letters). The classic phishing
trick is `paypaӏ.com` (`ӏ` instead of `l`); this detector catches
the building blocks.

Use [normalizeUnicode](./normalizeUnicode) to *replace* homoglyphs with their
ASCII equivalents — this function only flags their presence.

## Parameters

### input

`string`

String to scan.

## Returns

[`ThreatFinding`](../interfaces/ThreatFinding)[]

Empty array, or one finding of type `"homoglyph"` (the
  first matched lookalike).
