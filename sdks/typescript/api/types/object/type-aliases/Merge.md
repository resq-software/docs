# Type Alias: Merge\<T, U\>

&gt; **Merge**\<`T`, `U`\> = [`Simplify`](./Simplify)\<`Omit`\<`T`, keyof `U`\> & `U`\>

Defined in: [object.ts:128](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/object.ts#L128)

Shallow-merge `U` onto `T`: keys in both come from `U`, the result is
flattened. `Merge<{ a: 1; b: 2 }, { b: 3; c: 4 }>` is `{ a: 1; b: 3; c: 4 }`.

## Type Parameters

### T

`T`

### U

`U`
