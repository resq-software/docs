# Function: bind()

> **bind**\<`T`\>(`_target`, `propertyKey`, `descriptor`): `TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method)\<`unknown`\>\>

Defined in: [bind/bind.ts:88](https://github.com/resq-software/npm/blob/f2ab5fc82f4f501236bfdc25d86881be8e1fb643/packages/decorators/src/bind/bind.ts#L88)

Decorator that automatically binds a method to its class instance.
This ensures `this` always refers to the class instance, even when
the method is passed as a callback or stored separately.

Uses lazy binding on first access for better performance.

## Type Parameters

### T

`T` = `unknown`

The type of the class containing the decorated method

## Parameters

### \_target

`T`

The class prototype (unused)

### propertyKey

`string` \| `symbol`

The name of the method

### descriptor

`TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method)\<`unknown`\>\>

The property descriptor

## Returns

`TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method)\<`unknown`\>\>

The modified descriptor

## Throws

When applied to a non-method property

## Example

```typescript
class MyClass {
  private value = 42;

  @bind
  getValue(): number {
    return this.value;
  }

  @bind
  async fetchData(): Promise<Data> {
    return await this.api.getData();
  }
}

const instance = new MyClass();

// Works correctly when passed as callback
const getValue = instance.getValue;
console.log(getValue()); // 42

// Works with async methods too
const fetchData = instance.fetchData;
const data = await fetchData();
```
