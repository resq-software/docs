# Function: collectClassNames()

&gt; **collectClassNames**(`element`): `string`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:501](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L501)

Extracts all className strings from a React element tree (recursively).
Uses an array accumulator to avoid O(n²) string concatenation.

## Parameters

### element

`unknown`

## Returns

`string`
