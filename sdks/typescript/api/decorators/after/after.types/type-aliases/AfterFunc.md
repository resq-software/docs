# Type Alias: AfterFunc\<D\>

> **AfterFunc**\<`D`\> = (`x?`) => `void`

Defined in: [after/after.types.ts:31](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/after/after.types.ts#L31)

Function signature for after hooks.

## Type Parameters

### D

`D`

The return type of the decorated method

## Parameters

### x?

[`AfterParams`](../interfaces/AfterParams)\<`D`\>

Parameters containing args and response

## Returns

`void`

## Example

```typescript
const afterHook: AfterFunc<string> = ({ args, response }) => {
  console.log(`Method returned: ${response}`);
};
```
