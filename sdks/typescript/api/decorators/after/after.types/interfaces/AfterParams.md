# Interface: AfterParams\<D\>

Defined in: [after/after.types.ts:80](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/after/after.types.ts#L80)

Parameters passed to the after hook function.

 AfterParams

## Example

```typescript
const params: AfterParams<number> = {
  args: ['input', 42],
  response: 100
};
```

## Type Parameters

### D

`D` = `any`

The return type of the decorated method

## Properties

### args

> **args**: `unknown`[]

Defined in: [after/after.types.ts:82](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/after/after.types.ts#L82)

The arguments passed to the decorated method

***

### response

> **response**: `D`

Defined in: [after/after.types.ts:84](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/after/after.types.ts#L84)

The return value of the decorated method
