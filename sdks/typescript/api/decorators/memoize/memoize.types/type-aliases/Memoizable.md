# Type Alias: Memoizable\<T, D\>

> **Memoizable**\<`T`, `D`\> = (`target`, `propertyName`, `descriptor`) => `TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method.md)\<`D`\>\>

Defined in: [memoize/memoize.types.ts:129](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/memoize/memoize.types.ts#L129)

Type for the

## Type Parameters

### T

`T`

The type of the class containing the decorated method

### D

`D`

The return type of the decorated method

## Parameters

### target

`T`

The class prototype

### propertyName

keyof `T`

The name of the method being decorated

### descriptor

`TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method.md)\<`D`\>\>

The property descriptor

## Returns

`TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method.md)\<`D`\>\>

The modified descriptor

## Memoize

decorator function.
