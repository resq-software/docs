# Type Alias: Enumerate\<N, Acc\>

&gt; **Enumerate**\<`N`, `Acc`\> = `Acc`\[`"length"`\] *extends* `N` ? `Acc`\[`number`\] : `Enumerate`\<`N`, \[`...Acc`, `Acc`\[`"length"`\]\]\>

Defined in: [collection.ts:179](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/types/src/collection.ts#L179)

The union of non-negative integer literals strictly below `N` —
`Enumerate<3>` is `0 | 1 | 2`. The engine behind [NumberRange](./NumberRange). Bounded
by the TypeScript recursion limit, so keep `N` below ~1000. `Enumerate<0>` is
`never` (no literals below zero). The `Acc` parameter is an internal
tuple-length accumulator; do not pass it.

## Type Parameters

### N

`N` *extends* `number`

### Acc

`Acc` *extends* `number`[] = \[\]
