# Function: containsSQLInjection()

> **containsSQLInjection**(`input`): [`ThreatFinding`](../interfaces/ThreatFinding)[]

Defined in: [validators.ts:252](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L252)

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
