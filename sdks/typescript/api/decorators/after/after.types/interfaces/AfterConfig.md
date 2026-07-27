# Interface: AfterConfig\<T, D\>

Defined in: [after/after.types.ts:73](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/after/after.types.ts#L73)

Configuration options for the `@after` decorator.

[func](#func) is a two-way choice resolved at call time: an inline
[AfterFunc](../type-aliases/AfterFunc) is invoked directly, whereas a `keyof T` string names a
method looked up on the instance (`this`) each call — if that name does not
resolve to a callable, the wrapped call rejects. When `func` is a method name,
the class must actually be the receiver, since the lookup is against `this`.

## Example

```typescript
// Using a function reference
const config1: AfterConfig<MyClass, string> = {
  func: ({ args, response }) => console.log(response),
  wait: false
};

// Using a method name
const config2: AfterConfig<MyClass, string> = {
  func: 'logResult', // Calls this.logResult()
  wait: true
};
```

## Type Parameters

### T

`T` = `unknown`

The class owning the decorated method; constrains the `keyof T`
  method names accepted by [func](#func).

### D

`D` = `unknown`

The decorated method's resolved return type, forwarded to the
  hook as [AfterParams.response](./AfterParams#response).

## Properties

### func

&gt; **func**: [`AfterFunc`](../type-aliases/AfterFunc)\<`D`\> \| keyof `T`

Defined in: [after/after.types.ts:75](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/after/after.types.ts#L75)

The after function to execute, or the name of a method on the instance.

***

### wait?

&gt; `optional` **wait?**: `boolean`

Defined in: [after/after.types.ts:81](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/after/after.types.ts#L81)

When `true`, the wrapper awaits the hook (and any promise it returns) before
resolving to the method's value; when `false` or absent (the default), the
hook is fired without awaiting, so its rejection goes unobserved.
