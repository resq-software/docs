# Function: containsCommandInjection()

> **containsCommandInjection**(`input`): [`ThreatFinding`](../interfaces/ThreatFinding.md)[]

Defined in: [validators.ts:249](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/security/src/validators.ts#L249)

Detects command injection patterns in input
Note: This is strict - may trigger false positives on legitimate characters

## Parameters

### input

`string`

## Returns

[`ThreatFinding`](../interfaces/ThreatFinding.md)[]
