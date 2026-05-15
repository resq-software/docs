# Function: containsXSSPatterns()

> **containsXSSPatterns**(`input`): [`ThreatFinding`](../interfaces/ThreatFinding)[]

Defined in: [validators.ts:220](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L220)

Detect XSS-style payloads (script tags, event handlers, dangerous
URI schemes, prototype pollution, …) in a UTF-8 input.

Inputs longer than 100 000 characters are truncated before scanning
to bound regex evaluation cost and prevent ReDoS on crafted
payloads. Returns at most one finding — the regex catalog is
exhaustive enough that the first hit is sufficient for a
reject-or-sanitize decision.

## Parameters

### input

`string`

String to scan.

## Returns

[`ThreatFinding`](../interfaces/ThreatFinding)[]

Empty array when nothing matches, or a single
  [ThreatFinding](../interfaces/ThreatFinding) of type `"xss"`.

## Example

```ts
containsXSSPatterns(`<img src=x onerror="alert(1)">`);
// → [{ type: "xss", description: "...", matchedPattern: "onerror=" }]
```
