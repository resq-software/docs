# Function: containsPathTraversal()

> **containsPathTraversal**(`input`): [`ThreatFinding`](../interfaces/ThreatFinding)[]

Defined in: [validators.ts:348](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/security/src/validators.ts#L348)

Detect path-traversal payloads — `../`, encoded dots, raw absolute
paths trying to escape a base directory. Pair with `path.resolve()`
+ a `startsWith()` containment check on the canonicalised path
before reading or writing the file.

## Parameters

### input

`string`

String to scan.

## Returns

[`ThreatFinding`](../interfaces/ThreatFinding)[]

Empty array, or one finding of type `"path_traversal"`.
