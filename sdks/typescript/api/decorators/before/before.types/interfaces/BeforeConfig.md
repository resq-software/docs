# Interface: BeforeConfig\<T\>

Defined in: [before/before.types.ts:50](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/before/before.types.ts#L50)

Configuration options for the `@before` decorator.

[func](#func) is resolved at call time: an inline function is invoked directly,
whereas a `keyof T` string names a method looked up on the instance (`this`)
each call — if it does not resolve to a callable, the wrapped call rejects.
With [wait](#wait) set, a throwing hook aborts the method (guard pattern),
making the two fields interdependent rather than orthogonal.

## Example

```typescript
// Using a function reference
const config1: BeforeConfig<MyClass> = {
  func: () => console.log('Before method'),
  wait: false
};

// Using a method name
const config2: BeforeConfig<MyClass> = {
  func: 'validate',
  wait: true
};
```

## Type Parameters

### T

`T`

The class owning the decorated method; constrains the `keyof T`
  method names accepted by [func](#func).

## Properties

### func

&gt; **func**: ((...`args`) =&gt; `unknown`) \| keyof `T`

Defined in: [before/before.types.ts:52](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/before/before.types.ts#L52)

The before function to execute, or the name of a method on the instance.

***

### wait?

&gt; `optional` **wait?**: `boolean`

Defined in: [before/before.types.ts:59](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/decorators/src/before/before.types.ts#L59)

When `true`, the wrapper awaits the hook before running the method, so a
hook that throws or rejects prevents the method from running (a guard).
When `false` or absent (the default), the hook is fired without awaiting and
the method runs regardless of the hook's outcome.
