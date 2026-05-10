# Type Alias: AsyncMethod\<D, A\>

> **AsyncMethod**\<`D`, `A`\> = (...`args`) => `Promise`\<`D`\>

Defined in: [types.ts:67](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/types.ts#L67)

A generic async method type.

## Type Parameters

### D

`D` = `any`

The resolved type of the Promise

### A

`A` *extends* `any`[] = `any`[]

The argument types of the method (as an array)

## Parameters

### args

...`A`

## Returns

`Promise`\<`D`\>

## Example

```typescript
const fetchData: AsyncMethod<User, [string]> = async (userId) => {
  return await api.getUser(userId);
};
```
