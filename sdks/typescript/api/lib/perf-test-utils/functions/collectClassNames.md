# Function: collectClassNames()

> **collectClassNames**(`element`): `string`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:450](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/lib/perf-test-utils.ts#L450)

Extracts all className strings from a React element tree (recursively).
Uses an array accumulator to avoid O(n²) string concatenation.

## Parameters

### element

`unknown`

## Returns

`string`
