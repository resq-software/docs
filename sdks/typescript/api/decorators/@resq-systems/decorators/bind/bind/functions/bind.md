# Function: bind()

&gt; **bind**\<`F`\>(`_target`, `propertyKey`, `descriptor`): `TypedPropertyDescriptor`\<`F`\>

Defined in: [bind/bind.ts:91](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/bind/bind.ts#L91)

Decorator that automatically binds a method to its class instance.
This ensures `this` always refers to the class instance, even when
the method is passed as a callback or stored separately.

Uses lazy binding on first access for better performance.

Returns a **new** descriptor whose getter, on first read per instance, binds
the method and redefines the property as a plain own value on that instance —
so it mutates the instance the first time it is accessed, then serves the
cached bound function (idempotent thereafter). The replacement property is
non-enumerable but writable and configurable. The original prototype method is
left intact.

## Type Parameters

### F

`F` *extends* (...`args`) =&gt; `unknown`

The decorated method's function type, preserved end-to-end.

## Parameters

### \_target

`unknown`

The class prototype (unused).

### propertyKey

`string` \| `symbol`

The name of the method.

### descriptor

`TypedPropertyDescriptor`\<`F`\>

The property descriptor.

## Returns

`TypedPropertyDescriptor`\<`F`\>

The modified descriptor.

## Throws

At decoration time, when the descriptor has no method value
  (applied to an accessor or field), with message
  `"@bind is applicable only on methods."`.

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
