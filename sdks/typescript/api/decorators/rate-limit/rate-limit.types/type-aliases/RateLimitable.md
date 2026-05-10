# Type Alias: RateLimitable\<T, D\>

> **RateLimitable**\<`T`, `D`\> = (`target`, `propertyName`, `descriptor`) => `TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method)\<`D`\>\>

Defined in: [rate-limit/rate-limit.types.ts:170](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/rate-limit/rate-limit.types.ts#L170)

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

`TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method)\<`D`\>\>

The property descriptor

## Returns

`TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method)\<`D`\>\>

The modified descriptor

## Rate Limit

decorator function.
