# Function: assertClassNameMerging()

> **assertClassNameMerging**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:886](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/lib/perf-test-utils.ts#L886)

Verifies that a component function accepts and forwards className via
the cn() utility (className merging). Components that hardcode className
without merging break consumer customization.

## Parameters

### source

`string`

### file

`string`

## Returns

`void`
