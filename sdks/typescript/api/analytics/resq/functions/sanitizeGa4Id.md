# Function: sanitizeGa4Id()

&gt; **sanitizeGa4Id**(`id`): `any`

Defined in: [resq.ts:105](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/resq.ts#L105)

Validate a GA4 Measurement ID against [GA4\_ID\_PATTERN](../variables/GA4_ID_PATTERN).

Pure and total: never throws, has no effects, and treats any non-matching or
nullish input as a failed validation rather than an error.

## Parameters

### id

`string` \| `null` \| `undefined`

The candidate ID, typically `import.meta.env.VITE_GA4_ID`
  or `process.env.NEXT_PUBLIC_GA4_ID`. Accepts `null`/`undefined` for
  convenience so call sites don't need a guard around env-var reads
  or nullable config fields.

## Returns

`any`

The validated [Ga4MeasurementId](../type-aliases/Ga4MeasurementId) when `id` matches Google's
  format, otherwise the `null` sentinel (also returned for empty, `null`, or
  `undefined` input). Skip GA4 init entirely when this returns `null`.

## Example

```ts
sanitizeGa4Id("G-ABC123"); // → branded "G-ABC123"
sanitizeGa4Id("not-an-id"); // → null
sanitizeGa4Id(undefined); // → null
```
