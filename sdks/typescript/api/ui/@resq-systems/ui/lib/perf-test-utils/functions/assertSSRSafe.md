# Function: assertSSRSafe()

&gt; **assertSSRSafe**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:936](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/ui/src/lib/perf-test-utils.ts#L936)

Throw when `source` reads `window.*` or `document.*` at module
scope without any `useEffect` / `useLayoutEffect` / `useCallback`
elsewhere in the file. Bare browser-global access at module load
crashes Next.js / Remix during server-render.

Heuristic: presence of any hook is treated as proof that browser
accesses are guarded. False negatives are acceptable here — this
is a fast-fail tripwire, not a sound type system.

## Parameters

### source

`string`

### file

`string`

## Returns

`void`

## Throws

When `source` reads a `window.*`/`document.*` global and the
  file contains no `useEffect`/`useLayoutEffect`/`useCallback` hook.
