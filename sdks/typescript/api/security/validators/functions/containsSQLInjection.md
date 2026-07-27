# Function: containsSQLInjection()

&gt; **containsSQLInjection**(`input`): [`ThreatFinding`](../interfaces/ThreatFinding)[]

Defined in: [validators.ts:261](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L261)

Detect SQL-injection patterns (UNION SELECT, DROP TABLE,
comment-based bypasses, always-true tautologies, stacked queries)
in input.

**Not a replacement for parameterised queries.** Use this as a
defense-in-depth signal in addition to a properly bound prepared
statement, never as the only barrier.

## Parameters

### input

`string`

String to scan. Truncated at 100 000 characters.

## Returns

[`ThreatFinding`](../interfaces/ThreatFinding)[]

Empty array, or one finding of type `"sql_injection"`.
