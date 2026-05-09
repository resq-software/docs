# Function: assertClassNameMerging()

> **assertClassNameMerging**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:886](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L886)

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
