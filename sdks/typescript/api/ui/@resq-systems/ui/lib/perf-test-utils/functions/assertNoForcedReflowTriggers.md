# Function: assertNoForcedReflowTriggers()

&gt; **assertNoForcedReflowTriggers**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:218](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L218)

Throw when `source` reads a layout-triggering DOM property
(`offsetWidth`, `getBoundingClientRect`, `getComputedStyle`, …).
These cause synchronous layout when called after a style write,
destroying frame budget. Batch reads before writes or replace
with `ResizeObserver` / `IntersectionObserver`.

## Parameters

### source

`string`

### file

`string`

## Returns

`void`

## Throws

When `source` reads a layout-triggering DOM property.
