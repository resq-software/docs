# Type Alias: RemoveIndexSignature\<T\>

&gt; **RemoveIndexSignature**\<`T`\> = `{ [K in keyof T as string extends K ? never : number extends K ? never : symbol extends K ? never : K]: T[K] }`

Defined in: [object.ts:152](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/object.ts#L152)

Strip index signatures (`[k: string]` / `[k: number]`), keeping only the
explicitly-declared keys. Useful for turning a loose record back into a
closed shape before deriving a `keyof` union from it.

## Type Parameters

### T

`T`
