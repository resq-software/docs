# Type Alias: DeepReadonly\<T\>

&gt; **DeepReadonly**\<`T`\> = `T` *extends* (...`args`) =&gt; `unknown` ? `T` : `T` *extends* `ReadonlyMap`\<infer K, infer V\> ? `ReadonlyMap`\<`DeepReadonly`\<`K`\>, `DeepReadonly`\<`V`\>\> : `T` *extends* `ReadonlySet`\<infer U\> ? `ReadonlySet`\<`DeepReadonly`\<`U`\>\> : `T` *extends* `ReadonlyArray`\<infer U\> ? `ReadonlyArray`\<`DeepReadonly`\<`U`\>\> : `T` *extends* `object` ? `{ readonly [K in keyof T]: DeepReadonly<T[K]> }` : `T`

Defined in: [object.ts:62](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/object.ts#L62)

Recursively mark every property (and array element, map/set member)
`readonly`. Functions are left intact. Ideal for `as const`-style frozen
configuration and immutable snapshots.

## Type Parameters

### T

`T`
