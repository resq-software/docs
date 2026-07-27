# Type Alias: AsyncMethod\<D, A\>

&gt; **AsyncMethod**\<`D`, `A`\> = (...`args`) =&gt; `Promise`\<`D`\>

Defined in: [types.ts:92](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/types.ts#L92)

A generic async method type.

The counterpart to [Method](./Method) for promise-returning members: `D` here is
the **resolved** value, so the method's actual return type is `Promise<D>`.

## Type Parameters

### D

`D` = `unknown`

The value the returned `Promise` resolves to (not the promise
  itself).

### A

`A` *extends* `unknown`[] = `unknown`[]

The positional argument tuple; `extends unknown[]` keeps it a
  tuple while allowing any shape.

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
