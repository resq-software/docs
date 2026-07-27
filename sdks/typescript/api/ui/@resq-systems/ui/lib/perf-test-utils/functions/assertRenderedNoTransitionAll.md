# Function: assertRenderedNoTransitionAll()

&gt; **assertRenderedNoTransitionAll**(`classes`, `componentName`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:555](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L555)

Render-time variant of [assertNoTransitionAll](./assertNoTransitionAll). Pass the
concatenated `className` string from a rendered tree (collected
via [collectClassNames](./collectClassNames)).

## Parameters

### classes

`string`

### componentName

`string`

## Returns

`void`

## Throws

When `classes` contains the `transition-all` utility.
