# Function: containsPathTraversal()

&gt; **containsPathTraversal**(`input`): [`ThreatFinding`](../interfaces/ThreatFinding)[]

Defined in: [validators.ts:357](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L357)

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
