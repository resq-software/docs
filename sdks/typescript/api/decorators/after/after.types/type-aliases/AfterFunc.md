# Type Alias: AfterFunc\<D\>

> **AfterFunc**\<`D`\> = (`x?`) => `void`

Defined in: [after/after.types.ts:31](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/after/after.types.ts#L31)

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
