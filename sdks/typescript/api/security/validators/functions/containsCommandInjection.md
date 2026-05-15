# Function: containsCommandInjection()

> **containsCommandInjection**(`input`): [`ThreatFinding`](../interfaces/ThreatFinding)[]

Defined in: [validators.ts:311](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L311)

Detect shell command-injection patterns: command substitution
(`$(...)`, backticks), chained dangerous commands (`; rm`, `; curl`,
…) and shell-piped exec (`| sh`, `| bash`).

**Off by default in [detectThreatPatterns](./detectThreatPatterns)** — these patterns
occasionally fire on legitimate user content. Enable explicitly
(`checkCommandInjection: true`) only when input flows into a child
process or shell.

## Parameters

### input

`string`

String to scan. Truncated at 100 000 characters.

## Returns

[`ThreatFinding`](../interfaces/ThreatFinding)[]

Empty array, or one finding of type `"command_injection"`.
