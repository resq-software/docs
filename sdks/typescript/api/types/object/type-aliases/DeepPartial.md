# Type Alias: DeepPartial\<T\>

&gt; **DeepPartial**\<`T`\> = `T` *extends* (...`args`) =&gt; `unknown` ? `T` : `T` *extends* `ReadonlyArray`\<infer U\> ? `ReadonlyArray`\<`DeepPartial`\<`U`\>\> : `T` *extends* `object` ? `{ [K in keyof T]?: DeepPartial<T[K]> }` : `T`

Defined in: [object.ts:88](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/object.ts#L88)

Recursively make every property optional.

## Type Parameters

### T

`T`
