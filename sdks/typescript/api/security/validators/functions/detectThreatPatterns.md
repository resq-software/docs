# Function: detectThreatPatterns()

> **detectThreatPatterns**(`input`, `config?`): [`ThreatDetectionResult`](../interfaces/ThreatDetectionResult)

Defined in: [validators.ts:352](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/security/src/validators.ts#L352)

Runs all configured threat detectors on input

## Parameters

### input

`string`

The string to check

### config?

[`ThreatDetectionConfig`](../interfaces/ThreatDetectionConfig) = `DEFAULT_CONFIG`

Optional configuration for which checks to run

## Returns

[`ThreatDetectionResult`](../interfaces/ThreatDetectionResult)

Detection result with any findings
