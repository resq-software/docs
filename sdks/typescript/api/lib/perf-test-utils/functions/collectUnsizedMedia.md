# Function: collectUnsizedMedia()

> **collectUnsizedMedia**(`element`, `acc?`): `string`[]

Defined in: [packages/ui/src/lib/perf-test-utils.ts:413](https://github.com/resq-software/npm/blob/7b98eb21b0f3a7ae8e470a55763432a4f9283f77/packages/ui/src/lib/perf-test-utils.ts#L413)

Checks whether replaced elements (img, video, iframe, canvas) have
explicit dimensions — missing dimensions are the #1 cause of CLS.

## Parameters

### element

`unknown`

### acc?

`string`[] = `[]`

## Returns

`string`[]
