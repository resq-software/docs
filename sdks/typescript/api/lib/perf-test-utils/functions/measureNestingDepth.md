# Function: measureNestingDepth()

> **measureNestingDepth**(`element`, `current?`): `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:358](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L358)

Measures max nesting depth of a React element tree.
Deep trees cause long style recalculation (Style Writes) and slow
selector matching.

## Parameters

### element

`unknown`

### current?

`number` = `0`

## Returns

`number`
