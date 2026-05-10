# Function: sanitizeGa4Id()

> **sanitizeGa4Id**(`id`): `string` \| `null`

Defined in: [resq.ts:69](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/analytics/src/resq.ts#L69)

Validate a GA4 Measurement ID against [GA4\_ID\_PATTERN](../variables/GA4_ID_PATTERN.md).

## Parameters

### id

`string` \| `null` \| `undefined`

The candidate ID, typically `import.meta.env.VITE_GA4_ID`
  or `process.env.NEXT_PUBLIC_GA4_ID`. Accepts `null`/`undefined` for
  convenience so call sites don't need a guard around env-var reads
  or nullable config fields.

## Returns

`string` \| `null`

The validated ID when it matches Google's format, otherwise
  `null`. Skip GA4 init entirely when this returns `null`.
