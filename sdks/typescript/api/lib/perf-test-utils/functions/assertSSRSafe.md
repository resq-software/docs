# Function: assertSSRSafe()

> **assertSSRSafe**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:820](https://github.com/resq-software/npm/blob/fcf34e40a93a0b7cf8fbc4bf8f456a5c4ab9c4da/packages/ui/src/lib/perf-test-utils.ts#L820)

Bare `window.` or `document.` access outside hooks/callbacks crashes SSR.
We check for these globals at the module level (outside useEffect,
useCallback, useLayoutEffect, or event handler bodies).

## Parameters

### source

`string`

### file

`string`

## Returns

`void`
