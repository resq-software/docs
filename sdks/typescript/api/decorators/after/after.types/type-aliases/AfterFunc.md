# Type Alias: AfterFunc\<D\>

&gt; **AfterFunc**\<`D`\> = (`x?`) =&gt; `void`

Defined in: [after/after.types.ts:43](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/after/after.types.ts#L43)

Function signature for after hooks.

The payload is **optional** so a hook that ignores the call context can be a
zero-arg function. The declared return is `void` and the hook's return value
is ignored unless [AfterConfig.wait](../interfaces/AfterConfig#wait) is set — in which case a returned
promise is awaited before the decorated method resolves.

## Type Parameters

### D

`D`

The decorated method's resolved return type, surfaced as
  [AfterParams.response](../interfaces/AfterParams#response).

## Parameters

### x?

[`AfterParams`](../interfaces/AfterParams)\<`D`\>

Parameters containing the call arguments and the response.

## Returns

`void`

## Example

```typescript
const afterHook: AfterFunc<string> = ({ args, response }) => {
  console.log(`Method returned: ${response}`);
};
```
