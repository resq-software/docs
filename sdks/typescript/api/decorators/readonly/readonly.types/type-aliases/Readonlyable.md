# Type Alias: Readonlyable\<T\>

&gt; **Readonlyable**\<`T`\> = \<`F`\>(`target`, `propertyName`, `descriptor`) =&gt; `TypedPropertyDescriptor`\<`F`\>

Defined in: [readonly/readonly.types.ts:46](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/readonly/readonly.types.ts#L46)

Signature for decorators that make a method read-only.

Generic over the decorated method `F`, so the descriptor's type is preserved
end-to-end rather than erased to `Method<any>` — the shape of the built-in
(itself generic) `MethodDecorator`.

## Type Parameters

### T

`T` = `unknown`

The class type that owns the decorated method.

## Type Parameters

### F

`F` *extends* (...`args`) =&gt; `unknown`

## Parameters

### target

`T`

The class prototype.

### propertyName

`PropertyKey`

The name of the method being decorated.

### descriptor

`TypedPropertyDescriptor`\<`F`\>

The property descriptor.

## Returns

`TypedPropertyDescriptor`\<`F`\>

The modified descriptor with `writable` set to `false`.

## Example

```ts
type ReadonlyMethod = Readonlyable<MyClass>;

const decorator: ReadonlyMethod = (_target, _key, descriptor) => ({
  ...descriptor,
  writable: false,
});
```
