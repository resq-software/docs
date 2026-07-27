# Type Alias: Delegatable\<T, D\>

&gt; **Delegatable**\<`T`, `D`\> = (`target`, `propertyName`, `descriptor`) =&gt; `TypedPropertyDescriptor`\<[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`\>\>

Defined in: [delegate/delegate.types.ts:52](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/delegate/delegate.types.ts#L52)

Type for the

## Type Parameters

### T

`T`

The class owning the decorated method; `propertyName` is a
  `keyof T`.

### D

`D`

The value the decorated async method resolves to.

## Parameters

### target

`T`

The class prototype.

### propertyName

keyof `T`

The name of the method being decorated.

### descriptor

`TypedPropertyDescriptor`\<[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`\>\>

The property descriptor.

## Returns

`TypedPropertyDescriptor`\<[`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\<`D`\>\>

The modified descriptor.

## Delegate

decorator function.
Transforms an async method into one that deduplicates concurrent calls.

The legacy (`experimentalDecorators`) method-decorator shape: it accepts and
returns a descriptor over the *same* [AsyncMethod](../../../types/type-aliases/AsyncMethod) type, so the
decorated method keeps its resolved-value signature. It applies only to
promise-returning members, since dedup is defined in terms of an in-flight
promise.

## Example

```typescript
type MyDelegatable = Delegatable<MyService, User>;

// Usage in decorator factory
const decorator: MyDelegatable = delegate((id) => id);
```
