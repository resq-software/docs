# Interface: AfterConfig\<T, D\>

Defined in: [after/after.types.ts:57](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/after/after.types.ts#L57)

Configuration options for the

## After

decorator.

 AfterConfig

## Example

```typescript
// Using a function reference
const config1: AfterConfig<MyClass, string> = {
  func: ({ args, response }) => console.log(response),
  wait: false
};

// Using a method name
const config2: AfterConfig<MyClass, string> = {
  func: 'logResult', // Calls this.logResult()
  wait: true
};
```

## Type Parameters

### T

`T` = `any`

The type of the class containing the decorated method

### D

`D` = `any`

The return type of the decorated method

## Properties

### func

> **func**: [`AfterFunc`](../type-aliases/AfterFunc.md)\<`D`\> \| keyof `T`

Defined in: [after/after.types.ts:59](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/after/after.types.ts#L59)

The after function to execute, or a method name on the class

***

### wait?

> `optional` **wait?**: `boolean`

Defined in: [after/after.types.ts:61](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/after/after.types.ts#L61)

Whether to wait for the after function to complete before returning
