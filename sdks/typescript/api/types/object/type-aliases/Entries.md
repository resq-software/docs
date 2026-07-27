# Type Alias: Entries\<T\>

&gt; **Entries**\<`T`\> = `{ [K in keyof T]: [K, T[K]] }`\[keyof `T`\]

Defined in: [object.ts:51](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/object.ts#L51)

Strongly-typed `Object.entries` shape: the tuple union `[K, T[K]]` for each
own key, rather than `[string, unknown]`.

## Type Parameters

### T

`T`
