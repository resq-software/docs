# Function: collectUnsizedMedia()

> **collectUnsizedMedia**(`element`, `acc?`): `string`[]

Defined in: [packages/ui/src/lib/perf-test-utils.ts:413](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L413)

Checks whether replaced elements (img, video, iframe, canvas) have
explicit dimensions — missing dimensions are the #1 cause of CLS.

## Parameters

### element

`unknown`

### acc?

`string`[] = `[]`

## Returns

`string`[]
