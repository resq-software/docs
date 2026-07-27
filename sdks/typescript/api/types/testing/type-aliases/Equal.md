# Type Alias: Equal\<X, Y\>

&gt; **Equal**\<`X`, `Y`\> = \<`T`\>() =&gt; `T` *extends* `X` ? `1` : `2` *extends* \<`T`\>() =&gt; `T` *extends* `Y` ? `1` : `2` ? `true` : `false`

Defined in: [testing.ts:48](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/types/src/testing.ts#L48)

Strict type equality. `Equal<X, Y>` is `true` only when `X` and `Y` are
mutually assignable *and* identical — it distinguishes `any` from `unknown`,
`{ a: 1 }` from `{ readonly a: 1 }`, and other pairs that a plain
`X extends Y ? Y extends X` check conflates.

## Type Parameters

### X

`X`

### Y

`Y`
