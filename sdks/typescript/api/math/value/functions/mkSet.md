# Function: mkSet()

&gt; **mkSet**(`xs`): [`Value`](../type-aliases/Value)

Defined in: [packages/math/src/value.ts:83](https://github.com/resq-software/npm/blob/a23b0e86db5c4539fd4e521f64c284c116e1324a/packages/math/src/value.ts#L83)

Wrap an iterable of numbers as a `set`-sorted value.

Copies `xs` into a fresh `Set`, so the value is a snapshot: later mutation of
the source is not observable through it, and duplicate elements collapse.

## Parameters

### xs

`Iterable`\<`number`\>

## Returns

[`Value`](../type-aliases/Value)
