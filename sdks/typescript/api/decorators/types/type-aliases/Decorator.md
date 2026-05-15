# Type Alias: Decorator\<T\>

> **Decorator**\<`T`\> = (`target`, `propertyName`, `descriptor`) => `TypedPropertyDescriptor`\<[`Method`](./Method)\<`any`\>\>

Defined in: [types.ts:47](https://github.com/resq-software/npm/blob/fe2e20ae9db8398a0db1e3218edaabb3cf7004d6/packages/decorators/src/types.ts#L47)

A generic decorator type for method decorators.

## Type Parameters

### T

`T` = `any`

The class type containing the method

## Parameters

### target

`T`

### propertyName

keyof `T`

### descriptor

`TypedPropertyDescriptor`\<[`Method`](./Method)\<`any`\>\>

## Returns

`TypedPropertyDescriptor`\<[`Method`](./Method)\<`any`\>\>

## Example

```typescript
const myDecorator: Decorator<MyClass> = (target, propertyName, descriptor) => {
  // Decorator implementation
  return descriptor;
};
```
