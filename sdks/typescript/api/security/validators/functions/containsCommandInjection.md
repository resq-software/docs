# Function: containsCommandInjection()

&gt; **containsCommandInjection**(`input`): [`ThreatFinding`](../interfaces/ThreatFinding)[]

Defined in: [validators.ts:320](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L320)

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
