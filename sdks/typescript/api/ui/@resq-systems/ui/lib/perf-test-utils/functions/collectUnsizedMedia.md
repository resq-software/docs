# Function: collectUnsizedMedia()

&gt; **collectUnsizedMedia**(`element`, `acc?`): `string`[]

Defined in: [packages/ui/src/lib/perf-test-utils.ts:464](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L464)

Checks whether replaced elements (img, video, iframe, canvas) have
explicit dimensions — missing dimensions are the #1 cause of CLS.

Mutates and returns the `acc` accumulator: a caller-supplied array is
appended to in place (it is not copied). Omit `acc` to collect into a fresh
array. Does not throw.

## Parameters

### element

`unknown`

Tree to walk; non-element values are traversed but ignored.

### acc?

`string`[] = `[]`

Accumulator appended to in place; defaults to a new array.

## Returns

`string`[]

The same `acc`, now holding one message per unsized media element.
