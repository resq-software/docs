# Type Alias: ExactTimeReportable\<T\>

> **ExactTimeReportable**\<`T`\> = (`target`, `propertyName`, `descriptor`) => `any`

Defined in: [exec-time/exec-time.types.ts:69](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/exec-time/exec-time.types.ts#L69)

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
