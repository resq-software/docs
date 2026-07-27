# Type Alias: Ga4MeasurementId

&gt; **Ga4MeasurementId** = `Brand`\<`string`, `"Ga4MeasurementId"`\>

Defined in: [resq.ts:70](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/resq.ts#L70)

A GA4 Measurement ID that has been validated against [GA4\_ID\_PATTERN](../variables/GA4_ID_PATTERN).

Branding separates a checked ID from an arbitrary env string at the type
level: only [sanitizeGa4Id](../functions/sanitizeGa4Id) (the validated boundary) can mint one, so a
raw `process.env.*` value can never reach a gtag sink by accident.
