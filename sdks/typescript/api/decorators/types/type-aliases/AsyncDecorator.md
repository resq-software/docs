# Type Alias: AsyncDecorator\<T\>

> **AsyncDecorator**\<`T`\> = (`target`, `propertyName`, `descriptor`) => `TypedPropertyDescriptor`\<[`AsyncMethod`](./AsyncMethod.md)\<`any`\>\>

Defined in: [types.ts:89](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/types.ts#L89)

A decorator type specifically for async methods.

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

`TypedPropertyDescriptor`\<[`AsyncMethod`](./AsyncMethod.md)\<`any`\>\>

## Returns

`TypedPropertyDescriptor`\<[`AsyncMethod`](./AsyncMethod.md)\<`any`\>\>

## Example

```typescript
const asyncDecorator: AsyncDecorator<MyClass> = (target, propertyName, descriptor) => {
  const original = descriptor.value!;
  descriptor.value = async function(...args) {
    console.log('Before async call');
    const result = await original.apply(this, args);
    console.log('After async call');
    return result;
  };
  return descriptor;
};
```
