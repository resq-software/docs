# Type Alias: DeepRequired\<T\>

&gt; **DeepRequired**\<`T`\> = `T` *extends* (...`args`) =&gt; `unknown` ? `T` : `T` *extends* `ReadonlyArray`\<infer U\> ? `ReadonlyArray`\<`DeepRequired`\<`U`\>\> : `T` *extends* `object` ? `{ [K in keyof T]-?: DeepRequired<T[K]> }` : `T`

Defined in: [object.ts:97](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L97)

Recursively make every property required (strip `?`). The dual of [DeepPartial](./DeepPartial).

## Type Parameters

### T

`T`
