# Type Alias: Replace\<S, From, To\>

&gt; **Replace**\<`S`, `From`, `To`\> = `From` *extends* `""` ? `S` : `S` *extends* `` `${infer H}${From}${infer T}` `` ? `` `${H}${To}${T}` `` : `S`

Defined in: [string.ts:78](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/string.ts#L78)

Replace the **first** occurrence of `From` with `To` in `S`, returning `S`
unchanged when `From` does not occur. An empty `From` is a no-op (returns `S`),
guarding against an otherwise non-terminating match.

## Type Parameters

### S

`S` *extends* `string`

### From

`From` *extends* `string`

### To

`To` *extends* `string`
