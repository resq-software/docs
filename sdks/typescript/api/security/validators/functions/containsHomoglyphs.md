# Function: containsHomoglyphs()

&gt; **containsHomoglyphs**(`input`): [`ThreatFinding`](../interfaces/ThreatFinding)[]

Defined in: [validators.ts:388](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L388)

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
