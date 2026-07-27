# Function: assertInteractiveHasFocusVisible()

&gt; **assertInteractiveHasFocusVisible**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:798](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L798)

Throw when a file declares interactive event handlers
(`onClick`/`onKeyDown`/`onPress`) but does not include any
`focus-visible:*` styling and does not delegate to a primitive
(`Button`, `Pressable`, native `button`/`input`) that brings its
own focus ring.

## Parameters

### source

`string`

### file

`string`

## Returns

`void`

## Throws

When `source` has interactive handlers but neither a
  `focus-visible:*` class nor a delegated interactive primitive.
