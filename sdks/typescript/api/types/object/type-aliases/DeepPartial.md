# Type Alias: DeepPartial\<T\>

&gt; **DeepPartial**\<`T`\> = `T` *extends* (...`args`) =&gt; `unknown` ? `T` : `T` *extends* `ReadonlyArray`\<infer U\> ? `ReadonlyArray`\<`DeepPartial`\<`U`\>\> : `T` *extends* `object` ? `{ [K in keyof T]?: DeepPartial<T[K]> }` : `T`

Defined in: [object.ts:88](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L88)

Recursively make every property optional.

## Type Parameters

### T

`T`
