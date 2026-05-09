# Function: measureNestingDepth()

> **measureNestingDepth**(`element`, `current?`): `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:358](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/lib/perf-test-utils.ts#L358)

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
