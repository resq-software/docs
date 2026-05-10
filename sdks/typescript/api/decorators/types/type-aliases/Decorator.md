# Type Alias: Decorator\<T\>

> **Decorator**\<`T`\> = (`target`, `propertyName`, `descriptor`) => `TypedPropertyDescriptor`\<[`Method`](./Method.md)\<`any`\>\>

Defined in: [types.ts:47](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/types.ts#L47)

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

`TypedPropertyDescriptor`\<[`Method`](./Method.md)\<`any`\>\>

## Returns

`TypedPropertyDescriptor`\<[`Method`](./Method.md)\<`any`\>\>

## Example

```typescript
const myDecorator: Decorator<MyClass> = (target, propertyName, descriptor) => {
  // Decorator implementation
  return descriptor;
};
```
