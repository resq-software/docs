# Type Alias: ReplaceAll\<S, From, To\>

&gt; **ReplaceAll**\<`S`, `From`, `To`\> = `From` *extends* `""` ? `S` : `S` *extends* `` `${infer H}${From}${infer T}` `` ? `` `${H}${To}${ReplaceAll<T, From, To>}` `` : `S`

Defined in: [string.ts:89](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/string.ts#L89)

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
