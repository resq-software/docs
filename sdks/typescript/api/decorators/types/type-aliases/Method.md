# Type Alias: Method\<D, A\>

> **Method**\<`D`, `A`\> = (...`args`) => `D`

Defined in: [types.ts:31](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/types.ts#L31)

A generic method type used throughout decorators.

## Type Parameters

### D

`D` = `any`

The return type of the method

### A

`A` *extends* `any`[] = `any`[]

The argument types of the method (as an array)

## Parameters

### args

...`A`

## Returns

`D`

## Example

```typescript
const myMethod: Method<number, [string, boolean]> = (name, active) => {
  return active ? name.length : 0;
};
```
