# Type Alias: ExactTimeReportable\<T\>

> **ExactTimeReportable**\<`T`\> = (`target`, `propertyName`, `descriptor`) => `any`

Defined in: [exec-time/exec-time.types.ts:69](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/exec-time/exec-time.types.ts#L69)

Type for methods that can have their execution time reported.

## Type Parameters

### T

`T`

The type of the class containing the method

## Parameters

### target

`T`

The class prototype

### propertyName

keyof `T`

The name of the method

### descriptor

`TypedPropertyDescriptor`\<`any`\>

The property descriptor

## Returns

`any`

The modified descriptor
