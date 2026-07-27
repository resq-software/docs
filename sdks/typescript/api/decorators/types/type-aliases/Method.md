# Type Alias: Method\<D, A\>

&gt; **Method**\<`D`, `A`\> = (...`args`) =&gt; `D`

Defined in: [types.ts:44](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/decorators/src/types.ts#L44)

A generic method type used throughout decorators.

Models any callable member the package wraps. `A` is a positional-argument
**tuple** (not a loose array), so wrapping preserves arity and per-position
types rather than collapsing them to `unknown[]`.

## Type Parameters

### D

`D` = `unknown`

The value the method returns (for async methods this is the
  `Promise`, not its resolved type — see [AsyncMethod](./AsyncMethod)).

### A

`A` *extends* `unknown`[] = `unknown`[]

The positional argument tuple; `extends unknown[]` keeps it a
  tuple while allowing any shape.

## Parameters

### args

...`A`

## Returns

`D`

## Example

```typescript
const myMethod: Method<number, [string, boolean]> = (name, active) => {
  return active ? name.length : 0;
};
```
