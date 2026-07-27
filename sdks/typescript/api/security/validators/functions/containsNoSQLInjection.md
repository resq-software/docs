# Function: containsNoSQLInjection()

&gt; **containsNoSQLInjection**(`input`): [`ThreatFinding`](../interfaces/ThreatFinding)[]

Defined in: [validators.ts:289](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L289)

Detect NoSQL-injection patterns — Mongo-style operator injection
(`$where`, `$ne`, `$regex`), JavaScript-in-query payloads, and
structural manipulators that can bypass auth filters in document
stores.

## Parameters

### input

`string`

String to scan.

## Returns

[`ThreatFinding`](../interfaces/ThreatFinding)[]

Empty array, or one finding of type `"nosql_injection"`.
