# Type Alias: DeepReadonly\<T\>

&gt; **DeepReadonly**\<`T`\> = `T` *extends* (...`args`) =&gt; `unknown` ? `T` : `T` *extends* `ReadonlyMap`\<infer K, infer V\> ? `ReadonlyMap`\<`DeepReadonly`\<`K`\>, `DeepReadonly`\<`V`\>\> : `T` *extends* `ReadonlySet`\<infer U\> ? `ReadonlySet`\<`DeepReadonly`\<`U`\>\> : `T` *extends* `ReadonlyArray`\<infer U\> ? `ReadonlyArray`\<`DeepReadonly`\<`U`\>\> : `T` *extends* `object` ? `{ readonly [K in keyof T]: DeepReadonly<T[K]> }` : `T`

Defined in: [object.ts:62](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L62)

Recursively mark every property (and array element, map/set member)
`readonly`. Functions are left intact. Ideal for `as const`-style frozen
configuration and immutable snapshots.

## Type Parameters

### T

`T`
