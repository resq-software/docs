# Type Alias: Entries\<T\>

&gt; **Entries**\<`T`\> = `{ [K in keyof T]: [K, T[K]] }`\[keyof `T`\]

Defined in: [object.ts:51](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/object.ts#L51)

Strongly-typed `Object.entries` shape: the tuple union `[K, T[K]]` for each
own key, rather than `[string, unknown]`.

## Type Parameters

### T

`T`
