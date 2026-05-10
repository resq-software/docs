# Interface: AfterParams\<D\>

Defined in: [after/after.types.ts:80](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/after/after.types.ts#L80)

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

Defined in: [after/after.types.ts:82](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/after/after.types.ts#L82)

The arguments passed to the decorated method

***

### response

> **response**: `D`

Defined in: [after/after.types.ts:84](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/after/after.types.ts#L84)

The return value of the decorated method
