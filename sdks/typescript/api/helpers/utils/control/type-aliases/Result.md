# ~~Type Alias: Result\<T, E\>~~

&gt; **Result**\<`T`, `E`\> = [`OkResult`](../interfaces/OkResult)\<`T`\> \| [`ErrorResult`](../interfaces/ErrorResult)\<`E`\>

Defined in: [packages/helpers/src/utils/control.ts:108](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/helpers/src/utils/control.ts#L108)

A discriminated union type for handling success and error cases.

Represents either a successful result with a value or a failed result with an error.
This pattern provides type-safe error handling without throwing exceptions. The
[ok](../interfaces/OkResult#ok) property is the discriminant: `true` selects the
[OkResult](../interfaces/OkResult) variant (read `value`), `false` the [ErrorResult](../interfaces/ErrorResult)
variant (read `error`).

## Type Parameters

### T

`T`

### E

`E`

## Example

```ts
function divide(a: number, b: number): Result<number, string> {
  if (b === 0) {
    return Result.err('Division by zero')
  }
  return Result.ok(a / b)
}

const result = divide(10, 2)
if (result.ok) {
  console.log(`Result: ${result.value}`) // Result: 5
} else {
  console.error(`Error: ${result.error}`)
}
```

## Deprecated

Superseded by success / failure from
`@resq-systems/helpers` (the `{ success, value }` Result). Not a drop-in: the
discriminant is renamed `ok` → `success` when migrating. This parallel
`{ ok, value }` type is unused; removed in the next major.
