# Type Alias: ReplaceAll\<S, From, To\>

&gt; **ReplaceAll**\<`S`, `From`, `To`\> = `From` *extends* `""` ? `S` : `S` *extends* `` `${infer H}${From}${infer T}` `` ? `` `${H}${To}${ReplaceAll<T, From, To>}` `` : `S`

Defined in: [string.ts:89](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/string.ts#L89)

Replace **every** occurrence of `From` with `To` in `S`, returning `S`
unchanged when `From` does not occur. An empty `From` is a no-op (returns `S`),
so the recursion always terminates.

## Type Parameters

### S

`S` *extends* `string`

### From

`From` *extends* `string`

### To

`To` *extends* `string`
