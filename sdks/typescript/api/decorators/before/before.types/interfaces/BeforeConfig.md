# Interface: BeforeConfig\<T\>

Defined in: [before/before.types.ts:40](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/before/before.types.ts#L40)

Configuration options for the

## Before

decorator.

 BeforeConfig

## Example

```typescript
// Using a function reference
const config1: BeforeConfig<MyClass> = {
  func: () => console.log('Before method'),
  wait: false
};

// Using a method name
const config2: BeforeConfig<MyClass> = {
  func: 'validate',
  wait: true
};
```

## Type Parameters

### T

`T`

The type of the class containing the decorated method

## Properties

### func

> **func**: ((...`args`) => `unknown`) \| keyof `T`

Defined in: [before/before.types.ts:42](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/before/before.types.ts#L42)

The before function to execute, or a method name on the class

***

### wait?

> `optional` **wait?**: `boolean`

Defined in: [before/before.types.ts:44](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/before/before.types.ts#L44)

Whether to wait for the before function to complete before executing the method
