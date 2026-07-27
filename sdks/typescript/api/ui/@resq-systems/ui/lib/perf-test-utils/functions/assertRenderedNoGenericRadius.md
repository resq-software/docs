# Function: assertRenderedNoGenericRadius()

&gt; **assertRenderedNoGenericRadius**(`classes`, `componentName`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:570](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L570)

Render-time variant of [assertNoGenericRadius](./assertNoGenericRadius). Pass the
concatenated `className` string from a rendered tree.

## Parameters

### classes

`string`

### componentName

`string`

## Returns

`void`

## Throws

When `classes` contains a generic radius utility.
