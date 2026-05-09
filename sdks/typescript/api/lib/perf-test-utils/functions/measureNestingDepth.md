# Function: measureNestingDepth()

> **measureNestingDepth**(`element`, `current?`): `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:358](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L358)

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
