# Function: detectThreatPatterns()

&gt; **detectThreatPatterns**(`input`, `config?`): [`ThreatDetectionResult`](../interfaces/ThreatDetectionResult)

Defined in: [validators.ts:465](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/security/src/validators.ts#L465)

Run every enabled detector against `input` and aggregate findings.

Returns early-but-not-immediately: each individual detector still
runs to completion, but each detector returns at most one finding,
so the aggregate threats array is small (≤ 6 entries).

Non-string inputs (`null`, `undefined`, numbers, …) are treated as
safe — wrap caller-side validation around this if you want to
reject non-strings.

## Parameters

### input

`string`

The candidate string.

### config?

[`ThreatDetectionConfig`](../interfaces/ThreatDetectionConfig) = `DEFAULT_CONFIG`

Detector toggles. Defaults turn on everything
  except command-injection.

## Returns

[`ThreatDetectionResult`](../interfaces/ThreatDetectionResult)

`{ isSafe, threats }`.

## Example

```ts
const result = detectThreatPatterns(req.body.query);
if (!result.isSafe) return new Response(getThreatErrorMessage(result), { status: 400 });
```
