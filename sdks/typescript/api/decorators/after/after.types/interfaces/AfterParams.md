# Interface: AfterParams\<D\>

Defined in: [after/after.types.ts:96](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/after/after.types.ts#L96)

Parameters passed to the after hook function.

## Example

```typescript
const params: AfterParams<number> = {
  args: ['input', 42],
  response: 100
};
```

## Type Parameters

### D

`D` = `unknown`

The return type of the decorated method.

## Properties

### args

&gt; **args**: `unknown`[]

Defined in: [after/after.types.ts:98](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/after/after.types.ts#L98)

The exact positional arguments the decorated method was called with.

***

### response

&gt; **response**: `D`

Defined in: [after/after.types.ts:104](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/after/after.types.ts#L104)

The method's **resolved** return value (`Awaited<D>`) — for an async method
the fulfilled value, not the pending promise. The hook only runs on success,
so this is never a rejection.
