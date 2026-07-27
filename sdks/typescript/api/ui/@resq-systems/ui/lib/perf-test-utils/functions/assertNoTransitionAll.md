# Function: assertNoTransitionAll()

&gt; **assertNoTransitionAll**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:155](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L155)

Throw when `source` contains the `transition-all` Tailwind utility.
`transition-all` animates every changing property on every change,
burning frame budget on layout-bound properties that should stay
static. Use specific transitions (`transition-colors`,
`transition-transform`, …) instead.

## Parameters

### source

`string`

### file

`string`

## Returns

`void`

## Throws

When `source` contains the `transition-all` utility.
