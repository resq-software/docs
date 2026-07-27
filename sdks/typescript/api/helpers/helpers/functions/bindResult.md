# Function: bindResult()

&gt; **bindResult**\<`T`, `U`, `E`\>(`fn`): (`result`) =&gt; `Result`\<`U`, `E`\>

Defined in: [packages/helpers/src/helpers.ts:256](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L256)

Curried `Result` flatMap (also known as `chain` or `bind`). Like
[map](./map) but the transformation itself returns a `Result`, allowing
fallible steps to be sequenced without nesting.

## Type Parameters

### T

`T`

### U

`U`

### E

`E`

## Parameters

### fn

(`value`) =&gt; `Result`\<`U`, `E`\>

Result-returning step applied to the success value.

## Returns

A function `Result<T, E> → Result<U, E>`.

(`result`) =&gt; `Result`\<`U`, `E`\>

## Example

```ts
const validateAge = (n: number): Result<number, string> =>
  n >= 0 && n < 150 ? success(n) : failure("out of range");

bindResult(validateAge)(success(42)); // → success(42)
bindResult(validateAge)(success(-1)); // → failure("out of range")
```
