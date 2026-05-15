# Function: normalizeUnicode()

> **normalizeUnicode**(`input`): `string`

Defined in: [validators.ts:552](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L552)

Canonicalise a string for safe equality checks against ASCII.

Two-pass:
1. Normalize to NFC (composed form) so combining-character
   sequences don't compare differently from their pre-composed
   counterparts.
2. Replace known homoglyphs (Cyrillic `А`, Greek `Ε`, …) with their
   ASCII equivalents (`A`, `E`, …).

Use before storing user-controlled identifiers (usernames, domain
names) and before comparing them to a denylist or to each other.

Returns `""` for non-string or empty input.

## Parameters

### input

`string`

Raw string from an untrusted source.

## Returns

`string`

ASCII-normalized, NFC-composed string.
