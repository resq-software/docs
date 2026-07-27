# Function: assertClassNameMerging()

&gt; **assertClassNameMerging**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:1026](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L1026)

Throw when a component file uses `className` somewhere but never
calls `cn()` to merge incoming `className` with internal classes.
Components that hardcode `className` without merging silently
drop consumer overrides.

Exemptions: barrel files with no `className` usage, and wrappers
that pass `className` straight to a non-relative third-party
import (where the vendor handles merging).

## Parameters

### source

`string`

### file

`string`

## Returns

`void`

## Throws

When a component `file` uses `className` but never calls
  `cn()` and is not one of the exempt cases above.
