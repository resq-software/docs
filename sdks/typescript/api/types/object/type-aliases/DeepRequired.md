# Type Alias: DeepRequired\<T\>

&gt; **DeepRequired**\<`T`\> = `T` *extends* (...`args`) =&gt; `unknown` ? `T` : `T` *extends* `ReadonlyArray`\<infer U\> ? `ReadonlyArray`\<`DeepRequired`\<`U`\>\> : `T` *extends* `object` ? `{ [K in keyof T]-?: DeepRequired<T[K]> }` : `T`

Defined in: [object.ts:97](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/object.ts#L97)

Recursively make every property required (strip `?`). The dual of [DeepPartial](./DeepPartial).

## Type Parameters

### T

`T`
