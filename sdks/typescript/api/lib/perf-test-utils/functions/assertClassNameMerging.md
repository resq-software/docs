# Function: assertClassNameMerging()

> **assertClassNameMerging**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:886](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L886)

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
