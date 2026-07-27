# Type Alias: Merge\<T, U\>

&gt; **Merge**\<`T`, `U`\> = [`Simplify`](./Simplify)\<`Omit`\<`T`, keyof `U`\> & `U`\>

Defined in: [object.ts:128](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L128)

Shallow-merge `U` onto `T`: keys in both come from `U`, the result is
flattened. `Merge<{ a: 1; b: 2 }, { b: 3; c: 4 }>` is `{ a: 1; b: 3; c: 4 }`.

## Type Parameters

### T

`T`

### U

`U`
