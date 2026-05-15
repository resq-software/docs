# Type Alias: AsyncMethod\<D, A\>

> **AsyncMethod**\<`D`, `A`\> = (...`args`) => `Promise`\<`D`\>

Defined in: [types.ts:67](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/types.ts#L67)

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
