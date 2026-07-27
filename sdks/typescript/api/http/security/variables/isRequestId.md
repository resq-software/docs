# Variable: isRequestId

&gt; `const` **isRequestId**: (`value`) =&gt; `value is RequestId` = `requestIdRefiner.is`

Defined in: [packages/http/src/security.ts:137](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/http/src/security.ts#L137)

Type guard: narrows a `string` to [RequestId](../type-aliases/RequestId) when it already consists
solely of the safe charset and is within the length bound.

## Parameters

### value

`string`

## Returns

`value is RequestId`
