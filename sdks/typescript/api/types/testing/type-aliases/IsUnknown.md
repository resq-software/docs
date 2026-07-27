# Type Alias: IsUnknown\<T\>

&gt; **IsUnknown**\<`T`\> = [`IsAny`](./IsAny)\<`T`\> *extends* `true` ? `false` : `unknown` *extends* `T` ? `true` : `false`

Defined in: [testing.ts:83](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/testing.ts#L83)

`true` only for the `unknown` type (and not for `any`).

## Type Parameters

### T

`T`
