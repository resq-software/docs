# Interface: GtagConfigParams

Defined in: [index.ts:162](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L162)

Parameters for `gtag("config", id, …)`. A superset of [GtagEventParams](../type-aliases/GtagEventParams)
that also allows the two structured fields this package sets: the
cross-subdomain `linker` allow-list and the identity `user_id`. The tail is
widened to those value shapes (never `any`) so ad-hoc config keys still type.

## Indexable

&gt; \[`key`: `string`\]: `GtagParamValue` \| \{ `domains?`: readonly `string`[]; \}

## Properties

### linker?

&gt; `readonly` `optional` **linker?**: `object`

Defined in: [index.ts:163](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L163)

#### domains?

&gt; `readonly` `optional` **domains?**: readonly `string`[]

***

### user\_id?

&gt; `readonly` `optional` **user\_id?**: `string` \| `null`

Defined in: [index.ts:164](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L164)
