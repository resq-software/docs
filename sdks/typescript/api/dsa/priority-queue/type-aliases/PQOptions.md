# Type Alias: PQOptions\<T\>

&gt; **PQOptions**\<`T`\> = \[`T`\] *extends* \[`Comparable`\] ? [`PriorityQueueOptions`](../interfaces/PriorityQueueOptions)\<`T`\> : [`PriorityQueueOptions`](../interfaces/PriorityQueueOptions)\<`T`\> & `Required`\<`Pick`\<[`PriorityQueueOptions`](../interfaces/PriorityQueueOptions)\<`T`\>, `"compareFn"`\>\>

Defined in: [priority-queue.ts:63](https://github.com/resq-software/npm/blob/43e4668edb35f1d8b82814020f177750172b932c/packages/dsa/src/priority-queue.ts#L63)

Options refined by element type. For Comparable elements the default
numeric/lexicographic comparator is sound, so `compareFn` stays optional. For
every other element type (objects, tuples, unions, …) a `compareFn` is
**required** — otherwise the default comparator would stringify elements and
silently mis-order them, which is dangerous for a triage/dispatch queue.

## Type Parameters

### T

`T`
