# Type Alias: RateLimitable\<T, D\>

> **RateLimitable**\<`T`, `D`\> = (`target`, `propertyName`, `descriptor`) => `TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method)\<`D`\>\>

Defined in: [rate-limit/rate-limit.types.ts:170](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/rate-limit/rate-limit.types.ts#L170)

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
