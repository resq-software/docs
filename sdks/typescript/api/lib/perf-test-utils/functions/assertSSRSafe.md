# Function: assertSSRSafe()

> **assertSSRSafe**(`source`, `file`): `void`

Defined in: [packages/ui/src/lib/perf-test-utils.ts:820](https://github.com/resq-software/npm/blob/7cb46b2b7e7b1c6ebdc09af26b2a9132a360d5e3/packages/ui/src/lib/perf-test-utils.ts#L820)

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
