# Function: collectClassNames()

> **collectClassNames**(`element`): `string`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:450](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L450)

Extracts all className strings from a React element tree (recursively).
Uses an array accumulator to avoid O(n²) string concatenation.

## Parameters

### element

`unknown`

## Returns

`string`
