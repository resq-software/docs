# Type Alias: GtagCommand

&gt; **GtagCommand** = \[`"js"`, `Date`\] \| \[`"config"`, [`Ga4MeasurementId`](../../resq/type-aliases/Ga4MeasurementId), [`GtagConfigParams`](../interfaces/GtagConfigParams)?\] \| \[`"event"`, `string`, [`GtagEventParams`](./GtagEventParams)?\] \| \[`"set"`, `string`, [`GtagEventParams`](./GtagEventParams)\] \| \[`"consent"`, `"default"` \| `"update"`, `Readonly`\<`Record`\<`string`, `"granted"` \| `"denied"`\>\>\]

Defined in: [index.ts:179](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L179)

The discriminated union of gtag command tuples this package emits, keyed off
the first element (the command verb). Modeling the calls this way turns every
`gtag(...)` call site into a checked one: a wrong arity, a raw (unbranded)
measurement id, or a nested event param is a compile error rather than a
value silently dropped by GA4 at runtime.

Covers the verbs actually used here (`js`, `config`, `event`, `set`) plus
`consent`, which is part of the gtag contract and cheap to model ahead of
need. Extend this union when a new verb is introduced.
