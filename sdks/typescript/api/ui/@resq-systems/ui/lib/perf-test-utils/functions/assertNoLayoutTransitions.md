# Function: assertNoLayoutTransitions()

&gt; **assertNoLayoutTransitions**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:196](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L196)

Throw when `source` contains a `transition-[…]` arbitrary value
that animates a layout-bound property (`width`, `height`, `top`,
`left`, `right`, `bottom`, `margin`, `padding`). Animating those
triggers Forced Reflows on every frame; switch to `transform` /
`opacity` for compositor-friendly motion.

Sidebar component files are exempted because their resize anim is
unavoidably layout-bound and is gated by user input.

## Parameters

### source

`string`

### file

`string`

## Returns

`void`

## Throws

When a non-exempt `file` transitions a layout-bound
  property. Sidebar files (matched by name) return without checking.
