# Function: mkSet()

&gt; **mkSet**(`xs`): [`Value`](../type-aliases/Value)

Defined in: [packages/math/src/value.ts:83](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/math/src/value.ts#L83)

Wrap an iterable of numbers as a `set`-sorted value.

Copies `xs` into a fresh `Set`, so the value is a snapshot: later mutation of
the source is not observable through it, and duplicate elements collapse.

## Parameters

### xs

`Iterable`\<`number`\>

## Returns

[`Value`](../type-aliases/Value)
