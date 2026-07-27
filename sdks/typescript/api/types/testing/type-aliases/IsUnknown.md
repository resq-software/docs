# Type Alias: IsUnknown\<T\>

&gt; **IsUnknown**\<`T`\> = [`IsAny`](./IsAny)\<`T`\> *extends* `true` ? `false` : `unknown` *extends* `T` ? `true` : `false`

Defined in: [testing.ts:83](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/testing.ts#L83)

`true` only for the `unknown` type (and not for `any`).

## Type Parameters

### T

`T`
