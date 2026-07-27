# Type Alias: DeepMutable\<T\>

&gt; **DeepMutable**\<`T`\> = `T` *extends* (...`args`) =&gt; `unknown` ? `T` : `T` *extends* `ReadonlyMap`\<infer K, infer V\> ? `Map`\<`DeepMutable`\<`K`\>, `DeepMutable`\<`V`\>\> : `T` *extends* `ReadonlySet`\<infer U\> ? `Set`\<`DeepMutable`\<`U`\>\> : `T` *extends* `ReadonlyArray`\<infer U\> ? `DeepMutable`\<`U`\>[] : `T` *extends* `object` ? `{ -readonly [K in keyof T]: DeepMutable<T[K]> }` : `T`

Defined in: [object.ts:75](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L75)

Recursively strip `readonly` — the dual of [DeepReadonly](./DeepReadonly).

## Type Parameters

### T

`T`
