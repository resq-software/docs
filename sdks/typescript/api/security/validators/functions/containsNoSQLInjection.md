# Function: containsNoSQLInjection()

> **containsNoSQLInjection**(`input`): [`ThreatFinding`](../interfaces/ThreatFinding)[]

Defined in: [validators.ts:280](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L280)

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
