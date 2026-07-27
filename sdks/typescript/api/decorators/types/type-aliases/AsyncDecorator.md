# Type Alias: AsyncDecorator\<T\>

&gt; **AsyncDecorator**\<`T`\> = \<`F`\>(`target`, `propertyName`, `descriptor`) =&gt; `TypedPropertyDescriptor`\<`F`\>

Defined in: [types.ts:120](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/types.ts#L120)

A decorator type specifically for async methods.

Generic over the decorated async method `F`, so the descriptor's method type
is **preserved** end-to-end rather than erased to `AsyncMethod<any>`. The
`F extends (...args: never[]) => Promise<unknown>` bound restricts application
to promise-returning methods, and the same `F` is returned so the resolved
type survives.

## Type Parameters

### T

`T` = `unknown`

The class (or prototype) that owns the decorated async method;
  received as `target` but not required to be used.

## Type Parameters

### F

`F` *extends* (...`args`) =&gt; `Promise`\<`unknown`\>

## Parameters

### target

`T`

### propertyName

`PropertyKey`

### descriptor

`TypedPropertyDescriptor`\<`F`\>

## Returns

`TypedPropertyDescriptor`\<`F`\>

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
