# Function: assertReducedMotion()

&gt; **assertReducedMotion**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:986](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L986)

Throw when `source` declares custom `animate-*` classes (i.e.
not from `tw-animate-css` defaults) without any
`motion-reduce:*` / `motion-safe:*` / `prefers-reduced-motion`
handling. Prevents shipping animations that ignore the user's
accessibility preference.

## Parameters

### source

`string`

### file

`string`

## Returns

`void`

## Throws

When `source` declares a non-`tw-animate-css` `animate-*`
  class and has no `motion-reduce`/`motion-safe`/`prefers-reduced-motion`
  handling.
