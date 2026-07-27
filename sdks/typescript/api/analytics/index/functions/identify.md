# Function: identify()

&gt; **identify**(`userId`, `traits?`): `void`

Defined in: [index.ts:472](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/analytics/src/index.ts#L472)

Bind an identity on the shared [analytics](../variables/analytics) singleton. Convenience
wrapper over [Analytics.identify](../classes/Analytics#identify).

## Parameters

### userId

`string`

The stable user identifier.

### traits?

`Record`\<`string`, `unknown`\>

Optional user properties / person profile fields.

## Returns

`void`
