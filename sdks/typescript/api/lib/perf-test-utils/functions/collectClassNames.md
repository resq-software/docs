# Function: collectClassNames()

> **collectClassNames**(`element`): `string`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:450](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L450)

Extracts all className strings from a React element tree (recursively).
Uses an array accumulator to avoid O(n²) string concatenation.

## Parameters

### element

`unknown`

## Returns

`string`
