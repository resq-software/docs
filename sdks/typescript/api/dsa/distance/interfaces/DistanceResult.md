# Interface: DistanceResult

Defined in: [distance.ts:131](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/distance.ts#L131)

Outcome of a non-throwing distance calculation ([Distance.calculateSafe](../classes/Distance#calculatesafe)).

The [valid](#valid) flag governs the other fields: when `valid` is `true`,
`distance` holds a finite result and `error` is absent; when `valid` is
`false`, `distance` is `NaN` and `error` carries the failure message.

## Properties

### distance

&gt; **distance**: `number`

Defined in: [distance.ts:133](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/distance.ts#L133)

The computed distance, or `NaN` when `valid` is `false`.

***

### error?

&gt; `optional` **error?**: `string`

Defined in: [distance.ts:139](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/distance.ts#L139)

Present only when `valid` is `false`: the validation failure message.

***

### formula

&gt; **formula**: [`DistanceFormula`](../type-aliases/DistanceFormula)

Defined in: [distance.ts:135](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/distance.ts#L135)

The formula that was requested (echoed back regardless of outcome).

***

### valid

&gt; **valid**: `boolean`

Defined in: [distance.ts:137](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/distance.ts#L137)

`true` if the calculation succeeded; see the field constraints above.
