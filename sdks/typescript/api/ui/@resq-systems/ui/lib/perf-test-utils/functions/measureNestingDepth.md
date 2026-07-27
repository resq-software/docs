# Function: measureNestingDepth()

&gt; **measureNestingDepth**(`element`, `current?`): `number`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:401](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L401)

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
