# Type Alias: Verify\<T, U\>

&gt; **Verify**\<`T`, `U`\> = `U`

Defined in: [testing.ts:74](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/testing.ts#L74)

Assert that `U` is assignable to `T` (a one-way subtype/constraint check) and
pass `U` through. Unlike [Equal](./Equal), which demands exact identity, this
only checks assignability — use it to lock "X still satisfies contract Y":

## Type Parameters

### T

`T`

### U

`U` *extends* `T`

## Example

```ts
type _ok = Verify<{ id: string }, { id: string; extra: number }>; // ✓
type _no = Verify<{ id: string }, { id: number }>;                 // ✗ compile error
```
