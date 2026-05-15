# Type Alias: Method\<D, A\>

> **Method**\<`D`, `A`\> = (...`args`) => `D`

Defined in: [types.ts:31](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/types.ts#L31)

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
