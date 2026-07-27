# Function: map()

&gt; **map**\<`T`, `U`, `E`\>(`fn`): (`result`) =&gt; `Result`\<`U`, `E`\>

Defined in: [packages/helpers/src/helpers.ts:234](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/helpers.ts#L234)

Curried `Result` mapper. Apply a function to the value of a `Success`,
pass `Failure` through unchanged.

## Type Parameters

### T

`T`

### U

`U`

### E

`E`

## Parameters

### fn

(`value`) =&gt; `U`

Pure transformation applied only to the success value.

## Returns

A function `Result<T, E> → Result<U, E>`.

(`result`) =&gt; `Result`\<`U`, `E`\>

## Example

```ts
const doubled = map<number, number, string>((n) => n * 2)(success(21));
// → { success: true, value: 42 }

map<number, number, string>((n) => n * 2)(failure("nope"));
// → { success: false, error: "nope" } (unchanged)
```
