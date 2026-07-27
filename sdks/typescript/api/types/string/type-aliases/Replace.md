# Type Alias: Replace\<S, From, To\>

&gt; **Replace**\<`S`, `From`, `To`\> = `From` *extends* `""` ? `S` : `S` *extends* `` `${infer H}${From}${infer T}` `` ? `` `${H}${To}${T}` `` : `S`

Defined in: [string.ts:78](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/string.ts#L78)

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
