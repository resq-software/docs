# Type Alias: ExactTimeReportable\<T\>

&gt; **ExactTimeReportable**\<`T`\> = (`target`, `propertyName`, `descriptor`) =&gt; `any`

Defined in: [exec-time/exec-time.types.ts:91](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/exec-time/exec-time.types.ts#L91)

Type for methods that can have their execution time reported.

The **dual-protocol** shape of `@execTime`: the same callable must satisfy both
the legacy (`experimentalDecorators`) three-argument method decorator and the
Stage-3 `(value, context)` decorator. The two protocols disagree on the return
type, which is why it is deliberately `any` (see the inline `biome-ignore`) —
any concrete union would break one caller.

## Type Parameters

### T

`T`

The class owning the method; `propertyName` is a `keyof T` in the
  legacy form.

## Parameters

### target

`T`

The class prototype.

### propertyName

keyof `T`

The name of the method.

### descriptor

`TypedPropertyDescriptor`\<[`Method`](../../../types/type-aliases/Method) \| [`AsyncMethod`](../../../types/type-aliases/AsyncMethod)\>

The property descriptor.

## Returns

`any`

The modified descriptor.
