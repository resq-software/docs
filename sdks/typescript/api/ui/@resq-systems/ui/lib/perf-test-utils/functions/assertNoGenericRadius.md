# Function: assertNoGenericRadius()

&gt; **assertNoGenericRadius**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:173](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L173)

Throw when `source` uses a generic Tailwind radius utility
(`rounded-xl`, `rounded-2xl`, `rounded-3xl`). The design system
pins radii to specific pixel values per `STYLE_GUIDE.md`; the
generic utilities sneak through Tailwind's defaults and break
visual consistency.

## Parameters

### source

`string`

### file

`string`

## Returns

`void`

## Throws

When `source` uses `rounded-xl`/`rounded-2xl`/`rounded-3xl`.
