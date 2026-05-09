# Function: collectUnsizedMedia()

> **collectUnsizedMedia**(`element`, `acc?`): `string`[]

Defined in: [packages/ui/src/lib/perf-test-utils.ts:413](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L413)

Checks whether replaced elements (img, video, iframe, canvas) have
explicit dimensions — missing dimensions are the #1 cause of CLS.

## Parameters

### element

`unknown`

### acc?

`string`[] = `[]`

## Returns

`string`[]
