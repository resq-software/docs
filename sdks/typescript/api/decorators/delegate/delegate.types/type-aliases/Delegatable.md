# Type Alias: Delegatable\<T, D\>

> **Delegatable**\<`T`, `D`\> = (`target`, `propertyName`, `descriptor`) => `TypedPropertyDescriptor`\<[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`\>\>

Defined in: [delegate/delegate.types.ts:64](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/delegate/delegate.types.ts#L64)

Type for the

## Type Parameters

### T

`T`

The type of the class containing the decorated method

### D

`D`

The return type of the decorated async method

## Parameters

### target

`T`

The class prototype

### propertyName

keyof `T`

The name of the method being decorated

### descriptor

`TypedPropertyDescriptor`\<[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`\>\>

The property descriptor

## Returns

`TypedPropertyDescriptor`\<[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`\>\>

The modified descriptor

## Delegate

decorator function.
Transforms an async method into one that deduplicates concurrent calls.

## Example

```typescript
type MyDelegatable = Delegatable<MyService, User>;

// Usage in decorator factory
const decorator: MyDelegatable = delegate((id) => id);
```
