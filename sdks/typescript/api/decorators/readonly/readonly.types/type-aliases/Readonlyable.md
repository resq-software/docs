# Type Alias: Readonlyable\<T\>

> **Readonlyable**\<`T`\> = (`target`, `propertyName`, `descriptor`) => `PropertyDescriptor`

Defined in: [readonly/readonly.types.ts:37](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/readonly/readonly.types.ts#L37)

Type for decorators that make methods read-only.

## Type Parameters

### T

`T` = `any`

The type of the class containing the decorated method

## Parameters

### target

`T`

The class prototype

### propertyName

keyof `T`

The name of the method being decorated

### descriptor

`PropertyDescriptor`

The property descriptor

## Returns

`PropertyDescriptor`

The modified descriptor with writable set to false

## Example

```typescript
type ReadonlyMethod = Readonlyable<MyClass>;

const decorator: ReadonlyMethod = (target, key, descriptor) => {
  descriptor.writable = false;
  return descriptor;
};
```
