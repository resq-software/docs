# Type Alias: Decorator\<T\>

&gt; **Decorator**\<`T`\> = \<`F`\>(`target`, `propertyName`, `descriptor`) =&gt; `TypedPropertyDescriptor`\<`F`\>

Defined in: [types.ts:68](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/types.ts#L68)

A generic decorator type for method decorators.

Generic over the decorated method `F`, so the descriptor's method type is
**preserved** end-to-end (exactly the built-in `MethodDecorator` shape)
rather than erased to `Method<any>`. `(...args: never[]) => unknown` is the
correct "any function" bound (arguments are contravariant). The decorator
returns a descriptor of the *same* `F`, so callers see no signature change —
this is the legacy (`experimentalDecorators`) three-argument shape, not the
Stage-3 form.

## Type Parameters

### T

`T` = `unknown`

The class (or prototype) that owns the decorated method; the
  decorator receives it as `target` but is not required to use it.

## Type Parameters

### F

`F` *extends* (...`args`) =&gt; `unknown`

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
const myDecorator: Decorator<MyClass> = (target, propertyName, descriptor) => {
  // Decorator implementation
  return descriptor;
};
```
